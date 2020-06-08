import xml.etree.ElementTree as ET
import bisect


class Scheme(object):
    def __init__(self, tag):
        self.tag = tag
        self.attributes = list()
        self.children = list()

    def __str__(self):
        return '{}({})'.format(self.tag, ', '.join(self.attributes))

    def __gt__(self, other):
        return str(self) > str(other)

    def __eq__(self, other):
        return str(self) == str(other)

    def save_data(self, output, k=0):
        info = '{}{}'.format('--'*k, str(self))
        output.append(info)
        for child in self.children:
            child.save_data(output, k + 1)

    def add_attributes(self, keys):
        for attrib in keys:
            if attrib not in self.attributes:
                bisect.insort(self.attributes, attrib)

    def add_child(self, child):
        if child not in self.children:
            self.children.append(child)


def xml_tags(xml):
    root = ET.fromstring(xml)

    tree = dict()
    scheme = Scheme(root.tag)
    scheme.add_attributes(root.attrib.keys())
    xml_walk(root, tree, scheme)
    output = list()
    scheme.save_data(output)
    return output


def xml_walk(root, tree, parent):
    save(parent, tree)
    for element in root:
        child = find_child_scheme(tree, element.tag)
        child.add_attributes(element.attrib.keys())
        parent.add_child(child)
        if len(element) > 0:
            xml_walk(element, tree, child)
        else:
            save(child, tree)


def find_child_scheme(tree, tag):
    if tag in tree.keys():
        return tree.get(tag)
    return Scheme(tag)


def save(scheme, tree):
    tag = scheme.tag
    if tag not in tree:
        tree[tag] = scheme


print(xml_tags(""))
