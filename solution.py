import pandas as pd

class Matching:
    def __init__(self):
        """
        Construct an empty list of executions and orders 
        """
        self.executions = pd.DataFrame(columns = ['Execution ID', 'Price', 'Quantity', 'Sell-OrderID', 'Buy-OrderID'])
        self.buy_order_book = pd.DataFrame(columns = ["OrderID", "CreateTime", "Price", "Quantity"])
        self.sell_order_book = pd.DataFrame(columns = ["OrderID", "CreateTime", "Price", "Quantity"])
        self.executionID = 0

    def new(self, OrderID, CreateTime, Side, Price, Quantity):
        """
        Add the new order to the orders, and then process it
        """
        new_order = pd.Series(OrderID, CreateTime, Side, Price, Quantity)
        self.processing(new_order)

    def execution(self, Price, Quantity, SOrderID, BOrderID):
        """
        Create an execution for the new order
        """
        self.executions = self.executions.insert(self.executionID, Price, Quantity, SOrderID, BOrderID)
        self.executionID += 1 


    def _processing(self, new_order):
        """
        Private method
        Process the new order 
        """
        if new_order['Side'] == 'Buy':
            # Sort by lowest price if the new order is Buy side
            if self.sell_order_book.empty: # no more orders to cross against
                self.buy_order_book = pd.merge(self.buy_order_book, new_order, how = "outer",sort=True)

            sell_sorted = self.sell_order_book.sort_values(by = ['Price', 'CreateTime'], ascending=[False, True]) # Sort to ensure the order goes into the right place
            priority_order = sell_sorted.loc[0]

            if priority_order["Price"] <= new_order["Price"]:
                # You can only match if the sell price is higher than the buy price    
                if priority_order['Quantity'] < new_order['Quantity']:
                    self.execution(priority_order['Price', 'Quantity', 'OrderID'], new_order['OrderID'])
                else:
                    self.execution(new_order['Price', 'Quantity', 'OrderID'], priority_order['OrderID'])
        else:
            # Sort by lowest price if the new order is Sell side
            if self.buy_order_book.empty: # no more orders to cross against
                self.sell_order_book = pd.merge(self.sell_order_book, new_order, how = "outer",sort=True)
                sell_sorted = self.sell_order_book.sort_values(by = ['Price', 'CreateTime'], ascending=[False, True]) # sort to ensure the order goes into the right place

            buy_sorted = self.buy_order_book.sort_values(by = ['Price', 'CreateTime'], ascending=[True, True])
            priority_order = buy_sorted.loc[0]

            if priority_order['Price'] >= new_order['Price']:
                # You can only match if the sell price is higher than the buy price
                if priority_order['Quantity'] < new_order['Quantity']:
                    self.execution(priority_order['Price', 'Quantity', 'OrderID'], new_order['OrderID'])
                else:
                    self.execution(new_order['Price', 'Quantity', 'OrderID'], priority_order['OrderID'])
                

        return self.executions

        
        
if __name__ == "__main__":
    pd.read_csv("bam-campus-challenge-tech-kingl0ui5/data/buy_orders_standing.csv")