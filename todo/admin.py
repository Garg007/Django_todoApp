from django.contrib import admin

# Register your models here.
from .models import Todo1, Feedback, UserProfile

admin.site.register(Todo1)
admin.site.register(Feedback)
admin.site.register(UserProfile)
