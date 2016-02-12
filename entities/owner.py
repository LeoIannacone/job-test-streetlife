from player import Player


class Owner(Player):

    def update_stations(self, old_station):
        if old_station is not None:
            old_station.remove_owner(self)
        self.station.add_owner(self)

    def get_available_connections(self):
        connections = super(Owner, self).get_available_connections()
        not_explored = [c for c in connections if c not in self.path]
        # If all available connections have been already visitited
        if len(not_explored) == 0:
            return connections
        return not_explored

    def has_found_cat(self):
        return self.found

    def find(self):
        cats_in_station = self.station.get_cats()
        self.found = False
        for c in cats_in_station:
            if c.is_mine(self.id):
                self.found = True
                break
        if self.found:
            self.station.set_closed(True)
            print("Owner {0} found cat {0} - {1} is now closed"
                  .format(self.id, self.station.name))

        return self.found
