from django.db import models


class Portfolio(models.Model):
	GALERIE = (
	    ('A', 'App'),
	    ('M', 'Meeting'),
	    ('O', 'Autre'),
	)
	galerie = models.CharField(max_length=1, choices=GALERIE)

	title = models.CharField('Titre', max_length=80, unique=True)
	date = models.DateField()
	image = models.ImageField(upload_to='images', null=True, blank=True)
	description = models.TextField(blank=True, null=True)

	class Meta:
	    verbose_name = "Galerie"

	def __str__(self):
	    return self.title



class Presentation(models.Model):

	name = models.CharField('Nom', max_length=255, unique=True)
	role = models.CharField(max_length=255, unique=False)
	image = models.ImageField(upload_to='images', null=True, blank=True)
	description = models.TextField(blank=True, null=True)
	twitter_link = models.TextField("Lien vers votre page twitter", null=True, blank=True)
	facebook_link = models.TextField("Lien vers votre page facebook", null=True, blank=True)
	instagram_link = models.TextField("Lien vers votre page instagram", null=True, blank=True)
	linkedin_link = models.TextField("Lien vers votre page linkedin", null=True, blank=True)

	class Meta:
	    verbose_name = "Presentation"

	def __str__(self):
	    return self.name	    
