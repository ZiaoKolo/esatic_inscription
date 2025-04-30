# inscription/models.py
from django.db import models

class Candidat(models.Model):
    FILIERE_CHOICES = [
        ('informatique', 'Informatique'),
        ('reseaux', 'Réseaux et Télécommunications'),
        ('securite', 'Sécurité Informatique'),
        ('autre', 'Autre'),
    ]
    
    nom = models.CharField(max_length=100)
    prenoms = models.CharField(max_length=200)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    filiere = models.CharField(max_length=50, choices=FILIERE_CHOICES)
    
    # Documents scannés
    cni = models.FileField(upload_to='documents/cni/')
    diplome = models.FileField(upload_to='documents/diplomes/')
    photo = models.ImageField(upload_to='documents/photos/')
    
    # Informations de soumission
    date_soumission = models.DateTimeField(auto_now_add=True)
    code_inscription = models.CharField(max_length=20, unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        # Générer un code d'inscription si nouveau candidat
        if not self.code_inscription:
            import random
            import string
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            self.code_inscription = f"ESATIC-{code}"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.nom} {self.prenoms} - {self.code_inscription}"