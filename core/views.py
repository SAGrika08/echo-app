from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Scene, SceneSound, Sound
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')


class SoundList(LoginRequiredMixin, ListView):
    model = Sound

    def get_queryset(self):
        return Sound.objects.filter(user=self.request.user)

class SoundCreate(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'core/sound_form.html')

    def post(self, request):
        name = request.POST.get('name')
        sound_type = request.POST.get('type')
        sound = Sound(name=name, type=sound_type)

        if sound_type == 'uploaded':
            sound.file = request.FILES.get('file')
        elif sound_type == 'url':
            sound.url = request.POST.get('url')

        sound.user = request.user
        sound.save()
        return redirect('sound-index')



class SoundUpdate(LoginRequiredMixin, UpdateView):
    model = Sound
    fields = ['name']

class SoundDelete(LoginRequiredMixin, DeleteView):
    model = Sound
    success_url = reverse_lazy('sound-index')

class SceneList(LoginRequiredMixin,ListView):
    model = Scene

    def get_queryset(self):
        return Scene.objects.filter(user=self.request.user)


class SceneDetail(LoginRequiredMixin, DetailView):
    model = Scene  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sounds_not_in_scene = Sound.objects.exclude(id__in=self.object.sounds.all().values_list('id'))
        context['scene_sounds'] = SceneSound.objects.filter(scene=self.object)
        context['sounds_not_in_scene'] = sounds_not_in_scene
        return context

class SceneUpdate(LoginRequiredMixin, UpdateView):
    model = Scene
    fields = ['name', 'is_public']

class SceneDelete(LoginRequiredMixin, DeleteView):
    model = Scene
    success_url = reverse_lazy('scene-index')   

class MixerView(LoginRequiredMixin, View):

    def get(self, request):
        sounds = Sound.objects.all()
        return render(request, 'scenes/mixer.html', {'sounds': sounds})

    def post(self, request):
        name = request.POST.get('name')
        is_public = request.POST.get('is_public') == 'on'

        scene = Scene.objects.create(
            name=name,
            is_public=is_public,
            user=request.user
        )

        selected_sounds = request.POST.getlist('sounds')

        for sound_id in selected_sounds:
            level = request.POST.get(f'level_{sound_id}', 50)
            SceneSound.objects.create(
                scene=scene,
                sound_id=sound_id,
                level=int(level)
            )

        return redirect('scene-detail', pk=scene.id)

@login_required
def add_sound_to_scene(request, scene_id):
    if request.method == 'POST':
        sound_id = request.POST.get('sound_id')
        level = request.POST.get('level', 50)
        SceneSound.objects.create(scene_id=scene_id, sound_id=sound_id, level=int(level))
    return redirect('scene-detail', pk=scene_id)

@login_required
def remove_sound_from_scene(request, scene_id, sound_id):
    if request.method == 'POST':
        SceneSound.objects.filter(scene_id=scene_id, sound_id=sound_id).delete()
    return redirect('scene-detail', pk=scene_id)        

@login_required
def update_sound_level_in_scene(request, scene_id, sound_id):
    if request.method == 'POST':
        level = request.POST.get('level', 50)
        scene_sound = SceneSound.objects.filter(scene_id=scene_id, sound_id=sound_id).first()
        if scene_sound:
            scene_sound.level = int(level)
            scene_sound.save()
    return redirect('scene-detail', pk=scene_id)

@login_required
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('sound-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = SignUpForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)