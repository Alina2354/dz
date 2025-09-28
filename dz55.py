def filter_orders_by_status(orders, status):
    filtered_orders = [order for order in orders if order['status'] == status]
    return filtered_orders
