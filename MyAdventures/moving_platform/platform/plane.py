class Plane(object):
    def __init__(self, x=[0, 10], z=[0, 10]):
        self._x = x
        self._z = z

    def x_boundaries(self):
        return self._x

    def z_boundaries(self):
        return self._z

    @property
    def west_edge(self):
        return self._x[0]

    @property
    def east_edge(self):
        return self._x[1]

    @property
    def south_edge(self):
        return self._z[0]

    @property
    def north_edge(self):
        return self._z[1]