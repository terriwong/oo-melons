"""This file should have our order classes in it."""

from random import randint
import datetime

class AbstractMelonOrder(object):
    """This is melon order for all classes."""
    def __init__(self, species, qty):

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = None
        self.tax = None

    def get_base_price(self):

        base_price = randint(5,9)    
        
        # now = datetime.datetime.now()
        if 1 <= datetime.datetime.today().weekday() >= 5 and 8 <= datetime.datetime.now().hour >= 11:
            base_price =+ 4



    def get_total(self):
        """Gets the price for ALL melons!"""

        base_price = self.get_base_price()

        if self.species == "Christmas":
            base_price=1.5*base_price
        
        total = (1 + self.tax) * self.qty * base_price

        if self.order_type=="international" and self.qty<10:
            total+=3

        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True   

class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""
       
    order_type = "domestic"
    tax = 0.08

class GovernmentMelonOrder(AbstractMelonOrder):

    tax=0
    passed_inspection=False

    def inspect_melons(self,passed):
        """takes in a boolean input and updates passed_inspection."""
        if passed:
            self.passed_inspection = True
            # return True

   
class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):

        super(InternationalMelonOrder, self).__init__(species, qty)

        self.country_code = country_code

    order_type = "international"
    tax = 0.17    

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
