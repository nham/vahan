class Vehicle1a:
    def __init__(self, pos, mass):
        self.pos = pos
        self.mass = mass
        self.force = 0

    def sense_yummies(self):
        # this implies that no matter the mass of the vehicle, they all have the
        # same engine, i.e. a vehicle that weights more does not have a more
        # powerful engine
        self.force = yummies(self.pos)

    def move_step(self, step):
        # aristotelian physics! think driving a car. the foot stays on the gas
        # pedal in order to maintain speed
        self.sense_yummies()
        vel = self.force / self.mass
        self.pos += step * vel

a = Vehicle1a(0.1, 5);
b = Vehicle1a(0.1, 10);
c = Vehicle1a(-0.5, 5);
d = Vehicle1a(0.1, 1);

def yummies(x):
    return 1/6 * -x * (x - 4) * (x + 4) + 1


steps = 20
dt = 0.02

def simulate_vehicle(veh, steps, dt):
    print(veh.pos)
    for i in range(0, steps):
        veh.move_step(dt)
        print(veh.pos)

simulate_vehicle(a, steps, dt)
print("--------------")
simulate_vehicle(b, steps, dt)
print("--------------")
simulate_vehicle(c, steps, dt)
print("--------------")
simulate_vehicle(d, steps, dt)
