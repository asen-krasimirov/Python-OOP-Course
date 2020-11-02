from project.player import Player
from project.guild import Guild


player = Player("name", 10, 10)
player1 = Player("name1", 10, 10)
player2 = Player("name2", 10, 20)

player1.add_skill("fire", 20)
player1.add_skill("ice", 200)
player.add_skill("earth", 200)
player.add_skill("marce", 200)

guild = Guild("UGT")
print(guild.assign_player(player))
# print(guild.assign_player(player1))
# print(guild.assign_player(player2))
print(guild.guild_info())
