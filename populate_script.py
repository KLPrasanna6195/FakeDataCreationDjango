import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','dummydataproject.settings')
django.setup()

from faker import Faker
from dummydata.models import users
from django.utils import timezone

import datetime
start_date = datetime.date(year=2020, month=1, day=1)


def create_post(N):
    fake = Faker()
    for _ in range(N):
        fid = fake.pyint()
        freal_name = fake.name()
        ftz= fake.country()
        factivity_periods = timezone.now()
        fstart_time = fake.date_time_this_year()
        fEnd_time = fake.date_between(start_date=start_date, end_date='now')
        Users = users.objects.get_or_create(id=fid,real_name=freal_name,tz=ftz,activity_periods=factivity_periods,
                                                start_time = fstart_time,End_time = fEnd_time),

create_post(10)
print('Data is populated successfully')