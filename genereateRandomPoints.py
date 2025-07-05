from random import randint
def genereateRandomPoints(Range,type):
    tab = []

    for i in range(30):
        tab.append(randint(0,Range))

    print(f"Random Points list {type}: {tab}")
    return tab