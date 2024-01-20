class Car:

    def __init__(self, make, model, year) -> None:
        self.make = make.title()
        self.model = model.title()
        self.year = year
        self.odometer = 0

    def get_description(self) -> str:
        return f"{self.year} {self.make} {self.model} with {self.odometer} miles"

    def set_odometer(self, miles) -> None:
        self.odometer = miles

    def incremement_odometer(self, miles) -> None:
        self.odometer += miles

class Weaponized_Car(Car):
    def __init__(self, make, model, year, weapons):
        super().__init__(make, model, year)
        self.weapons = weapons
        self.armor_state = "pristine"

    def get_loadout(self) -> str:
        weapon_list = ""

        for weapon in self.weapons:
            weapon_list += f"{weapon}, "
        return f"Armed with {weapon_list}and with {self.armor_state} armor condition"