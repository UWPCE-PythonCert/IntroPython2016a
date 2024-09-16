#!/usr/bin/env python
#Krishna Bindhu
#Date:3/2/2016
"""
Python class example.
"""

#calss ELEMENT
# The start of it all:
# Fill it all in here.
class Element(object):
    """class attributes"""
    tag ='<html>'
    indent=''
    """class methods"""
    def __init__(self, content=""):
        self.content=[]
        if content is not None:
            self.content.append(content)
    def append(self, content):
        self.content.append(content)
    def render(self, file_out,ind=''):
        file_out.write(ind*4+self.tag)
        file_out.write('\n')
        file_out.write(str(self.content))
        file_out.write('\n')
        file_out.write(ind*4+"<\"+self.tag+">'')

"""
#subclass html
class Html(Element):
    tag='<html>'
    def __init__(self, content=""):
        super().__init__(content)



class Body(Element):
    tag='<body>'
    def __init__(self, content=""):
        super().__init__(content)
    def render(self, file_out,ind=''):
        file_out.write(ind*8+self.tag+"\n")
        file_out.write(self.content)
        file_out.write('\n')
        file_out.write(ind*8+"<\body>")

class P(Element):
    tag='<p>'
    def __init__(self, content=""):
        super().__init__(content)
    def append(self, content):
        super(P,self).append(content)
    def render(self, file_out,ind=''):
        file_out.write(ind*12+self.tag+"\n")
        file_out.write(ind*16+self.content)
        file_out.write('\n')
        file_out.write(ind*8+"<\p>")
"""
