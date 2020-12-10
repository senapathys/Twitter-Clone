from django.contrib import admin
from main.models import Tweet, Hashtag, Follow

# Register your models here.

admin.site.register(Tweet)
admin.site.register(Hashtag)
admin.site.register(Follow)

