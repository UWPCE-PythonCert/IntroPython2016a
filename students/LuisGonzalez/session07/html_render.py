
class Element(object):
    tag = "html"
    indent = 1
    def __init__(self, content = None, **kwargs):

        self.content = content

        if len(kwargs) > 0:
            self.extraAttributes = str(kwargs).strip('{}')
            self.extraAttributes = self.extraAttributes.replace("'", "", 2)
            self.extraAttributes = " " + self.extraAttributes.replace("'", '"')
        else:
            self.extraAttributes = None
        if self.content is None:
            self.content = list()
        else:
            self.content = [content]
    def append(self, new_content):
        self.content.append(new_content)

    def render(self, file_out, ind=""):
        if self.tag == "html":
            file_out.write("<!DOCTYPE html>\n")

        file_out.write(ind * Element.indent + "<" + self.tag)
        if self.extraAttributes is not None:
            file_out.write(self.extraAttributes)
            file_out.write(">\n ")
        else:
            file_out.write(">\n")

        for content in self.content:

            if isinstance(content, str):
                file_out.write(ind * (Element.indent + 1) + content + '\n')
            else:
                Element.indent += 1
                content.render(file_out, ind)
                Element.indent -= 1

        file_out.write(ind * Element.indent + "</" + self.tag + ">\n")

class Html(Element):
    tag = "html"

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

class OneLineTag(Element):
    def render(self, file_out, ind=""):
        file_out.write(ind * Element.indent + "<" + self.tag + "> ")

        for content in self.content:
            file_out.write(content)
        file_out.write(" </" + self.tag + ">\n")

class Title(OneLineTag):
    tag = "title"

class SelfClosingTag(Element):
    def render(self, file_out, ind=""):
        file_out.write(ind * Element.indent + "<" + self.tag + " /> \n")

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

class A(Element):
    tag = "a"
    def __init__(self, link, content):
        self.link = link
        self.content = content
        self.extraAttributes = None

    def render(self, file_out, ind=""):
        file_out.write(ind * Element.indent + "<" + self.tag + ' href="' + self.link + '"')
        file_out.write("> " + self.content + " </" + self.tag + ">\n")

class Ul(Element):
    tag = "ul"

class Li(Element):
    tag = "li"

class H(OneLineTag):
    tag = "h"
    def __init__(self, level, content = None):
        self.tag = self.tag + str(level)
        self.level = level
        self.content = content

class Meta(SelfClosingTag):
    tag = "meta"
    def __init__(self, **kwargs):
        self.content = str(kwargs)
        self.content = str(kwargs).strip('{}')
        self.content = self.content.replace("'", "", 2)
        self.content = " " + self.content.replace("'", '"')

    def render(self, file_out , ind=""):
        file_out.write(ind * Element.indent + "<" + self.tag)
        file_out.write(self.content + "/>\n")

