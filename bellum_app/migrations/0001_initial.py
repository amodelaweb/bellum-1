# Generated by Django 2.0.5 on 2018-05-12 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('creation_field', models.DateTimeField()),
                ('modification_time', models.DateTimeField()),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Group_Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.IntegerField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bellum_app.Group')),
            ],
        ),
        migrations.CreateModel(
            name='INode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('path', models.CharField(max_length=300)),
                ('type', models.CharField(choices=[('DIR', 'Directory'), ('FILE', 'File')], max_length=5)),
                ('creation_field', models.DateTimeField()),
                ('modification_time', models.DateTimeField()),
                ('permission', models.IntegerField(default=0)),
                ('password', models.CharField(max_length=400)),
                ('last_hash', models.CharField(max_length=400)),
                ('groups', models.ManyToManyField(related_name='inodes', through='bellum_app.Group_Object', to='bellum_app.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('ADM', 'Administrator'), ('USR', 'User')], max_length=4)),
                ('permission', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_field', models.DateTimeField()),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('user_name', models.CharField(max_length=25, unique=True)),
                ('modification_time', models.DateTimeField()),
                ('password', models.CharField(max_length=100)),
                ('password_change', models.DateTimeField()),
                ('private_key', models.CharField(max_length=300, unique=True)),
                ('public_key', models.CharField(max_length=200, unique=True)),
                ('logs', models.CharField(max_length=300)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bellum_app.Role')),
            ],
        ),
        migrations.CreateModel(
            name='User_Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.IntegerField()),
                ('inode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bellum_app.INode')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bellum_app.User')),
            ],
        ),
        migrations.AddField(
            model_name='inode',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bellum_app.User'),
        ),
        migrations.AddField(
            model_name='inode',
            name='users',
            field=models.ManyToManyField(related_name='inodes', through='bellum_app.User_Object', to='bellum_app.User'),
        ),
        migrations.AddField(
            model_name='group_object',
            name='inode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bellum_app.INode'),
        ),
        migrations.AddField(
            model_name='group',
            name='users',
            field=models.ManyToManyField(related_name='groups', to='bellum_app.User'),
        ),
    ]
