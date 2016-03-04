#!/usr/bin/env python 

#import io

class Element(object):
#    tag_indent = {'html':0,'head':4,'meta':8,'title':8,'body':4,'h2':8,'p':8,'hr':8,'ul':8,'li':12}
    tag = 'html'
    indent = '    '
#    content =[]

    def __init__ (self,content=None,**attributes):
        self.cont = []
        self.attributes = attributes
        if content is not None:
            self.cont.append(content)

    def content_add(self,content):
        self.cont.append(content)
    
    def  render_tag(self,current_ind):
        attrs = "".join([' {} ="{}"'.format(key,val) for key, val in self.attributes.items()])
        tag_str = "{}<{}{}>".format(current_ind, self.tag, attrs)
        return tag_str    

    def render(self, file_out,ind = ""):
        file_out.write(self.render_tag(current_ind))
        file_out.write('\n')
        for con in self.content:
            try:
                file_out.write(current_ind +self.indent+con+'\n')
            except TypeError:
                con.render(file_out, current_ind+self.indent)
        file_out.write("{}</{}>\n".format(current_ind, self.tag))

class Html(Element):
    def __init__ (self,content=None,**attributes):
        self.tag = 'html'

    def render(self, file_out,ind = ""):
        file_out.write('<!DOCTYPE html>')
        super(Html,self).render(self, file_out,ind = "")


class Body(Element):
    def __init__ (self,content=None,**attributes):
        self.tag = 'body'      

class P(Element):
    def __init__ (self,content=None,**attributes):
        self.tag = 'p'      

class Head(Element):
    def __init__ (self,content=None,**attributes):
        self.tag = 'head'      

class OneLineTag(Element):
    def render(self, file_out,ind = ""):
        self.render_tag(current_ind)
        file_out.write('<{}>{}'.format(self.tag,current_ind))
        try:
            file_out.write(current_ind +self.indent+self.content)
        except TypeError:
            con.render(file_out, current_ind+self.indent)
        file_out.write("{}</{}>\n".format(current_ind, self.tag))

class Title(OneLineTag):
    def __init__ (self,content=None,**attributes):
        self.tag = 'title'         

class SelfClosingTag(Element): 

    def render(self, file_out,ind = ""):
        self.render_tag(current_ind)
        file_out.write('<{}{}/>\n'.format(self.tag,current_ind))

class meta(SelfClosingTag):
    def render(self, file_out,ind = ""):
        self.render_tag(current_ind)
        file_out.write('<{}{}'.format('meta',current_ind))
        try:
            file_out.write(current_ind +self.indent+self.content)
        except TypeError:
            con.render(file_out, current_ind+self.indent)
        file_out.write("{}/>\n".format(current_ind))

class Hr(SelfClosingTag):
    def __init__ (self,content=None,**attributes):
        self.tag = 'hr'


class Br(SelfClosingTag):
    def __init__ (self,content=None,**attributes):
        self.tag = 'br'

class A(Element):
    def A__init__ (self,link,content=None):
        super(A, self).__init__(content=None,href=link)

class Ul(Element):
    def __init__ (sself,content=None,**attributes):
        self.tag = 'ul'      


class Li(Element):
    def __init__ (self,content=None,**attributes):
        self.tag = 'li'      

class Header(OneLineTag):
    def __init__(self,hl,content=None):
        self.tag = 'h' + hl
        super(Header,self).__init__(content=None,**attributes)


