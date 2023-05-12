from django.db import models

class Personne(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(default='toto@gmail.com')
    age = models.IntegerField(default=0)  # Valeur par défaut ajoutée

    def __str__(self):
        return self.nom
