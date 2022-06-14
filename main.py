from player_builder import player_builder
from header import title

#title header

print(title)
print("\nA text Adventure by Alex Francis")
start = input('Shall we begin? Type start to begin.')
if start == 'start':
    player = player_builder()


