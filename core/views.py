from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Scene, SceneSound, Sound
from django.urls import reverse_lazy


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class SoundList(ListView):
    model = Sound

class SoundCreate(CreateView):
    model = Sound
    fields = ['name', 'type', 'file', 'url']

    # def form_valid(self, form):
    # form.instance.user = self.request.user
    # return super().form_valid(form)


class SoundUpdate(UpdateView):
    model = Sound
    fields = ['name']

class SoundDelete(DeleteView):
    model = Sound
    success_url = reverse_lazy('sound-index')

class SceneList(ListView):
    model = Scene

class SceneDetail(DetailView):
    model = Scene  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sounds_not_in_scene = Sound.objects.exclude(id__in=self.object.sounds.all().values_list('id'))
        context['scene_sounds'] = SceneSound.objects.filter(scene=self.object)
        context['sounds_not_in_scene'] = sounds_not_in_scene
        return context

class SceneUpdate(UpdateView):
    model = Scene
    fields = ['name', 'is_public']

class SceneDelete(DeleteView):
    model = Scene
    success_url = reverse_lazy('scene-index')   

class MixerView(View):

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

def add_sound_to_scene(request, pk):
    if request.method == 'POST':
        sound_id = request.POST.get('sound_id')
        level = request.POST.get('level', 50)
        SceneSound.objects.create(scene_id=pk, sound_id=sound_id, level=int(level))
    return redirect('scene-detail', pk=pk)

def remove_sound_from_scene(request, scene_id, sound_id):
    if request.method == 'POST':
        SceneSound.objects.filter(scene_id=scene_id, sound_id=sound_id).delete()
    return redirect('scene-detail', pk=scene_id)        

def update_sound_level_in_scene(request, scene_id, sound_id):
    if request.method == 'POST':
        level = request.POST.get('level', 50)
        scene_sound = SceneSound.objects.filter(scene_id=scene_id, sound_id=sound_id).first()
        if scene_sound:
            scene_sound.level = int(level)
            scene_sound.save()
    return redirect('scene-detail', pk=scene_id)


