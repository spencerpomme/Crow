from django.contrib import admin

from .models import Word, Image


class WordAdmin(admin.ModelAdmin):
    fields = ['word_text', 'word_def', 'forget_count', 'correct_in_row']
    list_display = ('id', 'word_text', 'word_def', 'forget_count', 'correct_in_row', 'add_date')
    list_filter = ['forget_count']
    search_fields = ['word_text']


class ImageAdmin(admin.ModelAdmin):
    fields = ['word', 'caption', 'image']
    list_display = ('word', 'caption', 'image')
    search_fields = ['caption']


admin.site.register(Word, WordAdmin)
admin.site.register(Image, ImageAdmin)
