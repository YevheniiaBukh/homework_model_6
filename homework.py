
from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name: str):
        super().__init__(name)

        

class Phone(Field):
    def __init__(self, phone: str):
        super().__init__(phone)
       
    def validate_phone(self):
        if len(self.value) == 10 and self.value.isdigit():
            return f' Your number is correct {self.value} '
        else:
            return "Phone must counain exactly 10 digits"
        
# phone = Phone("2341116791")
# phone.validate_phone()      
# print(phone.validate_phone())


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
            
    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))
    
    def remove_phone(self, phone: str):
        found = self.find_phone(phone)
        if found is None:
           return "Phone not found"
        self.phones.remove(found)
        
    def edit_phone(self, old_phone: str, new_phone: str):
        found = self.find_phone(old_phone)
        if found is None:
           return "Phone not found"
       
       
       
    def find_phone(self, phone: str):
        for item in self.phones:
            if item.value == phone:
                return item
            return None
        
    def __str__(self):
                return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
            
  
class AddressBook(UserDict): 
    def add_record(self, record: Record):
        self.data[record.name.value] = record
        
    def find(self, name: str):
        return self.data.get(name)
    
    def delete(self, name: str):
        self.data.pop(name)

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
    


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
     
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

# Виведення: Contact name: John, phones: 1112223333; 5555555555
print(john)  

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")
