# Set .add()

no_stamps = int(input())
stamps = set()
for stamp in range(no_stamps):
    stamps.add(input())

print(len(stamps))