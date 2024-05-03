import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            new_phone = Phone(phone.get('id'), phone.get('name'), phone.get('image'),
                      phone.get('price'), phone.get('release_date'), phone.get('lte_exists'),
                      slugify(phone.get('name'), allow_unicode=True))
            new_phone.save()