from entities.exceptions import InvariantException
from entities.exceptions import NoAvailabeConnectionException
from entities.exceptions import CannotMoveFromClosedStationException


class ErrorsStats():

    def __init__(self):
        self.trapped = 0
        self.max_moves = 0
        self.no_connection = 0

    def calc(self, players):
        for p in players:
            if not p.has_error():
                continue

            e = p.get_error()
            if isinstance(e, InvariantException):
                self.max_moves += 1
            elif isinstance(e, NoAvailabeConnectionException):
                self.no_connection += 1
            elif isinstance(e, CannotMoveFromClosedStationException):
                self.trapped += 1

    def has_errors(self):
        return self.trapped > 0 or self.max_moves > 0 or self.no_connection > 0


class OwnersStats():

    def __init__(self):
        self.cats_found = 0
        self.total_steps = 0
        self.steps_average = -1
        self.most_unlucky = None

    def calc(self, owners):
        for o in owners:
            if o.has_error():
                continue

            if o.has_found_cat():
                self.cats_found += 1
                self.total_steps += o.get_number_of_moves()

                if self.most_unlucky is not None:
                    m_u_m = self.most_unlucky.get_number_of_moves()
                    if o.get_number_of_moves() > m_u_m:
                        self.most_unlucky = o
                else:
                    self.most_unlucky = o

        if self.cats_found > 0:
            self.steps_average = self.total_steps / self.cats_found


class StationsStats():

    def __init__(self):
        self.most_visited = None

    def calc(self, stations):
        self.most_visited = stations[0]
        for s in stations[1:]:
            m_v_t = self.most_visited.get_visitited_times()
            if s.get_visitited_times() > m_v_t:
                self.most_visited = s
