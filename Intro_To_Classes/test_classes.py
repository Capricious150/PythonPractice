from car import Car

# Hopping over here from another chapter to have some ready-made classes I can test.
def test_car():
    trial_car = Car("Honda", "Sonata", "2002")
    assert trial_car.get_description() == "2002 Honda Sonata with 0 miles"
    trial_car.incremement_odometer(10)
    assert trial_car.get_description() == "2002 Honda Sonata with 10 miles"

def test_another_car():
    trial_car = Car("Ford", "Highlander", "1989")
    assert trial_car.get_description() == "1989 Ford Highlander with 0 miles"
    trial_car.incremement_odometer(10)
    assert trial_car.get_description() == "1989 Ford Highlander with 10 miles"