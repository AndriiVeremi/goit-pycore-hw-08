import pickle
from contacts_class import AddressBook

def save_data(book, filename="address_book.pkl"):
    with open(filename, "wb") as file:
        pickle.dump(book, file)


def load_data(filename="address_book.pkl"):
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return AddressBook()