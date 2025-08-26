# Base class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery  # percentage

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"Battery charged. Current level: {self.battery}%")

    def info(self):
        print(f"{self.brand} {self.model} | Storage: {self.storage}GB | Battery: {self.battery}%")

# Child class (Inheritance)
class SmartphonePro(Smartphone):
    def __init__(self, brand, model, storage, battery, camera_quality):
        super().__init__(brand, model, storage, battery)  # inherit attributes
        self.camera_quality = camera_quality

    # Polymorphism: overriding info()
    def info(self):
        print(f"{self.brand} {self.model} | Storage: {self.storage}GB | "
              f"Battery: {self.battery}% | Camera: {self.camera_quality}MP")

    def take_photo(self):
        print(f"{self.brand} {self.model} takes a photo with {self.camera_quality}MP quality 📸")

# Testing
phone1 = Smartphone("Samsung", "A52", 128, 75)
phone1.info()
phone1.call("+123-456-789")
phone1.charge(20)

pro_phone = SmartphonePro("Apple", "iPhone 15 Pro", 256, 50, 48)
pro_phone.info()
pro_phone.take_photo()
