from django.db import models

class Info(models.Model):
    recipe_name = models.CharField(max_length=40)
    cuisine_name = models.CharField(max_length=40)
    recipe_text = models.CharField(max_length= 500)
    Ingredient1 = models.CharField(max_length=30)
    Ingredient2 = models.CharField(max_length=30)
    Ingredient3 = models.CharField(max_length=30)
    Ingredient4 = models.CharField(max_length=30)
    Ingredient1_cost = models.IntegerField(default=0)
    Ingredient2_cost = models.IntegerField(default=0)
    Ingredient3_cost = models.IntegerField(default=0)
    Ingredient4_cost = models.IntegerField(default=0)
    total = models.IntegerField(default=0)  
    def __unicode__(self):
       return self.recipe_name
   
