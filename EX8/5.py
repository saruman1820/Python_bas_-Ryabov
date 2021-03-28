"""
Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.
"""


def move(old_department, new_department, equipment):
    old_department.rem(equipment)
    new_department.add(equipment)


class Not_Space(Exception):
    pass


class Department():
    def __init__(self,
                 max_count: int,
                 department_name: str):
        self.max_count = max_count
        self.department_name = department_name
        self.storage = []

    def add(self, equipment):
        if not isinstance(equipment, Office_equipment):
            print(f"Вы пытаетесь добавить на склад не оргтехнику")
        else:
            self.storage.append(equipment)
            print(f"в депортамент {self.department_name} добавлено {equipment.manufacturer, equipment.model} "
                  f"ещё свободно {self.max_count - len(self.storage)} ")

    def rem(self, equipment):
        if not isinstance(equipment, Office_equipment):
            print(f"Вы пытаетесь удалить то чего нет на складt")
        else:
            self.storage.remove(equipment)
            print(f"в депортамент {self.department_name} добавлено {equipment.manufacturer, equipment.model} "
                  f"ещё свободно {self.max_count - len(self.storage)} ")

    def __str__(self):
        return self.storage.__str__()


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
        print(f"Устройство {self.manufacturer} {self.model} проинвенторизировано ")


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


printer1 = Printer(manufacturer="Xerox", model="202", count_sheets_per_minute=30, interface="ethernet",
                   price_one_sheet=0.5, max_count_sheet_per_one_cartridge=1000)

printer2 = Printer(manufacturer="Xerox", model="202", count_sheets_per_minute=30, interface="ethernet",
                   price_one_sheet=0.5, max_count_sheet_per_one_cartridge=1000)

printer3 = Printer(manufacturer="Xerox", model="202", count_sheets_per_minute=30, interface="ethernet",
                   price_one_sheet=0.5, max_count_sheet_per_one_cartridge=1000)

scanner1 = Scanner(manufacturer="hp", model="330", count_sheets_per_minute=60, interface="usb",
                   auto_feed=True)
scanner2 = Scanner(manufacturer="hp", model="330", count_sheets_per_minute=60, interface="usb",
                   auto_feed=False)
scanner3 = Scanner(manufacturer="hp", model="330", count_sheets_per_minute=60, interface="ethernet",
                   auto_feed=True)

mfu1 = Mfu(manufacturer="kyocera", model="350030", count_sheets_per_minute=60, interface="ethernet",
           price_one_sheet=0.5, max_count_sheet_per_one_cartridge=1000, auto_feed=True)

mfu2 = Mfu(manufacturer="kyocera", model="330asd", count_sheets_per_minute=60, interface="ethernet",
           price_one_sheet=0.5, max_count_sheet_per_one_cartridge=1000, auto_feed=False)

mfu3 = Mfu(manufacturer="kyocera", model="asdasd330", count_sheets_per_minute=60, interface="ethernet",
           price_one_sheet=0.5, max_count_sheet_per_one_cartridge=50000, auto_feed=True)

stock = Department(max_count=5, department_name="Stock")
recep = Department(max_count=2, department_name="Reception")
stock.add(printer1)
stock.add(printer2)
stock.add(printer3)
print(stock)
print(recep)
move(stock, recep, printer2)

print(stock)
print(recep)
