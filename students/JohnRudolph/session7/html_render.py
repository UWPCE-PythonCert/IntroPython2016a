#!/usr/bin/env python

######################################################
##############    HTML RENDER EXERCISE ###############
######################################################

class Element(object):
    '''
    Generates pretty html dynamically based on user supplied content
    User supplies htmnl tags, associated text and attributes
    '''

    tag = 'html'  #only necesarry because of step1 - subclass element should be used

    def __init__(self, content=None, **attributes):
        # container for content - will be strings or classes
        self.content = []
        # adding attributes dictionary
        self.attributes = attributes
        if content is not None:
            self.append(content)

    def append(self, content):
        #check if content is string or class
        if hasattr(content, 'render'):
            #if class then append
            self.content.append(content)
        else:
            #if string then use TextWrapper to create render class
            #needed so that render does not need to handle both strings/classes
            self.content.append(TextWrapper(content))

    def render_tag(self, current_ind):
        # tag and then content for each class
        attrs = "".join([' {}="{}"'.format(key, val) for key, val in self.attributes.items()])
        # indetation + tag + content
        tag_str = "\n{}<{}{}>".format(current_ind, self.tag, attrs)
        return tag_str

    def render(self, file_out, current_ind=""):
        #check if element is html and print out DOCTYPE is true
        if self.tag == 'html':
            file_out.write('<!DOCTYPE html>')
            StartIndent.indent = current_ind #set initial indent value as class attrib
        self.multi_linewrite(file_out, current_ind) #write out standard tag/content/tag

    def multi_linewrite(self, file_out, current_ind):
        #writes out standard /n/tag/n/content/n/tag format
        #write tag to file
        file_out.write(self.render_tag(current_ind))
        #loop through and render any appended elements
        for i in self.content:
            i.render(file_out, '{}'.format(current_ind + StartIndent.indent))
        # write out closing tag
        file_out.write("\n{}</{}>".format(current_ind, self.tag))


class Html(Element):
    tag = 'html'

class Head(Element):
    tag = 'head'

class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'

class A(Element):
    '''
    Creates a class for an anchor link element
    Need to render opening and closing tags differently
    Than in parent element class
    Also need a special wrapper to handle link text
    '''
    tag = 'a'

    def __init__(self, link, context):
        super(A, self).__init__(content = context, href = link)

    def append(self, content):
        #check if content is string or class
        if hasattr(content, 'render'):
            #if class then append
            self.content.append(content)
        else:
            #if string then use TextWrapper to create render class
            #needed so that render does not need to handle both strings/classes
            self.content.append(TextWrapperAnchor(content))

    def render_tag(self, current_ind):
        #tag and then content for each class
        attrs = "".join([' {}="{}"'.format(key, val) for key, val in self.attributes.items()])
        #indetation + tag + content
        tag_str = "\n{}<{}{}".format(current_ind, self.tag, attrs)
        return tag_str

    def render(self, file_out, current_ind=""):
        #check if element is html and print out DOCTYPE is true
        file_out.write(self.render_tag(current_ind))
        #loop through and render any appended elements
        for i in self.content:
            i.render(file_out, '{}'.format(current_ind + StartIndent.indent))
        #write out closing tag
        file_out.write(" </{}>".format(self.tag))


class OneLineTag(Element):
    '''
    Generates HTML for tags that have open closing tag on same line
    '''
    tag = ''

    def append(self, content):
        #check if content is class or text
        if hasattr(content, 'render'):
            #if class then append
            self.content.append(content)
        else:
            #if string then use TextWrapper to create render class
            #needed so that render does not need to handle both strings/classes
            #need to call TextWrapper for One Line content
            self.content.append(TextWrapperOneLine(content, self.tag))

    def render(self, file_out, current_ind=""):
            #one liners tags and content are handled in TextWrapperOneLine
            for i in self.content:
                i.render(file_out, current_ind)


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):
    '''
    Generates HTML for self closing tags
    '''
    tag = ''

    def render_tag(self, current_ind):
        # tag and then content for each class
        attrs = "".join([' {}="{}"'.format(key, val) for key, val in self.attributes.items()])
        # indetation + tag + content
        tag_str = "\n{}<{} />".format(current_ind, self.tag, attrs)
        return tag_str

    def render(self, file_out, current_ind):
        #write tag to file
        file_out.write('{}'.format(self.render_tag(current_ind)))


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'

class TextWrapper:
    """
    A wrapper that creates a render class for text
    Used when passing in text content so that render method
    Only has to handle class objects
    """

    def __init__(self, text):
        self.text = text

    #writes out text to file
    def render(self, file_out, current_ind=""):
        #have to get indent from IndentCaller based on calling element subclass
        file_out.write('\n{}{}'.format(current_ind, self.text))


class TextWrapperOneLine:
    """
    Used for One Line Renders
    A wrapper that creates a render class for text
    Used when passing in text content so that render method
    Only has to handle class objects
    """
    def __init__(self, text, elem):
        self.text = text
        self.element = elem

    #writes out text to file
    def render(self, file_out, current_ind=""):
        #have to get indent from IndentCaller based on calling element subclass
        tag1, tag2 = '<{}>'.format(self.element), '</{}>'.format(self.element)
        file_out.write('\n{}{} {} {}'.format(current_ind, tag1, self.text, tag2))


class TextWrapperAnchor(TextWrapperOneLine):

    """
    Used for Anchor Element Renders
    Used when passing in link text content so that render method
    Only has to handle class objects
    """

    def __init__(self, text):
        self.text = text

    def render(self, file_out, current_ind=""):
        #have to get indent from IndentCaller based on calling element subclass
        file_out.write('> {}'.format(self.text))


class StartIndent():
    '''
    Hold the initial starting indent value
    '''
    indent = ''

    def __init__(self):
        pass
