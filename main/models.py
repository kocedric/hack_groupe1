from django.db import models


class Portfolio(models.Model):
    title = models.CharField('Titre', max_length=80, unique=True)
    date = models.DateField()
    image = models.ImageField(upload_to='images', null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Galerie"

    def __str__(self):
        return self.title
