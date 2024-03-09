from django.db import models

class Publicite(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    photo = models.ImageField(upload_to='publicite/img/', null=True, blank=True)
    pdf = models.FileField(upload_to='publicite/pdf/', null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.titre

class Evenement(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    lien = models.URLField(default='http://example.com')
    photo = models.ImageField(upload_to='evenement/img/', null=True, blank=True)
    pdf = models.FileField(upload_to='evenement/pdf/', null=True, blank=True)
    date_debut = models.DateTimeField(null=True, blank=True)
    date_fin = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.nom

class Team(models.Model):
    nom = models.CharField(max_length=200)
    poste = models.TextField()
    photo = models.ImageField(upload_to='team/img/', null=True, blank=True)
    facebook = models.URLField(max_length=200, default='https://www.facebook.com')
    linkedin = models.URLField(max_length=200, default='https://www.linkedin.com')
    youtube = models.URLField(max_length=200, default='https://www.youtube.com')
    twitter = models.URLField(max_length=200, default='https://www.twitter.com')
    def __str__(self):
        return self.nom


class Newsletters(models.Model):
    email = models.EmailField()
    def __str__(self):
        return f"{self.email}"

class Inscription(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.IntegerField()
    sexe = models.CharField(max_length=1, choices=[('M', 'Masculin'), ('F', 'Féminin')])
    email = models.EmailField()
    profession = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)
    situation_matrimoniale = models.CharField(
        max_length=1,
        choices=[('C', 'Célibataire'), ('M', 'Marié(e)'), ('D', 'Divorcé(e)'), ('V', 'Veuf/Veuve')]
    )
    contact = models.TextField()

    def __str__(self):
        return f"{self.nom} {self.prenom}"



class Contact(models.Model):
    nom = models.CharField(max_length=500)
    email = models.EmailField()
    contact = models.TextField()
    sujet = models.CharField(max_length=500)
    message = models.TextField()
    def __str__(self):
        return f"{self.nom}"
