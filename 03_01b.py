"""


"""
from collections import namedtuple


def can_take_order(driver, num_packages):
    return driver.car_capacity >= num_packages


def main():
    # add code here
    # create a driver with a name, car type, and car capacity
    Driver = namedtuple("driver", ["name", "car_type", "car_capacity"])

    # an example you can use to practice: "Iris", "Toyota Prius", 7
    driver_one = Driver("Iris", "Toyota Prius", 7)
    driver_two = Driver("Mickie", "Hyundai Tucson", 15)
    driver_three = Driver("Witty", "Hummer", 26)
    # check if they can take a certain order, given their car's capacity.
    print(driver_one)
    print(can_take_order(driver_three, 20))
    return


if __name__ == "__main__":
    main()
