class Currency:
    def __init__(self, code, exchange_to_usd):
        self.amount = 0.00
        self.code = code
        self.exchange_to_usd = exchange_to_usd

    def set_amount(self, amount):
        self.amount = amount

    def in_currency(self, amount):
        return amount/ self.exchange_to_usd

    def to_usd(self, amount=None):
        #to_convert = amount if amount is not None else self.amount
        to_convert = amount or self.amount
        return to_convert * self.exchange_to_usd

    def __eq__(self, other):
        # Exactly equal, ==
        return self.to_usd() == other.to_usd()

    def __gt__(self,other):
        # Greater than, >
        return self.to_usd() > other.to_usd()

    def __lt__(self,other):
        # Less than, <
        pass

    def __le__(self, other):
        # Less than or equal to, <=
        pass

    def __ge__(self,other):
        # Greater than or equal to, >=
        pass

#1
#print(pounds.in_currency(1000))
#print(pounds.to_usd(1000))

#2
#pounds = Currency("GBP", 1.21)
#euros = Currency("EUR", 1.07)
#print(pounds.to_usd(1000) > euros.to_usd(1000))

#3
'''
pounds = Currency("GBP", 1.21)
pounds.set_amount(1000)
euros = Currency("EUR", 1.07)
euros.set_amount(1000)
print(pounds.to_usd() > euros.to_usd())
'''

#4
pounds = Currency("GBP", 1.21)
pounds.set_amount(1000)
euros = Currency("EUR", 1.07)
euros.set_amount(1000)
print(pounds == euros )