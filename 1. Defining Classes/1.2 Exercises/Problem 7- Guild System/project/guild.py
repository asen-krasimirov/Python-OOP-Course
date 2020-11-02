from project import player
from typing import List


class Guild:
    name: str
    player_list = List[player.Player]

    def __init__(self, name: str):
        self.name = name
        self.player_list = []

    def assign_player(self, player: player.Player) -> str:
        player_guild = player.guild
        player_name = player.name

        if player_guild == self.name:
            return f"Player {player_name} is already in the guild."

        if player_guild != "Unaffiliated" and player_guild != self.name:
            return f"Player {player_name} is in another guild."

        player.guild = self.name
        self.player_list.append(player)
        return f"Welcome player {player_name} to the guild {self.name}"

    def kick_player(self, player_name: str) -> str:
        for member in self.player_list:
            if member.name == player_name:
                member.guild = "Unaffiliated"
                self.player_list.remove(member)
                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        guild_information = [
            f"Guild: {self.name}",
            '\n'.join([member.player_info() for member in self.player_list]),

        return '\n'.join(guild_information)
