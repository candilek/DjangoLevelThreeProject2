import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
#ortam ayarlarını varsayılan olarak environ yaptık.

import django
django.setup()

import random
from appTwo.models import User
from faker import Faker

fakegen=Faker()#fakegen nesnesi oluşturarak Faker metodunu içine attık

def populate(N=5):

    for entry in range(N):
        fake_name=fakegen.name().split() #ismi boşluk karakterine göre bölmek için split() metodunu kullandık
        fake_first_name=fake_name[0]
        fake_last_name=fake_name[1]
        fake_email=fakegen.email()
#veritabanı için yeni bir giriş oluşturalım.Kullanıcı nesnesi
        user=User.objects.get_or_create(first_name=fake_first_name,
                                        last_name=fake_last_name,
                                         email=fake_email)[0]
if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)#20 tane kayıt getirsin.
    print('Populating Complete')
