from django.db import models


# Create your models here.

class Hrac(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Jméno hráče',
                            help_text='Zadej jméno hráče', )

    country = models.CharField(max_length=50,
                               verbose_name='Národnost',
                               help_text='Zadej národnost hráče', )

    born = models.DateField(verbose_name='Datum narození',
                            help_text='Zadejte, prosím, datum ve formátu: <em>den.měsíc.rok</em>', )

    class Meta:
        verbose_name = 'Hráč'
        verbose_name_plural = 'Hráči'
        ordering = ['name']

    def __str__(self):
        return self.name


class Tym(models.Model):
    name = models.CharField(max_length=50,
                            unique=True,
                            verbose_name='Název týmu',
                            help_text='Zadej název týmu', )

    player = models.ManyToManyField(Hrac,
                                    verbose_name='Zadej hráče',
                                    help_text='Zadej jméno hráče',
                                    )

    class Meta:
        verbose_name = 'Tým'
        verbose_name_plural = 'Týmy'
        ordering = ['name']

    def __str__(self):
        return self.name
