from dataclasses import dataclass


@dataclass
class Products:
    stock: str
    product: str
    product_name: str
    category_name: str
    foreign_name: str
    part_name: str
    keyboard_layout_product: str


product_text = Products(
    stock='Акции',
    product='Кресло компьютерное',
    product_name='Кресло компьютерное',
    category_name='Деловые аксессуары',
    foreign_name='Кофе',
    part_name='Шкаф',
    keyboard_layout_product='Green tea'
)
