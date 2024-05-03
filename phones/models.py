from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length = 30)
    image = models.TextField()
    price = models.IntegerField()
    release_date = models.DateField()
    lte_exists = models.BooleanField(default="True")
    slug = models.SlugField(blank=True, unique=True, verbose_name='URL')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug)
        super(Phone, self).save(*args, **kwargs)