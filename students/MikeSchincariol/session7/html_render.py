import io

class Element(object):

    @classmethod
    def check_content_is_compat(cls, content):
        if isinstance(content, str) or isinstance(content, Element):
            return True
        else:
            return False


    def __init__(self, content=None, **kwargs):
        '''
        :param content: The string or element instance to initialize the element with.
        :param kwargs: Attributes that are associated with the content
        :return: Nothing
        '''
        self.tag = 'tag'
        self.data = []
        self.attr = kwargs

        if content is not None:
            if Element.check_content_is_compat(content):
                self.data.append(content)
            else:
                raise ValueError("The 'content' argument must be a string or another Element")


    def append(self, content, **kwargs):
        '''
        :param content: The string or element instance to add to the items already in the element
        :param kwargs: Attributes that are associated with the content
        :return: Nothing
        '''

        self.attr.update(kwargs)
        if content is not None:
            if Element.check_content_is_compat(content):
                self.data.append(content)
            else:
                raise ValueError("The 'content' argument must be a string or another Element")


    def _render_start_tag(self, file_out, ind, inline=True, self_closing=False):
        try:
            if not inline:
                file_out.write("\n{0}".format(ind))
            file_out.write("<{0}".format(self.tag))
            for k,v in self.attr.items():
                file_out.write(' {0}="{1}"'.format(k, v))
            if self_closing:
                file_out.write("/>")
            else:
                file_out.write(">")
        except AttributeError:
            raise ValueError("The 'file_out' argument must be a class or subclass of io.TextIOBase")


    def _render_data(self, file_out, ind, inline=True):
        sub_ind = " " * (len(ind) + 3)

        for idx, item in enumerate(self.data):
            try:
                # Assume it is an Element
                item.render(file_out, sub_ind)
            except AttributeError:
                # Guess not...assume it is a string :)
                try:
                    if not inline:
                        file_out.write("\n{0}".format(sub_ind))
                    file_out.write("{0}".format(item))
                except AttributeError:
                    raise ValueError("The 'file_out' argument must be a class or subclass of io.TextIOBase")


    def _render_end_tag(self, file_out, ind, inline=True):
        try:
            if not inline:
                file_out.write("\n{0}".format(ind))
            file_out.write("</{0}>".format(self.tag))
        except AttributeError:
                    raise ValueError("The 'file_out' argument must be a class or subclass of io.TextIOBase")


    def render(self, file_out, ind = ""):
        '''

        :param file_out: A io.TextIOBase file object
        :param ind: A string, which supplies the amount of indentation whitespace to use
        :return: Nothing
        '''
        self._render_start_tag(file_out, ind, False, False)
        self._render_data(file_out, ind, False)
        self._render_end_tag(file_out, ind, False)



class Html(Element):
    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)
        self.tag = "html"
        self.data.append("<!DOCTYPE html>")


class Body(Element):
    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)
        self.tag = "body"


class P(Element):
    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)
        self.tag = "p"


class Head(Element):
    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)
        self.tag = "head"

class Ul(Element):
    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)
        self.tag = "ul"

class Li(Element):
    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)
        self.tag = "li"


class OneLineTag(Element):
    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)
        self.tag = "head"

    def render(self, file_out, ind=""):
        '''

        :param file_out: A io.TextIOBase file object
        :param ind: A string, which supplies the amount of indentation whitespace to use
        :return: Nothing
        '''
        self._render_start_tag(file_out, ind, False, False)
        self._render_data(file_out, ind, True)
        self._render_end_tag(file_out, ind, True)



class Title(OneLineTag):
    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)
        self.tag = "title"

class H(OneLineTag):
    def __init__(self, hdr_lvl, content=None, **kwargs):
        super().__init__(content, **kwargs)
        self.tag = "h{0}".format(hdr_lvl)


class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)
        self.tag = "selfclosing"

    def render(self, file_out, ind = ""):
        '''

        :param file_out: A io.TextIOBase file object
        :param ind: A string, which supplies the amount of indentation whitespace to use
        :return: Nothing
        '''
        self._render_start_tag(file_out, ind, True, True)
        self._render_data(file_out, ind, True)



class Hr(SelfClosingTag):
    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)
        self.tag = "hr"

class Br(SelfClosingTag):
    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)
        self.tag = "br"

class Meta(SelfClosingTag):
    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)
        self.tag = "meta"
        self.attr['charset']="UTF-8"


class A(Element):
    def __init__(self, link, content):
        super().__init__(content, href=link)
        self.tag = "a"