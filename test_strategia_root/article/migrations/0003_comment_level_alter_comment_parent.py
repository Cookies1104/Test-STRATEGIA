# Generated by Django 4.0.4 on 2022-04-14 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_alter_comment_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='level',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_%(class)s', to='article.comment', verbose_name='parent comment'),
        ),
    ]