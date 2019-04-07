# this script use simple factory pattern to control multiple method
#

import sys
from optparse import OptionParser

from pokemons.pokemons import Pokemon


def main(options, args=None):
    try:
        # initial trainer's pokemon
        if options.player_pokemon:
            print("You choose: %s" % options.player_pokemon)
            player_pokemon = Pokemon.create(options.player_pokemon)
        else:
            print("You must need choose a Pokemon")
            return 2

        while True:
            print("You summer pokemon: %s" % player_pokemon.name())
            print("input your command: %s" % list(player_pokemon.commands.keys()))
            command = input()
            if not command or command == "exit":
                break
            elif command in player_pokemon.commands:
                # do action
                command_name = player_pokemon.commands[command]
                print("%s use skill %s" % (player_pokemon.name(), getattr(player_pokemon, command_name, "defence")()))
            else:
                print("I Can't Understand your command")

    except KeyboardInterrupt:
        print("keyboard interrupt: stop battle")


if __name__ == "__main__":
    optParser = OptionParser(usage="""
            on this game, you can choose a Pokemon to start this your battle  
            
            """)

    optParser.add_option("-p",
                         "--player-pokemon",
                         default=None,
                         dest="player_pokemon",
                         help="choose an pokemon for your trainer")

    optParser.add_option("-n",
                         "--player-name",
                         default=None,
                         dest="player_name",
                         help="trainer name")

    (options, args) = optParser.parse_args()

    sys.exit(main(options, args))
