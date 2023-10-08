
class AX18(object):
    def __init__(self, id, name, port, baudrate):
        self.id = id
        self.name = name
        self.port = port
        self.baudrate = baudrate

    def __str__(self):
        return "AX18: %s" % self.name

    def __repr__(self):
        return "AX18: %s" % self.name

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.id)

    # implement properties
    def _get_speed(self):
        return 0

    def _set_speed(self, speed):
        pass

    def _get_current_speed(self):
        return 0

    speed = property(_get_speed, _set_speed)
    current_speed = property(_get_current_speed)





