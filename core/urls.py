from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('sounds/', views.SoundList.as_view(), name='sound-index'),
    path('sounds/create/', views.SoundCreate.as_view(), name='sound-create'),
    path('sounds/<int:pk>/edit/', views.SoundUpdate.as_view(), name='sound-edit'),
    path('sounds/<int:pk>/delete/', views.SoundDelete.as_view(), name='sound-delete'),
    path('scenes/', views.SceneList.as_view(), name='scene-index'),
    path('mixer/', views.MixerView.as_view(), name='mixer'),
    path('scenes/<int:pk>/', views.SceneDetail.as_view(), name='scene-detail'),
    path('scenes/<int:pk>/edit/', views.SceneUpdate.as_view(), name='scene-update'),
    path('scenes/<int:pk>/delete/', views.SceneDelete.as_view(), name='scene-delete'),
    path('scenes/<int:scene_id>/add_sound/', views.add_sound_to_scene, name='add-sound-to-scene'),
    path('scenes/<int:scene_id>/remove_sound/<int:sound_id>/', views.remove_sound_from_scene, name='remove-sound-from-scene'),
    path('scenes/<int:scene_id>/update_sound_level/<int:sound_id>/', views.update_sound_level_in_scene, name='update-sound-level-in-scene'),
]
