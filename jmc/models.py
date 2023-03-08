# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Allergy(models.Model):
    id = models.IntegerField(primary_key=True)
    allergy_name = models.CharField(db_column='allergy_ name', max_length=20, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'allergy'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    menu_type_code = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    restaurant = models.ForeignKey('Restaurant', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'menu'


class MenuAllergy(models.Model):
    allergy = models.ForeignKey(Allergy, models.DO_NOTHING)
    menu = models.ForeignKey(Menu, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'menu_allergy'


class MenuImage(models.Model):
    id = models.IntegerField(primary_key=True)
    filename = models.CharField(max_length=20, blank=True, null=True)
    filepath = models.CharField(max_length=45, blank=True, null=True)
    menu = models.ForeignKey(Menu, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'menu_image'


class MenuRecommendLog(models.Model):
    id = models.IntegerField(primary_key=True)
    datetime = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING)
    menu = models.ForeignKey(Menu, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'menu_recommend_log'


class NutritionInformation(models.Model):
    id = models.IntegerField(primary_key=True)
    ingredients = models.CharField(max_length=20, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    calories = models.IntegerField(blank=True, null=True)
    carbohydrates = models.IntegerField(blank=True, null=True)
    sugar = models.IntegerField(blank=True, null=True)
    protein = models.IntegerField(blank=True, null=True)
    fat = models.IntegerField(blank=True, null=True)
    trans_fat = models.IntegerField(blank=True, null=True)
    saturation_fat = models.IntegerField(blank=True, null=True)
    cholesterol = models.IntegerField(blank=True, null=True)
    sodium = models.IntegerField(blank=True, null=True)
    menu = models.ForeignKey(Menu, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'nutrition_information'


class PreferredMenu(models.Model):
    menu_type_code = models.IntegerField()
    preference = models.IntegerField()
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'preferred_menu'


class Restaurant(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=45)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restaurant'


class RestaurantImage(models.Model):
    id = models.IntegerField(primary_key=True)
    filename = models.CharField(max_length=20, blank=True, null=True)
    filepath = models.CharField(max_length=45, blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'restaurant_image'


class Review(models.Model):
    id = models.IntegerField(primary_key=True)
    rating = models.FloatField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING)
    menu = models.ForeignKey(Menu, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'review'


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=45)
    email = models.CharField(unique=True, max_length=30)
    gender = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserAllergy(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    allergy = models.ForeignKey(Allergy, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_allergy'
