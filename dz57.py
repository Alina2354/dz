def get_max_price(products):
  if not products:
    return None

  max_price = float('-inf')

  for product in products:
    price = product.get('price')
    if price is not None and price > max_price: 
        max_price = price

  return max_price if max_price != float('-inf') else None