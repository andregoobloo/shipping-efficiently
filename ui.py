from Package import convert_time
from Truck import Truck


# Creating the UI, asks user if they would like to view data for a specific package or all the packages
def ui(package_table):
    ui_interface = True
    while ui_interface:

        start = input("\nReady to track packages? y/n ").lower()
        if start == "y":
            time = input("Please enter a time in the following format: HH:MM:SS ")
            converted_time = convert_time(time)

            all_or_one = input(
                "Please enter 'all' to view all packages, 'one' to view a single package, or enter something else to quit: ").lower()

            if all_or_one == "all":
                print("\n")
                for i in range(len(package_table.list)):
                    package = package_table.search(i + 1)
                    package.packages_at_specific_time(converted_time)
                    print(str(package))
            elif all_or_one == "one":
                package_id = int(input("Enter the id for the package you would like to track: "))
                # search hash table for the package object
                single_package = package_table.search(package_id)
                # print details to the screen
                single_package.packages_at_specific_time(converted_time)
                print("\n")
                print(str(single_package))
            else:
                ui_interface = False

        else:
            ui_interface = False