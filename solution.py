import pandas as pd

class Matching:
    def __init__(self):
        """
        Construct an empty list of executions and orders 
        """
        self.execution = pd.DataFrame(columns = ['Execution ID', 'Price', 'Quantity', 'Sell-OrderID', 'Buy-OrderID'])
        self.order_book = pd.DataFrame(columns = ["OrderID", "CreateTime", "Side", "Price", "Quantity"])

    def new(self, OrderID, CreateTime, Side, Price, Quantity):
        """
        Add the new order to the orders, and then process it
        """
        new_order = pd.Series(OrderID, CreateTime, Side, Price, Quantity)
        self.processing(new_order)

    def execution(self):
        return 


    def _processing(self, new_order):
        """
        Private method
        Process the new order 
        """
        if new_order['Side'] == 'Buy':
            # scan for sell orders if the new order side is Buy
            highest_price = self.order_book.loc[self.order_book['Price'].idxmax()]
            if highest_price.shape[0] != 0: 
                # if multiple orders have the same price, the one with an earlier time is prioritised
                highest_price = highest_price.loc[highest_price['CreateTime'].idxmin()] 
        else:
            # Scan for buy orders if the new order side is Sell
            lowest_price = self.order_book.loc[self.order_book['Price'].idxmin()]
            if lowest_price.shape[0] != 0: 
                # if multiple orders have the same price, the one with an earlier time is prioritised
                lowest_price = lowest_price.loc[lowest_price['CreateTime'].idxmin()] 

        self.order_book.insert(new_order)
        
        