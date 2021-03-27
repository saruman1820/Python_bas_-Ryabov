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
    def __init__(self, price_one_sheet: float, max_count_sheet_per_one_cartridge: int, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.price_one_sheet = price_one_sheet
        self.max_count_sheet_per_one_cartridge = max_count_sheet_per_one_cartridge


class Scanner(Office_equipment):
    def __init__(self, auto_feed: bool = False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.auto_feed = auto_feed


class Mfu(Office_equipment):
    def __init__(self,
                 price_one_sheet: float,
                 max_count_sheet_per_one_cartridge: int,
                 auto_feed: bool = False,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)

        self.price_one_sheet = price_one_sheet
        self.max_count_sheet_per_one_cartridge = max_count_sheet_per_one_cartridge
        self.auto_feed = auto_feed


Printer1 = Printer(manufacturer="Xerox", model="202", count_sheets_per_minute=30, interface="ethernet",
                   price_one_sheet=0.5, max_count_sheet_per_one_cartridge=1000)

Printer2 = Printer(manufacturer="Xerox", model="202", count_sheets_per_minute=30, interface="ethernet",
                   price_one_sheet=0.5, max_count_sheet_per_one_cartridge=1000)

Printer3 = Printer(manufacturer="Xerox", model="202", count_sheets_per_minute=30, interface="ethernet",
                   price_one_sheet=0.5, max_count_sheet_per_one_cartridge=1000)

scanner1 = Scanner(manufacturer="hp", model="330", count_sheets_per_minute=60, interface="usb",
                   auto_feed=True)
scanner2 = Scanner(manufacturer="hp", model="330", count_sheets_per_minute=60, interface="usb",
                   auto_feed=False)
scanner3 = Scanner(manufacturer="hp", model="330", count_sheets_per_minute=60, interface="ethernet",
                   auto_feed=True)

mfu1 = Mfu(manufacturer="hp", model="330", count_sheets_per_minute=60, interface="ethernet",
           price_one_sheet=0.5, max_count_sheet_per_one_cartridge=1000, auto_feed= True)

mfu2 = Mfu(manufacturer="hp", model="330", count_sheets_per_minute=60, interface="ethernet",
           price_one_sheet=0.5, max_count_sheet_per_one_cartridge=1000, auto_feed= False)

mfu3 = Mfu(manufacturer="hp", model="330", count_sheets_per_minute=60, interface="ethernet",
           price_one_sheet=0.5, max_count_sheet_per_one_cartridge=50000, auto_feed= True)




