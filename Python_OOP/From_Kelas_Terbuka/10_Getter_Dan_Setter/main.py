import hero

# Create a top-level code environment. A top-level code is where we run the script directly; it is top-level because we imported the module that the main program needs. A top level-code is sometimes called an entry point to our program.

# Check if the module is equal to __main__. If it does then execute this condition.
if __name__ == '__main__':
    # Specified the module and instanciate the class.
    gerry = hero.Hero("Gerry",100,50)

    # Print the object representation
    print(gerry)

    # Print the attributes
    print(f"Hero's name: {gerry.name}")
    print(f"Hero's health: {gerry.health}")
    gerry.health = 40
    print(f"Hero's health after being changed: {gerry.health}")

    