import csv
from django.core.management.base import BaseCommand
from search.models import Restaurant

class Command(BaseCommand):
    help = 'Load data from restaurants_small.csv into Restaurant model'

    def handle(self, *args, **kwargs):
        with open('C:\\Users\\DELL\\Downloads\\restaurants_small.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Restaurant.objects.create(name=row['name'])
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
