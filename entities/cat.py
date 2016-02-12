from player import Player


class Cat(Player):

    def update_stations(self, old_station):
        if old_station is not None:
            old_station.remove_cat(self)
        self.station.add_cat(self)

    def is_mine(self, id):
        self.found = id == self.id
        return self.found

    def find(self):
        return self.found
