from car import Car, Weaponized_Car

best_car = Car("buick", "lesabre", 2000)
boom = Weaponized_Car("Abrahams", "M1", 2021, ["75mm Cannon", ".50 Cal MG"])

print(best_car.get_description())
print(boom.get_description())
print(boom.get_loadout())