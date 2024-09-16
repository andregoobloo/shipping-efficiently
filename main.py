# Andre Holzthum
# WGU
# Student ID: 012044675

import datetime

from CreateHashTable import CreateHashTable
from Package import load_package_data, convert_time
from Truck import Truck
from distance import distance_between, extract_address
from ui import ui

package_table = CreateHashTable()
load_package_data("packages.csv", package_table)

# Delivery Lists
truck1_list = [1, 7, 8, 13, 14, 15, 16, 19, 20, 21, 29, 30, 34, 39, 40]
truck2_list = [2, 3, 5, 6, 18, 25, 26, 27, 28, 31, 32, 33, 35, 36, 37, 38]
truck3_list = [4, 9, 10, 11, 12, 17, 22, 23, 24]


# Creating truck objects
truck1 = Truck(truck1_list, datetime.timedelta(hours=8))
truck2 = Truck(truck2_list, datetime.timedelta(hours=9, minutes=5))
truck3 = Truck(truck3_list, datetime.timedelta(hours=10, minutes=20))


# Method for delivering packages
def delivery(truck):
    # Place all packages into a new list
    to_be_delivered = []
    for i in truck.delivery_list:
        package = package_table.search(i)
        to_be_delivered.append(package)

    # Clear the old the list
    truck.delivery_list.clear()

    # Iterates through to_be_delivered list until all packages on the truck has been delivered
    while len(to_be_delivered) > 0:

        next_address_distance = 500
        next_package = None

        # Calculating the closest next address
        for package in to_be_delivered:
            distance = distance_between(extract_address(truck.current_location), extract_address(package.address))
            if distance <= next_address_distance:
                next_address_distance = distance
                next_package = package

        # Adds closest next package to the trucks delivery list
        truck.delivery_list.append(next_package.package_id)
        # Removes that package from the to_be_delivered list
        to_be_delivered.remove(next_package)
        # Adds mileage to next address to trucks miles count
        truck.miles += next_address_distance
        # Updates trucks current location
        truck.current_location = next_package.address
        # Updates the time
        truck.time += datetime.timedelta(hours=next_address_distance / truck.speed)
        next_package.delivery_time = truck.time
        next_package.shipped_time = truck.departure_time


# Packages being delivered by each truck, optimizing the shortest next distance
delivery(truck1)
delivery(truck2)
delivery(truck3)

# Updating package 9's address and zip code at 10:20am


# Printing total miles of all trucks and a welcome message
total_miles = round(truck1.miles + truck2.miles + truck3.miles, 2)
print("Welcome to the Western Governors University Parcel Service!")
print("Truck 1 miles =", round(truck1.miles, 2))
print("Truck 1 is delivering the following packages(ID): ", truck1.delivery_list)
print("Truck 2 miles =", round(truck2.miles, 2))
print("Truck 2 is delivering the following packages(ID): ", truck2.delivery_list)
print("Truck 3 miles =", round(truck3.miles, 2))
print("Truck 3 is delivering the following packages(ID): ", truck3.delivery_list)
print("Total Miles = ", total_miles)

# Running the UI
ui(package_table)