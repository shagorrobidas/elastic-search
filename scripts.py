import os
import csv
import random

# Ensure Django settings are configured before importing models
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
import django
django.setup()
from products.models import Product

file_path = 'MOCK_DATA.csv'  # Path to your CSV file


def load_products_from_csv(file_path):
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return
    
    try:
        with open(file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row.get('product_name')
                brand = row.get('brands')
                price = float(row.get('price', 0))
                
                if name and brand:
                    Product.objects.bulk_create([
                        Product(name=name, brand=brand, price=price)
                        for _ in range(random.randint(1, 5))
                    ])
                    print(f"Added product: {name} by {brand} at ${price}")
                else:
                    print(f"Skipping invalid row: {row}")
    except Exception as e:
        print(f"An error occurred while loading products: {e}")
        return
if __name__ == "__main__":
    load_products_from_csv(file_path)
