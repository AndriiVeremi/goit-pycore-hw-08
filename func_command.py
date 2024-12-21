from decorators import input_error
from colorama import Fore, Style, init

init(autoreset=True) 

@input_error
def add_contact(args, book):
    name, phone, *_ = args
    record = book.find_record(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = f"{Fore.GREEN}Contact added.{Fore.RESET}"
    else:
        message = f"{Fore.GREEN}Contact updated.{Fore.RESET}"
    record.add_phone(phone)
    return message


@input_error
def change_contact(args, book):
    name, old_phone, new_phone = args
    record = book.find_record(name)
    if record is None: 
        return f"{Fore.RED}No contact found with name {name}.{Style.RESET_ALL}"
    return record.edit_phone(old_phone, new_phone)
    
    
@input_error
def show_contact(args, book):
    name = args[0]
    record = book.find_record(name)
    if isinstance(record, str):
        return record
    return str(record)
 
 
@input_error
def show_all_contact(book):
    if not book:  
        return f"{Fore.RED}No contacts saved.{Style.RESET_ALL}" 
    result = "\n".join(
        f"{name}: {', '.join(f"{Fore.MAGENTA}{phone.value}{Style.RESET_ALL}" for phone in record.phones)}"
        for name, record in book.items()
    )    
    return result


@input_error
def delete_contact(args, book):
    name, phone = args
    record = book.find_record(name)
    if isinstance(record, str):
        return record
    return record.remove_phone(phone)
    
    
@input_error
def add_birthday(args, book):
    name, birthday = args
    record = book.find_record(name)
    if isinstance(record, str):  
        return record
    return record.add_birthday(birthday)


@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find_record(name)
    if isinstance(record, str):  
        return record
    if record.birthday:
        return f"{Fore.BLUE}Birthday of {name}: {record.birthday.value.strftime('%d.%m.%Y')}{Style.RESET_ALL}"
    else:
        return f"{Fore.LIGHTYELLOW_EX}{name} does not have a birthday set.{Style.RESET_ALL}"


@input_error
def birthdays(args, book):
    days = int(args[0]) if args else 7  
    upcoming = book.get_upcoming_birthdays(days)
    if not upcoming:
        return "No upcoming birthdays."
    result = "\n".join(
        f"{Fore.LIGHTYELLOW_EX}{record.name.value}: {record.birthday.value.strftime('%d.%m.%Y')} ({record.days_to_birthday()} days left){Style.RESET_ALL}"
        for record in upcoming
    )
    return  f"{Fore.LIGHTYELLOW_EX}Upcoming birthdays:\n{result}{Fore.RESET}"
    
    
