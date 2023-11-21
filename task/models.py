from django.db import models

# Create your models here.
class CreateTaskModel(models.Model):
    id=models.IntegerField(primary_key=True)
    title= models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    is_completed = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title