# Week 7 - Lab #1: HTML Renderer Exercise
# Date: Friday, February 19, 2016
# Student: Chi Kin Ho

# !/usr/bin/env python

"""
Python class example.
"""

# The start of it all:
# Fill it all in here.


class Element(object):

    tag = 'html' # class attribute
    level = 1 # indentation level

    def __init__(self, content=None, **kwargs):
        # Initialize the Element object with the given content.
        if content is None:
            self.content = list()
        else:
            self.content = [content]

        if kwargs is not None:
            if 'style' in kwargs:
                self.style = kwargs['style']
            else:
                self.style = None

            if 'id' in kwargs:
                self.id = kwargs['id']
            else:
                self.id = None

    def append(self, new_content):
        # Append the new_content to the end of the existing content.
        self.content.append(new_content)

    def render(self, file_out, ind=""):

        file_out.write(ind * Element.level + '<' + self.tag)

        if self.style is not None:
            file_out.write(' ' + 'style="' + self.style + '"')
        if self.id is not None:
            file_out.write(' ' + 'id="' + self.id + '"')

        file_out.write('>\n')

        for content in self.content:
            if isinstance(content, str): # Stop the recursion when content is of string.
                file_out.write(ind * (Element.level + 1) + content + '\n')
            else: # Recursively call render() to print the tag element.
                Element.level += 1
                content.render(file_out, ind)
                Element.level -= 1

        file_out.write(ind * Element.level + '</' + self.tag + '>')

        if self.tag != 'html':
            file_out.write('\n')


class Html(Element):

    tag = 'html' # Override the Element's class attribute with html

    def render(self, file_out, ind=""):

        file_out.write('<!DOCTYPE html>' + '\n')
        Element.render(self, file_out, ind)


class Body(Element):

    tag = 'body' # Override the Element's class attribute with body


class P(Element):

    tag = 'p' # Override the Element's class attribute with p


class Head(Element):

    tag = 'head' # Override the Element's class attribute with head


class OneLineTag(Element):

    def render(self, file_out, ind=""):

        file_out.write(ind * Element.level + '<' + self.tag + '>')
        file_out.write(' ' + self.content[0] + ' ')
        file_out.write('</' + self.tag + '>' + '\n')


class Title(OneLineTag):

    tag = 'title' # Override the OneLineTag's class attribute with title


class SelfClosingTag(Element):

    def render(self, file_out, ind=""):

        file_out.write(ind * Element.level + '<' + self.tag + ' />' + '\n')


class Hr(SelfClosingTag):

    tag = 'hr' # Override the SelfClosingTag's class attribute with hr


class Br(SelfClosingTag):

    tag = 'br' # Override the SelfClosingTag's class attribute with br


class Meta(SelfClosingTag):

    tag = 'meta' # Override the SelfClosingTag's class attribute with meta

    def __init__(self, **kwargs):

        Element.__init__(self, None)
        if 'charset' in kwargs:
            self.charset = kwargs['charset']

    def render(self, file_out, ind=""):

        file_out.write(ind * Element.level + '<' + self.tag + ' charset="' + self.charset + '" />' + '\n')


class A(Element):

    tag = 'a' # Override the Element's class attribute with a

    def __init__(self, link, content=None):

        Element.__init__(self, content)
        self.link = link # Store the hyperlink of the anchor tag.

    def render(self, file_out, ind=""):

        file_out.write(ind * Element.level + '<' + self.tag + ' href="' + self.link + '">')

        for content in self.content:
            if isinstance(content, str): # Stop the recursion when content is of string.
                file_out.write(' ' + content + ' ')
            else: # Recursively call render() to print the tag element.
                Element.level += 1
                content.render(file_out, ind)
                Element.level -= 1

        file_out.write('</' + self.tag + '>\n')


class Ul(Element):

    tag = 'ul' # Override the Element's class attribute with ul


class Li(Element):

    tag = 'li' # Override the Element's class attribute with li


class H(OneLineTag):

    tag = 'h' # Override the OneLineTag's class attribute with h2

    def __init__(self, size, content=None, **kwargs):

        self.tag += str(size) # Add the size of the header to the tag name
        Element.__init__(self, content, **kwargs)

