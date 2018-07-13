# Model definition for app wordcards
import datetime
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe


class Word(models.Model):
    word_text = models.CharField(max_length=64)
    word_def = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True)
    forget_count = models.IntegerField(default=0)
    correct_in_row = models.IntegerField(default=0)
    list_display = ('word_text', 'add_date', 'forget_count', 'correct_in_row')
    list_filter = ['forget_count', 'correct_in_row']
    search_fields = ['word_text']

    def __str__(self):
        return self.word_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.add_date <= now

    was_published_recently.admin_order_field = 'Add_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Added recently?'


class Image(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='../media/image')
    caption = models.CharField(max_length=128)
    list_display = ('word', 'caption', 'image')
    search_fields = ['caption']


