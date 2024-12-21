def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return f"{Fore.RED}Give me name and phone please.{Fore.RESET}"
        except KeyError:
            return f"{Fore.RED}Contact does not exist.{Fore.RESET}"
        except IndexError:
            return f"{Fore.RED}Please provide contact name or number.{Fore.RESET}"

    return inner