from helpers import parse_input
from func_command import *
from contacts_models import *
from contacts_data import load_data, save_data
from colorama import Fore, Style, init


def main():
    book = load_data()
    # book = AddressBook()
    print(f"{Fore.LIGHTYELLOW_EX}Welcome to the assistant bot!{Style.RESET_ALL}")
    while True:
        user_input = input(f"{Fore.BLUE}Enter a command: {Style.RESET_ALL}")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            save_data(book)
            print(f"{Fore.YELLOW}Goodbye!{Style.RESET_ALL}")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) >= 2:
                print(add_contact(args, book))
            else:
                print(f"{Fore.RED}Expected at least 2 arguments: name and phone.{Fore.RESET}")    
        elif command == "change":
            if len(args) >= 3:
                print(change_contact(args, book))
            else:
                print(f"{Fore.RED}Expected 3 arguments: name, old phone and new phone.{Fore.RESET}")
        elif command == "phone":
            if len(args) >= 1:
                print(show_contact(args, book))
            else:
                print(f"{Fore.RED}Expected 1 argument: name.{Fore.RESET}")
        elif command == "all":
            print(show_all_contact(book))   
        elif command == "delete":
            if len(args) >= 1:
                print(delete_contact(args, book))
            else:
                print(f"{Fore.RED}Expected 2 arguments: name and phone.{Fore.RESET}") 
        elif command == "add-birthday":
            if len(args) >= 2:
                print(add_birthday(args, book))
            else:
                print(f"{Fore.RED}Usage: add-birthday <name> <birthday (DD.MM.YYYY)>{Fore.RESET}")
        elif command == "show-birthday":
            if len(args) >= 1:
                print(show_birthday(args, book))
            else:
                print(f"{Fore.RED}Usage: show-birthday <name>{Fore.RESET}")
        elif command == "birthdays":
            print(birthdays(args, book))        
        else:
            print(f"{Fore.RED}Invalid command. Please try again.{Fore.RESET}")


if __name__ == "__main__":
    main()