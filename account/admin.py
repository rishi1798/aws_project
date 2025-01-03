from django.contrib import admin
from account.models import User
from .models import Photo
# Register your models here.

admin.site.register(User)

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
