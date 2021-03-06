# Generated by Django 2.0.7 on 2018-07-13 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='../media/image')),
                ('caption', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_text', models.CharField(max_length=64)),
                ('word_def', models.TextField()),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('forget_count', models.IntegerField(default=0)),
                ('correct_in_row', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wordcards.Word'),
        ),
    ]
