from django.urls import path
from . import views 
from .views import signup

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('explore/', views.ExploreView.as_view(), name='explore'),
    path('sounds/', views.SoundList.as_view(), name='sound-index'),
    path('sounds/create/', views.SoundCreate.as_view(), name='sound-create'),
    path('sounds/<int:pk>/edit/', views.SoundUpdate.as_view(), name='sound-edit'),
    path('sounds/<int:pk>/delete/', views.SoundDelete.as_view(), name='sound-delete'),
    path('scenes/', views.SceneList.as_view(), name='scene-index'),
    path('mixer/', views.MixerView.as_view(), name='mixer'),
    path('scenes/<int:pk>/', views.SceneDetail.as_view(), name='scene-detail'),
    path('scenes/<int:pk>/edit/', views.SceneUpdate.as_view(), name='scene-update'),
    path('scenes/<int:pk>/delete/', views.SceneDelete.as_view(), name='scene-delete'),
    path('accounts/signup/', signup, name='signup'),
]
