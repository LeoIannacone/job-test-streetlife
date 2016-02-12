import os
import json

from station import Station

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.normpath(os.path.join(CURRENT_PATH, "..", "tfl"))
STATIONS_FILENAME = os.path.join(BASE_DIR, "stations.json")
CONNECTIONS_FILENAME = os.path.join(BASE_DIR, "connections.json")


class StationFactory():

    @classmethod
    def get_stations(cls):
        stations = {}

        with open(STATIONS_FILENAME, 'rU') as s_fd:
            json_stations = json.load(s_fd)
            for info in json_stations:
                (id, name) = (info[0], info[1])
                stations[id] = Station(id, name)

        with open(CONNECTIONS_FILENAME, 'rU') as c_fd:
            json_connections = json.load(c_fd)
            for info in json_connections:
                (s_id1, s_id2) = (info[0], info[1])
                if s_id1 in stations and s_id2 in stations:
                    (s1, s2) = (stations[s_id1], stations[s_id2])
                    s1.add_connection(s2)
                    s2.add_connection(s1)

        return stations.values()
