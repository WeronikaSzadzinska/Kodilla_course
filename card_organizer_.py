

from faker import Faker
from datetime import datetime
    
class BaseContact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email
    
    def __str__(self):
        return f'{self.name} {self.email}'
    
    def __repr__(self):
        return f"BaseContact(make={self.name} phone_number={self.phone_number} mail={self.email})"
    
    @property
    def contact(self):
        return print(f"Wybieram numer: {self.phone_number} i kontaktuję się z: {self.name}")
    
    @property
    def length_count(self):
        return print(len(self.name)+1)

class BusinessContact(BaseContact):
    def __init__(self, company, job, company_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.job = job
        self.company_phone = company_phone

    def __repr__(self):
        return f"BusinessContact(make={self.name}, company={self.company}, company_phone={self.company_phone} job={self.job}, phone_number={self.phone_number} mail={self.email})"
    
    def __str__(self):
        return f'{self.name} {self.email} {self.company}'


def create_cards(card_type, quantity):
    
    quantity = int(quantity)
    now1 = datetime.now()
    contacts = []
    if card_type == 'P':
        for n in range(quantity):
            fake = Faker()
            contact = BaseContact(name = fake.name(), phone_number=fake.phone_number(), email = fake.email())
            contacts.append(contact)
    if card_type == 'B':
        for n in range(quantity):
            fake = Faker()
            contact = BusinessContact(name = fake.name(), company = fake.company(), company_phone = fake.phone_number(), job = fake.job(), phone_number=fake.phone_number(), email = fake.email())
            contacts.append(contact)   
    now2 = datetime.now()
    t = now2-now1
    print(f"time needed in the loop {t}")
    for n in contacts:
        print(n)

card_type = input("cards should be business [B] or personal [P]? ")    
quantity = input("how many cards you want? " )
create_cards(card_type, quantity)




