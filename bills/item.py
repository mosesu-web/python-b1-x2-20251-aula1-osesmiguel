from enum import Enum
import datetime
from .entity import *

# Do not change the value of ISD_FACTOR var
ISD_FACTOR = 0.25


class TaxType(Enum):
    # Do not change this enum
    IVA = 1
    ISD = 2


class Tax:
    # Write the parameters in the next line
    def __init__(self, tax_id: str, tax_type: TaxType, percentage: float) -> None:
        # Write here your code
        self.tax_id: str = tax_id
        self.tax_type: TaxType = tax_type
        self.percentage: float = percentage


class Product:
     # Write the parameters in the next line
    def __init__(self, product_id: str, name: str, expiration_date: datetime.date, 
                bar_code: str, quantity: int, price: float, taxes: list[Tax]) -> None:
        # Write here your code
        self.product_id: str = product_id
        self.name: str = name
        self.expiration_date: datetime.date = expiration_date
        self.barcode: str = bar_code
        self.quantity: int = quantity
        self.price: float = price
        self.taxes: list[Tax] = taxes

    def calculate_tax(self, tax: Tax) -> float:
        # Write here your code
        if tax.tax_type == TaxType.ISD:
            return self.quantity*self.price*tax.percentage*ISD_FACTOR
        else:
            return self.quantity*self.price*tax.percentage

    def calculate_total_taxes(self) -> float:
        # Write here your code
        total_taxes: float = 0.0
        for tax in self.taxes:
            total_taxes += self.calculate_tax(tax)
        return total_taxes
    
    def calculate_total(self) -> float:
        # Write here your code
        return (self.quantity*self.price
                + self.calculate_total_taxes())

    def __eq__(self, another: object) -> bool:
        # Do not change this method
        return hasattr(another, 'product_id') and self.product_id == another.product_id

    def __hash__(self):
        # Do not change this method
        return hash(self.product_id)

    def print(self):
        # Do not change this method
        print(
            f"Product Id:{self.product_id} , name:{self.name}, quantity:{self.quantity}, price:{self.price}")
        for tax in self.taxes:
            print(f"Tax:{tax.tax_type} , percentage:{tax.percentage}")


class Bill:
    def __init__(self, bill_id: str, sale_date: datetime.date, seller: Seller, buyer: Buyer, products: list[Product]):
        # Write here your code
        self.bill_id: str = bill_id
        self.sale_date: datetime.date = sale_date
        self.seller: Seller = seller
        self.buyer: Buyer = buyer
        self.products: list[Product] = products

    def calculate_total(self) -> float:
        # Write here your code
        total_bill: float = 0.0
        for product in self.products:
            total_bill += product.calculate_total()
        return total_bill

    def print(self):
        # Do not change this method
        self.buyer.print()
        self.seller.print()
        for product in self.products:
            product.print()
