#!/usr/bin/env python

"""
Python class example.
"""


# The start of it all:
# Fill it all in here.
class Element(object):

    tag = 'html'  # shouldn't really be usable without properly subclassing
    indent = '    '

    def __init__(self, content=None, **attributes):

        self.content = []
        # adding attributes dictionary
        self.attributes = attributes

        if content is not None:
            self.content.append(content)

    def append(self, content):
        self.content.append(content)

    # added render tag method to deal with any type of tag at indentation level
    def render_tag(self, current_ind):
        # tag and then content for each class
        attrs = "".join([' {}="{}"'.format(key, val) for key, val in self.attributes.items()])
        # indentation + tag + content
        tag_str = "{}<{}{}>".format(current_ind, self.tag, attrs)
        return tag_str

    def render(self, file_out, current_ind=""):
        # render method now calls the render tag method instead of just a string
        file_out.write(self.render_tag(current_ind))
        file_out.write('\n')
        for con in self.content:
            try:
                file_out.write(current_ind + self.indent + con+"\n")
            except TypeError:
                con.render(file_out, current_ind+self.indent)
        # write out closing tag
        file_out.write("{}</{}>\n".format(current_ind, self.tag))


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Html(Element):
    tag = 'html'


class Head(Element):
    tag = 'head'


class Title(Element):
    tag = 'title'
