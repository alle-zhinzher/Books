from enum import Enum
from abc import ABCMeta, abstractmethod

"""
We begin with a Server interface. An Enum parameter describes the different
possible states of a server. We use the abc module to forbid direct instantiation
of the Server interface and make the fundamental boot() and kill() methods
mandatory, assuming that different actions are needed to be taken for booting,
killing, and restarting each server.
"""
State = Enum('State', 'new running sleeping restart zombie')


class Server(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    def __str__(self):
        return self.name

    @abstractmethod
    def boot(self):
        pass

    @abstractmethod
    def kill(self, restart=True):
        pass


"""
A modular operating system can have a great number of interesting servers: a file
server, a process server, an authentication server, a network server, a graphical/
window server, and so forth. The following example includes two stub servers-
the FileServer , and the ProcessServer . Apart from the methods required to be
implemented by the Server interface, each server can have its own specific methods.
For instance the FileServer has a create_file() method for creating files, and the
ProcessServer has a create_process() method for creating processes.
"""


class FileServer(Server):
    def __init__(self):
        '''actions required for initializing the file server'''
        self.name = 'FileServer'
        self.state = State.new

    def boot(self):
        print('booting the {}'.format(self))
        '''actions required for booting the file server'''
        self.state = State.running

    def kill(self, restart=True):
        print('Killing {}'.format(self))
        '''actions required for killing the file server'''
        self.state = State.restart if restart else State.zombie

    def create_file(self, user, name, permissions):
        '''check validity of permissions, user rights, etc.'''
        print("trying to create the file '{}' for user '{}' with permissions {}"
              .format(name, user, permissions))


class ProcessServer(Server):
    def __init__(self):
        '''actions required for initializing the process server'''
        self.name = 'ProcessServer'
        self.state = State.new

    def boot(self):
        print('booting the {}'.format(self))
        '''actions required for booting the process server'''
        self.state = State.running

    def kill(self, restart=True):
        print('Killing {}'.format(self))
        '''actions required for killing the process server'''
        self.state = State.restart if restart else State.zombie

    def create_process(self, user, name):
        '''check user rights, generate PID, etc.'''
        print("trying to create the process '{}' for user'{}'".format(name, user))

"""The OperatingSystem class is a Facade. In __init__() , all the necessary server
instances are created. The start() method, used by the client code, is the entry point
to the system. More wrapper methods can be added, if necessary, as access point
to the services of the servers such as the wrappers create_file() and create_
process() . From the client's point of view, all those services are provided by the
OperatingSystem class. The client should not be confused with unnecessary details
such as the existence of servers and the responsibility of each server.
"""
class OperatingSystem:
    '''The Facade'''
    def __init__(self):
        self.fs = FileServer()
        self.ps = ProcessServer()
    def start(self):
        [i.boot() for i in (self.fs, self.ps)]
    def create_file(self, user, name, permissions):
        return self.fs.create_file(user, name, permissions)
    def create_process(self, user, name):
        return self.ps.create_process(user, name)

def main():
    os = OperatingSystem()
    os.start()
    os.create_file('foo', 'hello', '-rw-r-r')
    os.create_process('bar', 'ls /tmp')
if __name__ == '__main__':
    main()