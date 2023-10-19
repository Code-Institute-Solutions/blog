from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    list_display = ('title',)
    search_fields = ['title', 'content']
    summernote_fields = ('content',)
