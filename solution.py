import pandas as pd

class Order:
    def __init__(self):
        self.Execution = pd.DataFrame(columns = ['Execution ID', 'Price', 'Quantity', 'Sell-OrderID', 'Buy-OrderID'])
        self.Orders = pd.DataFrame(columns = ["OrderID", "CreateTime", "Side", "Price", "Quantity"])

    def new(self, OrderID, CreateTime, Side, Price, Quantity):
        self.Orders.insert(OrderID, CreateTime, Side, Price, Quantity)
        self.processing()

    def execution(self):
        return 


    def _processing():
        if 