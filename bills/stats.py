# Write your imports here
from .entity import Buyer, Seller
from .item import Product, Bill
from enum import Enum


class OrderType:
    # Do not change this enum
    ASC = 0
    DES = 1


class Statistics:
    def __init__(self, bills: list[Bill]):
        # Do not change this method
        self.bills = bills

    def find_top_sell_product(self) -> (Product, int):
        # Write here your code
        top_products: dict[Product, int] = {}
        for bill in self.bills:
            for product in bill.products:
                if product in top_products:
                    top_products[product] += 1
                else:
                    top_products[product] = 1
        return sorted(top_products.items(), key=lambda item: item[1], reverse= True)[0]

    def find_top_two_sellers(self) -> list:
        # Write here your code
        top_sellers: dict[Seller, float] = {}
        for bill in self.bills:
            if bill.seller in top_sellers:
                top_sellers[bill.seller] += bill.calculate_total()
            else:
                top_sellers[bill.seller] = bill.calculate_total()
        sorted_top_sellers: list[tuple[Seller, float]] = sorted(top_sellers.items(), key= lambda item: item[1], reverse= True)
        if len(top_sellers) > 1:
            return [sorted_top_sellers[0][0], sorted_top_sellers[1][0]]
        elif len(top_sellers) == 1:
            return [sorted_top_sellers[0][0]]

    def find_buyer_lowest_total_purchases(self) -> (Buyer, float):
        # Write here your code
        buyers_ranking: dict[Buyer, float] = {}
        for bill in self.bills:
            if bill.buyer in buyers_ranking:
                buyers_ranking[bill.buyer] += bill.calculate_total()
            else:
                buyers_ranking[bill.buyer] = bill.calculate_total()
        return sorted(buyers_ranking.items(), key= lambda item: item[1])[0]

    def order_products_by_tax(self, order_type: OrderType) -> tuple:
        # Write here your code
        products_by_tax: dict[Product, float] = {}
        reverse: bool = False
        for bill in self.bills:
            for product in bill.products:
                if product in products_by_tax:
                    products_by_tax[product] += product.calculate_total_taxes()
                else:
                    products_by_tax[product] = product.calculate_total_taxes()
        if order_type == OrderType.DES:
            reverse = True
        return sorted(products_by_tax.items(), key= lambda item: item[1], reverse=reverse)

    def show(self):
        # Do not change this method
        print("Bills")
        for bill in self.bills:
            bill.print()
