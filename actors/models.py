from django.db import models

NATIONALITY_CHOICES = (
  ('USA', 'Estados Unidos'),
  ('BRAZIL', 'Brasil')
)


class Actors(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(blank=True, null=True)
    nationality = models.CharField(choices=NATIONALITY_CHOICES, blank=True, null=True, max_length=200)

    def __str__(self):
        return self.name
