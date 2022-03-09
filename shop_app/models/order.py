class Order():

    def __init__(self, customer_name, order_date, quantity, book_title, book_price):
            self.customer_name = customer_name
            self.order_date = order_date
            self.quantity = quantity
            self.book_title = book_title
            self.book_price = book_price
            self.total_price = book_price * quantity