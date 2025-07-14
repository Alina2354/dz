def count_sales(sales):
    product_revenue = {}
    for product, quantity, price in sales:
        revenue = quantity * price
        if product in product_revenue:
            product_revenue[product] += revenue
        else:
            product_revenue[product] = revenue
    return product_revenue

def count_max_sales(product_revenue):
    best_selling_product = None
    max_revenue = 0
    for product, revenue in product_revenue.items():
        if revenue > max_revenue:
            max_revenue = revenue
            best_selling_product = product
    print(f"Товар с максимальной выручкой: {best_selling_product} (Выручка: {max_revenue})")



if __name__ == '__main__':
    sales = [
        ("Ноутбук", 5, 50000),
        ("Смартфон", 10, 30000),
        ("Наушники", 20, 2000),
        ("Ноутбук", 3, 48000),
        ("Смартфон", 7, 32000),
        ("Наушники", 15, 2500)
    ]
    product_revenue = count_sales(sales)
    print(product_revenue)
    print(count_max_sales(product_revenue))
