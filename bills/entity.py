from abc import ABC, abstractmethod

class Person:
    def __init__(self, dni: str, email: str, mobile: str) -> None:
        # Write here your code
        self.dni: str = dni
        self.email: str = email
        self.mobile: str = mobile

    @abstractmethod
    def print(self):
        pass

    def __eq__(self, another: object) -> bool:
       # Do not change this method
       return hasattr(another, 'dni') and self.dni == another.dni
    
    def __hash__(self):
       # Do not change this method
       return hash(self.dni)

class Buyer(Person):
    def __init__(self, dni: str, email: str, mobile: str, full_name: str, age: int, address: str):
        # Write here your code
        super().__init__(dni, email, mobile)
        self.full_name: str = full_name
        self.age: int = age
        self.address: str = address

    def print(self):
        # Do not change this method
        print(f"Buyer: {self.dni}, email:{self.email}")

class Seller(Person):
    # Write the parameters in the next line
    def __init__(self, dni: str, email: str, mobile: str, business_name: str, business_address: str):
        # Write here your code        
        super().__init__(dni, email, mobile)
        self.business_name: str = business_name
        self.business_address: str = business_address
        
    def print(self):
        # Do not change this method
        print(f"Seller: {self.dni} , email:{self.email} ")
