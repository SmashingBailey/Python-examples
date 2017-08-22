class Vehicle:

    def __init__(self, make, model, transmission):
        self.make = make
        self.model = model
        self.transmission = transmission

    def vehicle_information(self):
        print '{} \n{} \n{}'.format(self.make, self.model, self.transmission)
        print 10 * '-'
veh_1 = Vehicle('Infiniti', 'G35', 'Manual')
veh_2 = Vehicle('BMW', '330ci', 'Manual')

veh_1.vehicle_information()
veh_2.vehicle_information()

class Location(Vehicle):
    def __init__(self, make, model, transmission, location):
        Vehicle.__init__(self, make, model, transmission)
        self.location = location

veh_3 = Location('Nissan', '350z', 'manual', 'Dallas')

print veh_3.vehicle_information
print veh_3.location
