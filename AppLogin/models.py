from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
    def __str__(self):
        return f"Foto : {self.imagen}, Usuario : {self.user}, Email : {self.user.email}, Nombre : {self.user.first_name}"
        return super().__str__()

##################
#################
##############