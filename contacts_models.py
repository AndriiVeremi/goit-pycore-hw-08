from collections import UserDict
from datetime import datetime, timedelta
from colorama import Fore, Style, init

init(autoreset=True) 

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        self.value = name

class Phone(Field):
    def __init__(self, value):
        if len(value) != 10:
            raise ValueError(f"{Fore.RED}A phone number must be 10 digits long{Fore.RESET}")
        if not value.isdigit():
            raise ValueError(f"{Fore.RED}The phone number must contain only digits{Fore.RESET}")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError(f"{Fore.RED}Invalid date format. Use DD.MM.YYYY{Fore.RESET}")
        
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None    
    
    def edit_phone(self, old_phone, new_phone):
        for idx, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[idx] = Phone(new_phone)
                return f"{Fore.GREEN}Phone {old_phone} changed to {new_phone}.{Fore.RESET}"        
        return f"{Fore.RED}Phone {old_phone} not found.{Fore.RESET}"
         
    def remove_phone(self, phone):
        for idx, p in enumerate(self.phones):
            if p.value == phone:
                del self.phones[idx]
                return f"{Fore.GREEN}Phone {phone} removed.{Fore.RESET}"
            return f"{Fore.RED}Phone {phone} not found.{Fore.RESET}"    
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
        return f"{Fore.GREEN}Birthday {birthday} added to contact {self.name.value}.{Fore.RESET}"

    def days_to_birthday(self):
        if self.birthday:
            today = datetime.now().date()
            next_birthday = self.birthday.value.replace(year=today.year).date()
            if next_birthday < today:
                next_birthday = next_birthday.replace(year=today.year + 1)
            return (next_birthday - today).days
        return None                    

    def __str__(self):
        phones = '; '.join(p.value for p in self.phones)
        birthday = f", birthday: {self.birthday}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {phones}{birthday}"
    

class AddressBook(UserDict):
    
    def add_record(self, record):
        self.data[record.name.value] = record
        return f"Record for {record.name.value} added."
    
    def find_record(self, name):
        return self.data.get(name, None)
    
    def get_upcoming_birthdays(self, days=7):
        today = datetime.now().date()
        upcoming = []
        for record in self.data.values():
            if record.birthday:
                next_birthday = record.birthday.value.replace(year=today.year).date()
                if next_birthday < today:
                    next_birthday = next_birthday.replace(year=today.year + 1)
                if 0 <= (next_birthday - today).days <= days:
                    upcoming.append(record)
        return upcoming
    
    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
    
   