from player_builder import player_builder
from header import title
import time

#title header

print(title)
print("\nA text Adventure by Alex Francis")
start = input('Shall we begin? Type start to begin.\n')
if start == 'start':
    player = player_builder()
else:
    print('There is no choice. Let us begin.')
    time.sleep(3)
    player = player_builder()    


