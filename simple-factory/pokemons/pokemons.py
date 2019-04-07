from pydoc import locate


class Pokemon:

    pokemon_class_dir = "pokemons."

    commands = {'a': 'attack', 'd': 'defence', 's': 'special', 'exit': None}

    @classmethod
    def create(cls, pokemon=None):
        try:
            pokemon += '.' + pokemon
            class_ = locate(cls.pokemon_class_dir + pokemon)
            # print(class_)
            # print(dir(class_))
            player_pokemon = class_()
            # print(player_pokemon)
        except TypeError:
            print("You don't have this pokemon")
            from pokemons.Moltres import Moltres
            player_pokemon = Moltres()
        finally:
            pass

        return player_pokemon

    def name(self):
        return self.__class__.__name__

    def attack(self):
        raise NotImplementedError

    def defence(self):
        raise NotImplementedError

    def special(self):
        raise NotImplementedError

    def exit(self):
        raise NotImplementedError
