# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"


# Child class (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # Call parent constructor
        self.__storage = storage        # Private attribute (encapsulation)
        self.__battery = battery        # Private attribute

    # Encapsulation: Getter & Setter for storage
    def get_storage(self):
        return self.__storage

    def upgrade_storage(self, extra_storage):
        if extra_storage > 0:
            self.__storage += extra_storage
            print(f"Storage upgraded! New storage: {self.__storage} GB")
        else:
            print("Invalid storage upgrade.")

    # Method to use battery
    def use_battery(self, usage):
        if 0 < usage <= self.__battery:
            self.__battery -= usage
            print(f"Used {usage}% battery. Remaining: {self.__battery}%")
        else:
            print("Not enough battery!")

    # Polymorphism example (override parent method)
    def device_info(self):
        return f"{self.brand} {self.model} - {self.__storage}GB, {self.__battery}% battery"


# --- Usage ---
phone1 = Smartphone("Samsung", "Galaxy S25", 256, 100)
phone2 = Smartphone("Apple", "iPhone 16", 512, 85)

print(phone1.device_info())   # Polymorphism in action
print(phone2.device_info())

phone1.upgrade_storage(128)   # Encapsulation (controlled modification)
phone1.use_battery(20)        # Method affecting private data
