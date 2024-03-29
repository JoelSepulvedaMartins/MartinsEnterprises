from django.db import models

# Create your models here.

##Django adiciona o id por padrao
class Services(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=120)
    message = models.TextField(max_length=1000)  
    telephone = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name