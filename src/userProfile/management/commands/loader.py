from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth import get_user_model
from recommenderEngine.utils import create_fake_data

User = get_user_model()

class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser):
        parser.add_argument("count", nargs='?', default=10, type=int)
        parser.add_argument("--show-total", action='store_true', default=False)

    def handle(self, *args: Any, **options: Any):
        count = options.get('count')
        show_total= options.get('show_total')
        profiles = create_fake_data(count = count)
        new_users = []
        for profile in profiles:
            new_users.append(
                User(**profile)
                )
        userBulk = User.objects.bulk_create(new_users, ignore_conflicts=True)
        print(f"NEW USER CREATED = {len(userBulk)}")
        if show_total:
            print(f"Total users = {User.objects.count()}")
        # return super().handle(*args, **options) 