"""
``Coordinate``: a simple class with a custom ``__str__``::

    >>> moscow = Coordinate(55.756, 37.617)
    >>> print(moscow)
    <coordinates.Coordinate object at 0x...>
    >>> location = Coordinate(55.756, 37.617)
    >>> print(moscow == location)
    False
"""

# tag::COORDINATE[]
class Coordinate:

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

# end::COORDINATE[]