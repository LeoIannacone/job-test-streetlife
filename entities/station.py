class Station():

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.connections = []
        self.owners = []
        self.cats = []
        self.closed = False
        self.visited_times = 0

    def add_connection(self, station):
        if station not in self.connections:
            self.connections.append(station)

    def get_connections(self):
        return self.connections

    def remove_owner(self, owner):
        if owner in self.owners:
            self.owners.remove(owner)

    def add_owner(self, owner):
        if owner not in self.owners:
            self.owners.append(owner)
            self._increase_visited()

    def remove_cat(self, cat):
        if cat in self.cats:
            self.cats.remove(cat)

    def add_cat(self, cat):
        if cat not in self.cats:
            self.cats.append(cat)
            self._increase_visited()

    def get_cats(self):
        return self.cats

    def set_closed(self, closed):
        self.closed = closed

    def is_closed(self):
        return self.closed

    def _increase_visited(self):
        self.visited_times += 1

    def get_visitited_times(self):
        return self.visited_times
