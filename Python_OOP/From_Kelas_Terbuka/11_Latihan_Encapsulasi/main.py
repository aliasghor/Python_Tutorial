# Import the hero module
import hero

# Create a top-level code environment. Check if the condition of the module's name is equal to __main__, if it does then execute the condition.
if __name__ == '__main__':
    # Specified a class from a module and instanciate it.
    gerry = hero.Hero("Gerry",100,5,10)
    mogi = hero.Hero("Mogi",100,5,100)

    print(repr(gerry))
    print(str(gerry))

    print('\n')

    print(repr(mogi))
    print(str(mogi))

    print('\n')
    gerry.attack(mogi)
    gerry.attack(mogi)
    gerry.attack(mogi)
    print(gerry)