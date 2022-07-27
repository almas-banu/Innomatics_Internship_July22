# The Captain's Room

k = int(input())
rooms = list(map(int,input().split()))
family = set()
captain = set()
for room in rooms:
    if room not in family:
        family.add(room)
        captain.add(room)
    else:
        captain.discard(room)
captain = list(captain)
print(captain[0])