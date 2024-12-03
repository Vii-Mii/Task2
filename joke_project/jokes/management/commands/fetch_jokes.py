from django.core.management.base import BaseCommand
from jokes.services import fetch_and_store_jokes

class Command(BaseCommand):
    help = 'Fetch jokes from JokeAPI and store them in the database'

    def handle(self, *args, **kwargs):
        fetch_and_store_jokes()
        self.stdout.write(self.style.SUCCESS('Successfully fetched and stored jokes'))
