
def display_orders(orders):
    for order in orders:
        # Unpacking the tuple
        customer_name, product, quantity = order
        
        # Formatting and printing the order details
        print(f"Customer: {customer_name} | Product: {product} | Quantity: {quantity}")

# Sample order data
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Charlie", "Smartphone", 3),
    ("Diana", "Headphones", 4)
]

# Call the function to display orders
display_orders(orders)
