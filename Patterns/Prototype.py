"""
Let's see how we can use the Prototype pattern for creating an application that
shows book information. We begin with the representation of a book. Apart from
the usual initialization, the Book class demonstrates an interesting technique. It
shows how we can avoid the telescopic constructor problem. In the __init__()
method, only three parameters are fixed: name , authors , and price . But clients
can pass more parameters in the form of keywords (name=value) using the rest
variable-length list. The line self.__dict__.update(rest) adds the contents of
rest to the internal dictionary of the Book class to make them part of it.

But there's a catch. Since we don't know all the names of the added parameters,
we need to access the internal dict for making use of them in __str__() . And
since the contents of a dictionary do not follow any specific order, we use an
OrderedDict to force an order; otherwise, every time the program is executed,
different outputs will be shown. Of course, you should not take my words for
granted. As an exercise, remove the usage of OrderedDict and sorted() and
run the example to see if I'm right:
"""
import copy
from collections import OrderedDict
class Book:
    def __init__(self, name, authors, price, **rest):
        '''Examples of rest: publisher, length, tags, publication
        date'''
        self.name = name
        self.authors = authors
        self.price = price
        # in US dollars
        self.__dict__.update(rest)
    def __str__(self):
        mylist=[]
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            mylist.append('{}: {}'.format(i, ordered[i]))
            if i == 'price':
                mylist.append('$')
            mylist.append('\n')
        return ''.join(mylist)

class Prototype:
    def __init__(self):
        self.objects = dict()

    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        del self.objects[identifier]

    def clone(self, identifier, **attr):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError('Incorrect object identifier:{}'.format(identifier))
        obj = copy.deepcopy(found)
        obj.__dict__.update(attr)
        return obj

def main():
    b1 = Book('The C Programming Language', ('Brian W. Kernighan',
                                             'Dennis M.Ritchie'),
                                            price=118,
                                            publisher='Prentice Hall',
                                            length=228,
                                            publication_date='1978-02-22',
                                            tags=('C',
                                                  'programming',
                                                  'algorithms',
                                                  'data structures'
                                                  )
                                            )
    prototype = Prototype()
    cid = 'k&r-first'
    prototype.register(cid, b1)
    b2 = prototype.clone(cid, 
                        name='The C Programming Language(ANSI)',
                        price=48.99,
                        length=274,
                        publication_date='1988-04-01',
                        edition=2,
                        tags=('C+++',
                             "Patterns"
                             ),
                        )
    for i in (b1, b2):
        print(i)
    print("ID b1 : {} != ID b2 : {}".format(id(b1), id(b2)))
if __name__ == '__main__':
    main()