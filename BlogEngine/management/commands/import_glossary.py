import csv
from django.core.management.base import BaseCommand
from BlogEngine.models import Glossary  
from django.utils.text import slugify

def get_unique_slug(model_instance, slugable_field_name, slug_field_name):
    slug = slugify(getattr(model_instance, slugable_field_name))
    unique_slug = slug
    num = 1
    while model_instance.__class__.objects.filter(**{slug_field_name: unique_slug}).exists():
        unique_slug = '{}-{}'.format(slug, num)
        num += 1
    return unique_slug


class Command(BaseCommand):
    help = 'Loads data from CSV into the Glossary model'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='Path to the CSV file with glossary data')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file_path']
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                term = row['Tech Topic']
                glossary, created = Glossary.objects.get_or_create(term=term)
                if created:
                    glossary.definition = row['HTML Definition']
                    glossary.description = row.get('HTML Description', '')
                    glossary.slug = get_unique_slug(glossary, 'term', 'slug')
                    glossary.save()
                else:
                    self.stdout.write(self.style.WARNING(f'Skipped duplicate term: {term}'))
            self.stdout.write(self.style.SUCCESS('Successfully imported glossary data'))
