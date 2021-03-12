from django.db import models


class Portfolio(models.Model):
    title = models.CharField('Titre', max_length=80)
    date = models.DateField()
    image = models.ImageField(upload_to='images', null=True, blank=True)
    description = models.DateField(blank=True)

    class Meta:
        verbose_name = "Galerie"

    def __str__(self):
        return self.title
