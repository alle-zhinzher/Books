"""
Let's begin with the what we have part. Our application has a Computer class that
shows basic information about a computer. All the classes of this example, including
the Computer class are very primitive, because we want to focus on the Adapter
pattern and not on how to make a class as complete as possible.
"""


class Computer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} computer'.format(self.name)

    def execute(self):
        return 'executes a program'


"""
We decide to enrich our application with
more functionality, and luckily, we find two interesting classes implemented in two
different libraries that are unrelated with our application: Synthesizer and Human .
In the Synthesizer class, the main action is performed by the play() method. In the
Human class, it is performed by the speak() method. To indicate that the two classes
are external, we place them in a separate module, as shown:
"""


class Synthesizer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} synthesizer'.format(self.name)

    def play(self):
        return 'is playing an electronic song'


class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '{} the human'.format(self.name)

    def speak(self):
        return 'says hello'


"""
The client only knows how to call the
execute() method, and it has no idea about play() or speak() . How can we make
the code work without changing the Synthesizer and Human classes? Adapters to
the rescue! We create a generic Adapter class that allows us to adapt a number of
objects with different interfaces, into one unified interface. The obj argument of the
__init__() method is the object that we want to adapt, and adapted_methods is a
dictionary containing key/value pairs of method the client calls/method that should
be called.
"""


class Adapter:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


"""
Let's see how we can use the Adapter pattern. An objects list holds all the objects.
The compatible objects that belong to the Computer class need no adaptation. We can
add them directly to the list. The incompatible objects are not added directly. They
are adapted using the Adapter class. The result is that the client code can continue
using the known execute() method on all objects without the need to be aware of
any interface differences between the used classes.
"""


def main():
    objects = [Computer('Asus')]
    synth = Synthesizer('moog')
    objects.append(Adapter(synth, dict(execute=synth.play)))
    human = Human('Bob')
    objects.append(Adapter(human, dict(execute=human.speak)))
    for i in objects:
        print('{} {}'.format(str(i), i.execute()))


if __name__ == "__main__":
    main()
