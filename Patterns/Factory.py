import xml.etree.ElementTree as etree
import json
'''
The JSONConnector class parses the JSON file and has a parsed_data() method
that returns all data as a dictionary ( dict ). The property decorator is used to make
parsed_data() appear as a normal variable instead of a method as follows:
'''


class JSONConnector:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


'''
The XMLConnector class parses the XML file and has a parsed_data() method that
returns all data as a list of xml.etree.Element as follows:
'''


class XMLConnector:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


'''
The connection_factory() function is a Factory Method. It returns an instance of
JSONConnector or XMLConnector depending on the extension of the input file path as follows:
'''


def connection_factory(filepath):
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(filepath))
    return connector(filepath)


'''
The connect_to() function is a wrapper of connection_factory() . It adds
exception handling as follows:
'''


def connect_to(filepath):
    factory = None
    try:
        factory = connection_factory(filepath)
    except ValueError as ve:
        print(ve)
    return factory


'''
The main() function demonstrates how the Factory Method design pattern can be
used. The first part makes sure that exception handling is effective as follows:
'''


def main():
    sqlite_factory = connect_to('data/person.sq3')

    xml_factory = connect_to('data/person.xml')
    xml_data = xml_factory.parsed_data()

    json_factory = connect_to('data/donut.json')
    json_data = json_factory.parsed_data


if __name__ == '__main__':
    main()
