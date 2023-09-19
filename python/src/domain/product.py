from dataclasses import dataclass, field

from .category import Category


@dataclass
class Product:
    name: str = ""
    price: float = 0
    category: Category = field(default_factory=Category)

    def __post_init__(self):
        self.tax = round(self.price / 100 * self.category.tax_percentage, 2)
        self.taxed_amount = round((self.price + self.tax), 2)
