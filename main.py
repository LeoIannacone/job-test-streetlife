import random
from argparse import ArgumentParser

from entities.factories import StationFactory
from entities.players.cat import Cat
from entities.players.owner import Owner

from entities.stats import OwnersStats, ErrorsStats, StationsStats


def main():
    parser = ArgumentParser()
    parser.add_argument('-n', '--number', type=int,
                        help='Number of entities')

    args = parser.parse_args()

    stations = StationFactory.get_stations()
    stations_len = len(stations)

    def get_random_station():
        return stations[random.randint(0, stations_len - 1)]

    owners = []
    cats = []
    for i in xrange(1, args.number + 1):
        owner = Owner(i)
        cat = Cat(i)
        (owner_station, cat_station) = (None, None)
        while owner_station == cat_station:
            owner_station = get_random_station()
            cat_station = get_random_station()

        owner.set_station(owner_station)
        cat.set_station(cat_station)

        owner.start()
        cat.start()

        owners.append(owner)
        cats.append(cat)

    players = owners + cats
    for p in players:
        p.join()

    ownersStats = OwnersStats()
    ownersStats.calc(owners)

    ownersErrorsStats = ErrorsStats()
    ownersErrorsStats.calc(owners)

    catsErrorsStats = ErrorsStats()
    catsErrorsStats.calc(cats)

    stationsStats = StationsStats()
    stationsStats.calc(stations)

    print("\nTotal number of cats: {}".format(args.number))
    print("Number of cats found: {}".format(ownersStats.cats_found))
    print("Average number of movements required " +
          "to find a cat: {}".format(ownersStats.steps_average))

    if ownersErrorsStats.has_errors():
        print("\nThere where problems with owners:")
        if ownersErrorsStats.trapped > 0:
            print(" - {} were trapped in a closed station"
                  .format(ownersErrorsStats.trapped))
        if ownersErrorsStats.no_connection > 0:
            print(" - {} had no more connectios opened"
                  .format(ownersErrorsStats.no_connection))
        if ownersErrorsStats.max_moves > 0:
            print(" - {} reached max number of moves"
                  .format(ownersErrorsStats.max_moves))

    if catsErrorsStats.has_errors():
        print("\nThese poor cats got lost:")
        if catsErrorsStats.trapped > 0:
            print(" - {} were trapped in a closed station"
                  .format(catsErrorsStats.trapped))
        if catsErrorsStats.no_connection > 0:
            print(" - {} had no more connectios opened"
                  .format(catsErrorsStats.no_connection))
        if catsErrorsStats.max_moves > 0:
            print(" - {} reached max number of moves"
                  .format(catsErrorsStats.max_moves))

    print("\nThe most visited station was {}, {} times"
          .format(stationsStats.most_visited.name,
                  stationsStats.most_visited.get_visitited_times()))
    print("The owner {} should be really tired, he visited {} stations"
          .format(ownersStats.most_unlucky.id,
                  ownersStats.most_unlucky.get_number_of_moves()))

if __name__ == '__main__':
    main()
