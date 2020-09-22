from django.db import models


class PlaceOfCollisions(models.Model):
    """ модель места концентрации ДТП """
    latitude = models.DecimalField('широтка центра места концентрации ДТП', max_digits=8)
    longitude = models.DecimalField('долгота центра места концентрации ДТП', max_digits=8)
    location = models.CharField('расположение город/вне города', max_length=50)
