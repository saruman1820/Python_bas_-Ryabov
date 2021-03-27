"""
Начните работу над проектом «Склад оргтехники».
Создайте класс,описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""


class Stock():
    pass


class Office_equipment:
    def __init__(self,
                 manufacturer: str,
                 model: str,
                 count_sheets_per_minute: float = 0,
                 interface: str = "usb"):
        self.manufacturer = manufacturer
        self.model = model
        self.count_sheets_per_minute = count_sheets_per_minute
        self.interface = interface


class Printer(Office_equipment):
    def __init__(self, price_one_sheet: float, max_count_sheet_per_one_cartridge: int):
        self.price_one_sheet = price_one_sheet
        self.max_count_sheet_per_one_cartridge = max_count_sheet_per_one_cartridge


class Scanner(Office_equipment):
    def __init__(self,  auto_feed: bool = False):
        self.auto_feed = auto_feed


class Mfu(Office_equipment):
    def __init__(self,
                 price_one_sheet: float,
                 max_count_sheet_per_one_cartridge: int,
                 auto_feed: bool = False):
        self.price_one_sheet = price_one_sheet
        self.max_count_sheet_per_one_cartridge = max_count_sheet_per_one_cartridge
        self.auto_feed = auto_feed
