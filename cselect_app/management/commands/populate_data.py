# yourapp/management/commands/populate_data.py
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from cselect_app.models import Product

class Command(BaseCommand):
    help = 'Populate Product model with sample data and images'

    def handle(self, *args, **options):
        # Sample data for CartItem (computer-related products)
        cart_items_data = [
            ('COM-001', 'Laptop', 'High-performance laptop with SSD', 'Computers'),
            ('COM-002', 'Desktop PC', 'Powerful desktop computer for gaming', 'Computers'),
            ('COM-003', 'External Hard Drive', '1TB External Hard Drive', 'Computer Accessories'),
            ('COM-004', 'Wireless Mouse', 'Ergonomic wireless mouse', 'Computer Accessories'),
            ('COM-005', 'Monitor', '24-inch LED monitor', 'Computer Accessories'),
            ('COM-006', 'Gaming Keyboard', 'Mechanical gaming keyboard with RGB lighting', 'Computer Accessories'),
            ('COM-007', 'Webcam', 'HD webcam for video conferencing', 'Computer Accessories'),
            ('COM-008', 'Printer', 'All-in-one printer with wireless connectivity', 'Printers'),
            ('COM-009', 'Wi-Fi Router', 'Dual-band Wi-Fi router', 'Networking'),
            ('COM-010', 'External SSD', '500GB External Solid State Drive', 'Computer Accessories'),
        ]

        # Populate CartItem model with images
        for data in cart_items_data:
            product_code, product_name, description, category = data

            # Create a CartItem instance
            cart_item = Product.objects.create(
                product_code=product_code,
                product_name=product_name,
                description=description,
                category=category,
                price=0.0,
                quantity=30
            )

            image_filename = f"{product_code}.png"
            image_path = os.path.join(settings.BASE_DIR, 'cselect_app', 'static', 'img', image_filename)
            
            if os.path.exists(image_path):
                cart_item.attachments.name = f"attachments/{image_filename}"
                cart_item.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated CartItem model with images'))
