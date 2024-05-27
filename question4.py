# QUestion 4 Task 1

def print_orders(orders):
    for order in orders:
        customer_name, product, quantity = order
        print(f"Customer: {customer_name}, Product: {product}, Quantity: {quantity}")

# Sample Order Data
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Charlie", "Smartphone", 3),
    ("Diana", "Headphones", 4)
]

# Example usage
print_orders(orders)
