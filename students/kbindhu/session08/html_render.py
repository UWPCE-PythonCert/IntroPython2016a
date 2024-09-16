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
    tag ='html'
    """class methods"""
    def __init__(self, content1=None,**kwargs):
        #if nothing passed content is an empty list
        self.content=[]
        self.kwargs=kwargs
        if content1 is not None:
            #appending strings/objects passed to list
            self.content.append(content1)
    def append(self, content1):
        self.content.append(content1)
    def render(self, file_out,ind='    '):
        start_tag="<{}>".format(self.tag)
        # this for step4 adding additional arguments for tags
        for k,v in self.kwargs.items():
            start_tag="<{} {}={}>".format(self.tag,k,v)
        file_out.write(ind+start_tag)
        file_out.write('\n')
        # iterating through the list 
        for i in range(0,len(self.content)):
            #checking the member in a list is a string
            #if string add 4 spaces and string
            if (isinstance(self.content[i], str)):
                file_out.write(ind + '    ' + self.content[i])
                file_out.write('\n')
            else:
                # call recursively the render if the content appended is a class and add 4 spaces
                self.content[i].render(file_out,ind + '    ')
                file_out.write('\n')
        end_tag="</{}>".format(self.tag)
        file_out.write(ind+end_tag)


#subclass HTML

class Html(Element):
    #overiding tag
    tag='html'
    def render(self, file_out,ind='    '):
        file_out.write("<!DOCTYPE html>\n")
        super().render(file_out,ind="    ")
#subclass HTML
class Body(Element):
    #overiding tag
    tag='body'

class P(Element):
    #overiding tag
    tag='p'
#subclass Head
class Head(Element):
    #overiding tag
    tag='head'
#One lineTag subclass
class OneLineTag(Element):
    #overiding the render method to print content in one line
    def render(self, file_out,ind='    '):
        start_tag="<{}>".format(self.tag)
        file_out.write(ind+start_tag)
        # iterating through the list 
        for i in range(0,len(self.content)):
            #checking the member in a list is a string
            if (isinstance(self.content[i], str)):
                file_out.write(self.content[i])
            else:
                # call recursively the render if the content appended is a class
                self.content[i].render(file_out,ind)
        end_tag="</{}>".format(self.tag)
        file_out.write(end_tag)
        file_out.write('\n')

#subclass Title
class Title(OneLineTag):
    tag='title'
 
 #SelfClosing Tag subclass
class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)
#overirding render method to render end tag alone
    def render(self, file_out,ind='    '):
        #checking whether arguments are empty(this is done for self closing tags br and hr where there are no arguments)
        if(self.kwargs is None):
            end_tag="<{} />".format(self.tag)
            file_out.write(ind+end_tag)
            #this is for meta class wnen there ia argument being passed
        else:
            for k,v in self.kwargs.items():
                end_tag="<{} {}= {}/>".format(self.tag,k,v)
                file_out.write(ind+end_tag)
#subclass Hr and Br
class Hr(SelfClosingTag):
    tag='hr'
class Hr(SelfClosingTag):
    tag='br'

#Anchor class
class A(Element):
    tag='a'
    def __init__(self, content,link):
        super().__init__(content)
        #passing link as keywrod argument to element class
        self.kwargs["href"]=link

#subclass Unordered List
class Ul(Element):
    tag="ul"

#ordered List
class Li(Element):
    tag="li"
#subclass H
class H(OneLineTag):
    def __init__(self,number,content):
        self.tag="h"+str(number)
        super().__init__(content)
#subclass  Meta
class Meta(SelfClosingTag):
    tag='meta'
    def __init__(self,content=None,**kwargs):
        super().__init__(content)
        self.kwargs['charset']="UTF-8"

