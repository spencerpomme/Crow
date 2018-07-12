from django.contrib import admin

from .models import Word, Image


class WordAdmin(admin.ModelAdmin):
    fields = ['word_id', 'word_text', 'word_def', 'add_date', 'forget_count']
    list_display = ('word_text', 'word_def', 'add_date', 'forget_count')


class ImageAdmin(admin.ModelAdmin):
    fields = ['id', 'word', 'caption', 'image']
    list_display = ('id', 'word', 'caption', 'image')


admin.site.register(Word, WordAdmin)
admin.site.register(Image, ImageAdmin)
