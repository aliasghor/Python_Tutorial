# Python OOP (Object Oriented Programming) getter and setter.

"""
    To retrive a private a attributes we'll have to used a decorator called @property. @property decorator will treat a method like an attribute. Additionally we can use @methodname.getter to get/retrive the private attributes. To change the private attributes we'll need to use the @methodname.setter to initalize the private attributes to a new value.
"""

class Hero:
    
    def __init__(self, name: str, health: int, armor: int) -> None:
        self.__name = name
        self.__health = health
        self.__armor = armor

    # Use the @property decorator method to treat a method like an attribute and to retrive the private attributes.

    @property
    def name(self) -> str:
        """A property method to retrive the private attribute name."""
        return self.__name
    
    # Additionally we can explicilty retrive the private attribute like this

    # Make a @property that currently does not do anything. Later it will be used to retrive the private health attribute.
    @property
    def health(self):
        pass

    # Use the decorator @method_name.getter to get the private health attribute.
    @health.getter
    def health(self) -> int:
        """A property method to retrive the private attribute health."""
        return self.__health
    
    @health.setter
    def health(self, newHealth: int) -> None:
        # Type checked the argument
        if not isinstance(newHealth,int):
            raise TypeError(f"Error, expected the attribute value to be an int! Got {type(newHealth).__name__}.")
        
        elif newHealth < 0 or newHealth > 100:
            raise ValueError("Error, the attribute must be higher than 0 or lower than 100.")
        
        else:
            self.__health = newHealth
    
    # Print a string representation of the object (not designed the claritynies to some users).
    def __repr__(self):
        return f"Hero('{self.__name}', {self.__health}, {self.__armor})"