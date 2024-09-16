from CreateHashTable import CreateHashTable
from Package import load_package_data


package_table = CreateHashTable()

load_package_data("packages.csv", package_table)

# Finding which packages need to be delivered early

priority = []

print("Priority Packages: \n")

for i in range(len(package_table.list)):
    early = package_table.search(i + 1)
    # Packages 6 and 25 are delayed, so they will be ignored
    if early.deadline != "EOD" and early.package_id != 6 and early.package_id != 25:
        print(early.package_id)
        priority.append(early)

print("\n------")
print("------ \n")

# Finding packages that share the same address to make delivery more efficient

print("Packages being shipped to the same address: \n")

for i in range(1, len(package_table.list)):
    same = package_table.search(i)
    for j in range(i+1, len(package_table.list)):
        comparison = package_table.search(j)
        if same.address == comparison.address and same.package_id != comparison.package_id:
            print(same.package_id, "&", comparison.package_id)


# Same Addresses : (2,33)(5,37,38)(7,29)(8,30)(13,39)(15,16,34)(20,21)(25,26)(27,35)(31,32)

print("\n------")
print("------ \n")

# Finding packages that have notes to better optimize delivery instructions

print("Packages with special instructions: \n")

for i in range(len(package_table.list)):
    has_note = package_table.search(i + 1)
    if has_note.note != "None":
        print("Package", has_note.package_id, has_note.note)

# Optimizing delivery based on results

# truck1 = [1, 7, 8, 13, 14, 15, 16, 19, 20, 21, 29, 30, 34, 40]
#
# truck2 = [2, 3, 5, 18, 27, 33, 35, 36, 37, 38, 39]
#
# truck3_delayed_905 = [6, 25, 26, 28, 31, 32]
#
# last_delivery_delayed_1020 = [9]
# # Same address sets (2,33) (27,35) (5,37,38) (13,39) (15,16,34)
# #                   (25,26) *(31,32)* (7,29) (8,30) (20,21)
#
# # 8 unassigned packages remain: 4, 10, 11, 12, 17, 22, 23, 24