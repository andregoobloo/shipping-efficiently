import csv
import datetime

from Truck import Truck


class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, note, status):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.note = note
        self.status = status
        self.shipped_time = None
        self.delivery_time = None

    def __str__(self):
        return "ID: %s, %s, %s, %s, %s, %s, Deadline: %s, Status: %s, Delivered at: %s" % (
            self.package_id, self.address, self.city, self.state,
            self.zip_code, self.weight, self.deadline,
            self.status, self.delivery_time,)

    # Updating package status' for when a user inputs a specific time in the UI
    def packages_at_specific_time(self, input_time):
        if input_time >= self.delivery_time:
            self.status = "Delivered"
        elif self.delivery_time > input_time > self.shipped_time:
            self.status = "En Route"
        else:
            self.status = "At Hub"
        # Updating package 9's address at 10:20am
        if self.package_id == 9:
            if input_time >= datetime.timedelta(hours=10, minutes=20):
                self.address = "410 S State St"
                self.zip_code = "84111"
            else:
                self.address = "300 State St"
                self.zip_code = "84103"


# Loading package data from csv file to a hash table
def load_package_data(file, package_table):
    with open(file) as packages:
        package_data = csv.reader(packages, delimiter=',')
        # next(package_data)
        for package in package_data:
            p_id = int(package[0])
            p_address = package[1]
            p_city = package[2]
            p_state = package[3]
            p_zip_code = package[4]
            p_deadline = package[5]
            p_weight = package[6]
            p_note = package[7]
            p_status = "At Hub"

            p = Package(p_id, p_address, p_city, p_state, p_zip_code, p_deadline, p_weight, p_note, p_status)

            package_table.insert(p_id, p)


def convert_time(input_time):
    (h, m, s) = input_time.split(":")
    hour = int(h)
    minute = int(m)
    second = int(s)
    return datetime.timedelta(hours=hour, minutes=minute, seconds=second)
