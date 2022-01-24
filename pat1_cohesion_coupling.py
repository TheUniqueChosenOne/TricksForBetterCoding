"""
1. high cohesion and low coupling
2. group code according data pipeline
"""
import random
from functools import reduce
class VehicleInfo:
    brand: str
    tax_percentage: float
    price: int

    def __init__(self, brand, tax_percentage=0.01, price=10000):
        self.brand = brand
        self.tax_percentage = tax_percentage
        self.price = price
    
    @property
    def tax_per(self):
        return self.tax_percentage
    
    @tax_per.setter
    def tax_per(self, value):
        assert value >=0 and value <=1
        self.tax_percentage = value
    
    def __str__(self, num_space=0):
        space = ' '*num_space
        des_info = f"{space}Vehicle Brand Information:\n"\
        f"{space}brand = {self.brand}\n"\
        f"{space}tax_percentage = {self.tax_percentage}\n"\
        f"{space}price = {self.price}"

        return des_info

class Vehicle:
    ID: str
    lisence: str
    brand_info: VehicleInfo
    def __init__(self, id, lisence, brand_info):
        self.id = id
        self.lisence = lisence
        self.brand_info = brand_info

    def __str__(self):
        dash_line = '-' * 60
        des_info = f"{dash_line}\nVechile Information:\n"\
        f"vehicle ID = {self.id}\n"\
        f"lisence = {self.lisence}\n"\
        f"   |\n   V\n" + self.brand_info.__str__(3) +f'\n{dash_line}'

        des_info = des_info.split('\n')
        des_info = ['|' +line + ' '*(60-len(line))+'|' for line in des_info if len(line) <= 60]
        des_info = '\n'.join(des_info)
        return des_info

class VehicleRegistry:
    vehicle_brands = {}
    LISENCE_LEN = 3
    def __init__(self):
        self.vehicle_brands['Tesla 3'] = VehicleInfo('Tesla 3', tax_percentage=0.2, price=50000)
        self.vehicle_brands['PENCHI 6'] = VehicleInfo('PENCHI 6', tax_percentage=0.3, price=100000)

    def is_brand_valid(self, brand):
        if brand in self.vehicle_brands.keys():
            return True
        else:
            return False

    def register_id(self, brand):
        id = random.sample(range(10), 5)
        id = [str(item) for item in id]
        id = reduce(lambda x,y: x+y, id)
        return id
    
    def register_lisence(self, brand, id):
        lisence = [str(random.choice(range(20))) for _ in range(self.LISENCE_LEN)]
        lisence = '-'.join(lisence)
        return lisence

    def register_vehicle(self, brand):
        assert self.is_brand_valid(brand)

        id = self.register_id(brand)
        lisence = self.register_lisence(brand, id)
        brand_info = self.vehicle_brands[brand]

        return Vehicle(id, lisence, brand_info)


class App:
    def create_vehicle(self, brand):
        vehicle_registry = VehicleRegistry()
        return vehicle_registry.register_vehicle(brand)

app = App()
vehicle = app.create_vehicle('PENCHI 6')
print(vehicle)