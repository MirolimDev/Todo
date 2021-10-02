from django.db import models
# from django.db.models.aggregates import Max

# Create your models here.

class CreateModel(models.Model):
    type_name = models.CharField(max_length=150)
    succesfull_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type_name

