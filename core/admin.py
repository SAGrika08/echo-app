from django.contrib import admin
from .models import Scene, Sound, SceneSound

admin.site.register(Sound)
admin.site.register(Scene)
admin.site.register(SceneSound)

