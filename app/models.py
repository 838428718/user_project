# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models



class User(models.Model):
    uid = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    account = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    group = models.ForeignKey('UserGroup', models.DO_NOTHING, db_column='group', blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user'


class UserGroup(models.Model):
    gid = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=255, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user_group'
