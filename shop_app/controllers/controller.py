from flask import render_template
from app import app
from models.order_list import orders

@app.route('/orders/')
def index():
    return render_template('index.html', orders=orders)

@app.route('/orders/<index>')
def get(index):
    # index_to_int = 
    order=orders[int(index)]
    return render_template('order.html', order=order, index=index)

# @app.route('/orders/<customer_id>')
# def get(customer_id):
#     for order in orders:
#         if customer_id == order.customer_id:
#             order = order
#             return order
   
#     return render_template('order.html', order=order, customer_id = customer_id)