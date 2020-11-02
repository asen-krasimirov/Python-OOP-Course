from project.pokemon import Pokemon


class Trainer:
    name: str
    pokemon: list

    def __init__(self, name: str):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        pokemon_names = [pok.name for pok in self.pokemon]
        if pokemon.name in pokemon_names:
            return "This pokemon is already caught"

        self.pokemon.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str) -> str:

        for pok in self.pokemon:
            if pok.name == pokemon_name:
                self.pokemon.pop(self.pokemon.index(pok))
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self) -> str:
        trainer_information = [
            f"Pokemon Trainer {self.name}",
            f"Pokemon count {len(self.pokemon)}",
            '\n'.join([f'- {pok.pokemon_details()}' for pok in self.pokemon]),
            ""
        ]
        return '\n'.join(trainer_information)
