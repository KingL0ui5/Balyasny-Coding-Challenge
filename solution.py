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
            # Sort by lowest price if the new order is Buy side
            buy_sorted = self.order_book.sort_values(by = ['Price', 'CreateTime'], ascending=[False, True])
        
        else:
            # Sort by lowest price if the new order is Sell side
            sell_sorted = self.order_book.sort_values(by = ['Price', 'CreateTime'], ascending=[True, True])

        self.order_book.insert(new_order)
        
        