def doNothing():
    """Seriously this function doesn't do anything.The reason why i creating this function is just want to learn the "pass" keyword"""
    pass

print(doNothing.__doc__)

# continue is a keyword to skipped an iterration

i = 0

while i < 5:
    i += 1
    if i == 3:
        continue

    print(f"i -> {i}")
    