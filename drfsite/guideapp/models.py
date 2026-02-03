from django.db import models

class Sportsman(models.Model):
    name = models.CharField(max_length = 40)
    age = models.IntegerField()
    time_created = models.DateTimeField(auto_now_add = True)
    time_update = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField()
    cat = models.ForeignKey('Category', on_delete = models.PROTECT, null = True)


    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 40, db_index = True)

    def __str__(self):
        return self.name

    