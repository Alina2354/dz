def unique_products(products):
    seen_skus = set()
    unique_products_list = []

    for product in products:
        sku = product['sku']
        if sku not in seen_skus:
            unique_products_list.append(product)
            seen_skus.add(sku)

    return unique_products_list
