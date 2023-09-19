from dataclasses import dataclass, field

from .product import Product


@dataclass
class OrderItem:
    product: Product = field(default_factory=Product)
    quantity: int = 0

    def __post_init__(self):
        self.taxed_amount = round(self.product.taxed_amount * self.quantity, 2)
        self.tax = self.product.tax * self.quantity
