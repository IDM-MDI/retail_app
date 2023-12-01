import random

from django.core.management.base import BaseCommand
from django.db.models import Q
from faker import Faker
from electronics_retail.models import Retail, Product, Contact, Address  # Import your models
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Populate database with fake data'
    fake = Faker()

    def handle(self, *args, **kwargs):
        self.create_products()
        self.create_users()
        self.create_retails()
        self.create_retails()
        self.stdout.write(self.style.SUCCESS('Successfully populated fake data'))

    def create_products(self):
        for _ in range(50):
            Faker.seed(random.random())
            Product.objects.create(
                name=self.fake.unique.word(),
                category=self.fake.word(),
                release=self.fake.date_this_decade()
            )

    def create_users(self):
        for _ in range(20):
            User.objects.create(
                username=self.fake.unique.user_name(),
                password=self.fake.unique.password(),
                email=self.fake.unique.email()
            )

    def create_retails(self):
        for _ in range(20):
            Faker.seed(random.random())
            choice = random.choice(['FC', 'DB', 'DL', 'LR', 'IE'])
            retail = Retail.objects.create(
                name=self.fake.company(),
                contact=Contact.objects.create(
                    email=self.fake.unique.email(),
                    address=Address.objects.create(
                        country=self.fake.country(),
                        city=self.fake.city(),
                        district=self.fake.address(),
                        number=self.fake.building_number()
                    )
                ),
                debt=random.uniform(100, 10000),
                type=choice
            )
            products_count = random.randint(1, 5)
            products = Product.objects.order_by('?').all()[:products_count]
            retail.products.set(products)

            users_count = random.randint(1, 3)
            users = User.objects.filter(~Q(is_staff=True) & ~Q(is_superuser=True)).order_by('?').all()[:users_count]
            retail.users.set(users)

            if choice != 'FC' and Retail.objects.exists():
                retail.provider = Retail.objects.order_by('?').first()

            retail.save()

