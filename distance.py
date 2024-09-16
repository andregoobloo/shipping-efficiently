import csv

# Reading the distance file
with open("distance.csv") as file1:
    distances = csv.reader(file1)
    distance_list = list(distances)

# Reading the address file
with open("address.csv") as file2:
    addresses = csv.reader(file2)
    address_list = list(addresses)


# Method for finding distance between two addresses
def distance_between(x, y):
    distance = distance_list[x][y]
    if distance == '':
        distance = distance_list[y][x]

    return float(distance)


# Method to get address number from address string
def extract_address(address):
    for row in address_list:
        if address in row[2]:
            return int(row[0])
