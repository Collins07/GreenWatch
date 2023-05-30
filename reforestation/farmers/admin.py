from django.contrib import admin
from farmers.models import Image, Profile,Comment, Follow

# Register your models here.
admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Follow)