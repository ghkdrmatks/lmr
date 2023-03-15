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
    address = models.CharField(max_length=45)
    business_hours = models.CharField(max_length=20, blank=True, null=True)

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


class ReviewImage(models.Model):
    id = models.IntegerField(primary_key=True)
    fllename = models.CharField(max_length=20, blank=True, null=True)
    filepath = models.CharField(max_length=45, blank=True, null=True)
    review = models.ForeignKey(Review, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'review_image'


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
