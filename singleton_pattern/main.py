    # """
    # Singleton is basically to create only one instance of a class in whole the application.
    # Example : Database connection , Cache Implementation

    # """

class Singleton(object):
    
    # default constructor
    def __new__(cls, *args, **kwargs):     
        if not hasattr(cls, 'instance') or not cls.instance:
          cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, language):
        self.language = language

obj1 = Singleton("English")
obj2 = Singleton("German")

print(obj1)
print(obj2)
# will print the same instance

print(obj1 == obj2)
# will print True


# https://medium.com/analytics-vidhya/singleton-design-pattern-python-use-case-c85fc870eda2