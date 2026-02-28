from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

CHOICES = (
    ('recorded', 'Recorded'),
    ('uploaded', 'Uploaded'),
    ('url', 'URL'),
)

class Sound(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=CHOICES, default=CHOICES[0][0])
    file = models.FileField(upload_to='sounds/', null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('sound-index')
    
class Scene(models.Model):
    name = models.CharField(max_length=200)
    is_public = models.BooleanField(default=False)
    sounds = models.ManyToManyField(Sound, through='SceneSound')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('scene-detail', kwargs={'pk': self.id})
    
class SceneSound(models.Model):
    scene = models.ForeignKey(Scene, on_delete=models.CASCADE)
    sound = models.ForeignKey(Sound, on_delete=models.CASCADE)
    level = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.sound.name} in {self.scene.name} at {self.level}"
