"""
>>> basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
>>> bus = TwilightBus(basketball_team)
>>> bus1 = TwilightBus(copy.deepcopy(basketball_team))
>>> bus1.drop('Sue')
>>> bus1.drop('Maya')
>>> basketball_team
['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
>>> bus.drop('Tina')
>>> bus.drop('Pat')
>>> basketball_team
['Sue', 'Maya', 'Diana']
"""

# tag::TWILIGHT_BUS_CLASS[]
import copy
class TwilightBus:
    """A bus model that makes passengers vanish"""

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []  # <1>
        else:
            self.passengers = passengers  #<2>

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)  # <3>
# end::TWILIGHT_BUS_CLASS[]

