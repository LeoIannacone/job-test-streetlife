import time
import random
from threading import Thread

from ..exceptions import InvariantException
from ..exceptions import NoAvailabeConnectionException
from ..exceptions import CannotMoveFromClosedStationException

MAX_MOVES = 100000
SLEEP_TIME = 0.01  # s


class Player(Thread):

    def __init__(self, id, type="Player",
                 sleep_time=SLEEP_TIME,
                 max_moves=MAX_MOVES):
        super(Player, self).__init__()
        self.id = id
        self.sleep_time = sleep_time
        self.number_of_moves = 0
        self.found = False
        self.path = []
        self.station = None
        self.error = None
        self.max_moves = max_moves

    def _invariant(self):
        return self.number_of_moves < self.max_moves

    def _update_invariant(self):
        if not self._invariant():
            raise InvariantException("Max number of moves reached")
        self.number_of_moves += 1

    def get_number_of_moves(self):
        return self.number_of_moves

    def set_station(self, station):
        self._update_invariant()
        old_station = self.station
        self.path.append(old_station)
        self.station = station
        self.update_stations(old_station)

    def get_available_connections(self):
        """
        Returns the stations connected where the player can go
        """
        result = [s for s in self.station.get_connections()
                  if not s.is_closed()]
        if len(result) == 0:
            raise NoAvailabeConnectionException(
                "All connected stations are closed")
        return result

    def move(self):
        if self.station.is_closed():
            raise CannotMoveFromClosedStationException(
                "Cannot move - station is closed")

        connections = self.get_available_connections()
        next_station = connections[random.randint(0, len(connections) - 1)]
        self.set_station(next_station)

    def run(self):
        while not self.find():
            try:
                self.move()
                time.sleep(self.sleep_time)
            except Exception as e:
                self.error = e
                break

    def has_error(self):
        return self.error is not None

    def get_error(self):
        return self.error

    def find(self):
        pass

    def update_stations(self, old_station):
        pass
