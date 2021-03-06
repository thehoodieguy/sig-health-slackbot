# Generated by Django 3.0.1 on 2019-12-28 22:39

from django.db import migrations, models
import django.db.models.manager
import django.utils.timezone
import django_enumfield.db.fields
import django_project.utils
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmojiTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', django_enumfield.db.fields.EnumField(default=0, enum=django_project.utils.TaskStatus)),
                ('execute_at', models.DateTimeField(verbose_name='실행 일시')),
                ('name', models.CharField(max_length=100, verbose_name='이모지 이름')),
                ('timestamp', models.CharField(max_length=100, verbose_name='이모지 달 메세지 타임스탬프')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('unexecuted', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='MessageTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', django_enumfield.db.fields.EnumField(default=0, enum=django_project.utils.TaskStatus)),
                ('execute_at', models.DateTimeField(verbose_name='실행 일시')),
                ('text', models.TextField(verbose_name='보낼 텍스트')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('unexecuted', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ReplyTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', django_enumfield.db.fields.EnumField(default=0, enum=django_project.utils.TaskStatus)),
                ('execute_at', models.DateTimeField(verbose_name='실행 일시')),
                ('thread_ts', models.CharField(max_length=100, verbose_name='댓글을 달기 위한 쓰레드')),
                ('text', models.TextField(verbose_name='보낼 텍스트')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('unexecuted', django.db.models.manager.Manager()),
            ],
        ),
    ]
