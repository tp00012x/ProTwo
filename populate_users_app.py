import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

from users_app.models import User
from faker import Faker

fake = Faker()


def populate_users(n=5):
    for _ in range(n):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()

        u = User.objects.get_or_create(first_name=first_name, last_name=last_name, email=email)[0]
        u.save()


if __name__ == '__main__':
    populate_users(20)
    print('Populated 20 users')
