from django.core.management.base import BaseCommand
from BlogEngine.models import Glossary
from BlogEngine.openai_connector import call_chat_gpt

class Command(BaseCommand):
    help = 'Fetches a description for a given term using ChatGPT'

    def add_arguments(self, parser):
        parser.add_argument('term', type=str, help='The term to define')

    def handle(self, *args, **options):
        term_name = options['term']
        # term, created = Glossary.objects.get_or_create(name=term_name)
        # if not term.description:  # Only fetch if no description already exists
        #     prompt = f"Define the term: {term.name}"
        #     response = call_chat_gpt(prompt)
        #     term.description = response  # Assuming the API call returns the description directly
        #     term.save()
        #     self.stdout.write(self.style.SUCCESS(f'Successfully updated term: {term.name} with description: {term.description}'))
        # else:
        #     self.stdout.write(self.style.WARNING(f'Description already exists for term: {term.name}'))

        prompt = f"Define the term: {term_name}"
        response = call_chat_gpt(prompt)
        self.stdout.write(self.style.SUCCESS(f'Successfully updated term: {term_name} with description: {response}'))