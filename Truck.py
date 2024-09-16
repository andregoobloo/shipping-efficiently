class Truck:
    MAX_CAPACITY = 16
    SPEED = 18

    def __init__(self, delivery_list, departure_time, capacity=MAX_CAPACITY, speed=SPEED):
        self.capacity = capacity
        self.speed = speed
        self.miles = 0.0
        self.delivery_list = delivery_list
        self.current_location = "4001 South 700 East"
        self.departure_time = departure_time
        self.time = departure_time

    def __str__(self):
        return "%s, %s, %s, %s, %s" % (self.delivery_list, self.current_location, self.departure_time,
                                       self.time, self.miles)


