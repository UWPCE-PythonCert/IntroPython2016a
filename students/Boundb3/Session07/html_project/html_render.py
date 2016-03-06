#!/usr/bin/env python

"""
B3 version copy - start

Python class example.

"""

# The start of it all:
# Fill it all in here.

class Element(object):
    #class attributes
    tag = "element tag"
    indent = "    "
    print("hi")
    #content = []


    def __init__(self, content=None, **attributes): ###!!!could i have added the link attribute here??
        #store content
        self.content = []


        # add an attributes dictionary
        self.attributes = attributes

        #check for content
        if content is not None:
            self.content.append(content)
            print("there was content in init. init appended content = {} to self = {} ".format(content,self.tag))
        print("\t\tcompleted init call for:", self.tag, "\n" )

    def ToString(self):
        return self.tag
    #to over write the default __str__
    def __str__(self):
        return self.ToString()


    def append(self, new_content):
        #add new string content to content list
        print("\t\tcalling append function \n appending: appending {} to {} ".format(new_content, self.tag  ))
        if new_content is not "":
            self.content.append(new_content)

    #new render tag method
    def render_tag(self, current_ind):
        # tag and then content for each class
        attrs = "".join([' {} ="{}"'.format(key,val) for key, val in self.attributes.items()])
        #print("this is self.attributes from render_tag:  ", self.attributes)
        #indentation + tag + content
        tag_str = "{}<{}{}>".format(current_ind, self.__str__(), attrs)
        #print("from render_tag: current_ind is '{}' and tag strg is '{}'".format(current_ind, tag_str))
        return tag_str

    def render(self, file_out, current_ind= " default indent"):
        print("entering rendering func ")
        #print("this is current ind: ", current_ind)
        #print("this is self.tag '{}' inside render func and this is self.__str__ '{}' :  ".format(self.tag, self.__str__()))

        #now render will call the render tag menthod - instead of just a string defined tag
        file_out.write(self.render_tag(current_ind)) # the problem here is that the current_ind attribute is carrying text of: html, or htmlbody inside the attribute!!!

        print("just finished call to render_tag")
        file_out.write("\n")

        for con in self.content:
            try:
                #render it
                print("\t--> con is: " , con)
                file_out.write(current_ind + self.indent + con+"\n") #was: stuff_str.render(file_out)
            except TypeError as e:
                print("hit a snag: ", e, "con is: ", con)
                con.render(file_out, current_ind + self.indent) # was: .write(str(stuff_str)) ### watch it if it is self.tag

        #write out closing tag
            #was:
            #stop at the closing html tag
            #end_tag = "</{}>".format(self.tag)
            #add that tag to the end of the file object
            #file_out.write(end_tag)
        file_out.write("{}</{}>\n".format(current_ind, self.tag))



class Body (Element):
    tag = "body"
    print("subclass tag = : ",tag)
    pass

class P (Element):
    #print(super.tag) Why does this not work? (to print out the super's tag)
    tag = "p"
    print("subclass tag = : ",tag)
    pass

class Html (Element):
    tag = "html"
    print("subclass tag = : ",tag)
    pass

class Head (Element):
    tag = "head"

    pass

class OneLineTag (Element):
    def render(self, file_out, current_ind= " default indent"):
        print("entering OneLineTag rendering func ")

        #now render will call the render tag menthod
        file_out.write(self.render_tag(current_ind))

        #print("just finished call to render_tag")
        #file_out.write("\n") # B3 - this is not needed in this render subclass

        for con in self.content:
            try:
                #render it
                print("\t--> con is: " , con)
                file_out.write(current_ind + self.indent + con ) #b-3 removed +"\n" from the write instructions to stay on the same line
            except TypeError as e:
                print("hit a snag: ", e, "con is: ", con)
                con.render(file_out, current_ind + self.indent) # was: .write(str(stuff_str)) ### watch it if it is self.tag

        #write out closing tag
        file_out.write("{}</{}>\n".format(current_ind, self.tag))

class Title (OneLineTag):
    tag = "title"
    pass

class SelfClosingTag (Element):
    def render(self, file_out, current_ind= " default indent"):
        print("entering SelfClosingTag rendering func ")
        #write out closing tag
        file_out.write("{}<{} /> {}\n".format(current_ind, self.tag, self.attributes))

'''
#comment out this section
        #now render will call the render tag menthod
        #file_out.write(self.render_tag(current_ind))

        #print("just finished call to render_tag")
        #file_out.write("\n") # B3 - this is not needed in this render subclass

        for con in self.content:
            try:
                #render it
                print("\t--> con is: " , con)
                file_out.write(current_ind + self.indent + con) #b-3 removed +"\n" from the write instructions to stay on the same line
            except TypeError as e:
                print("hit a snag: ", e, "con is: ", con)
                con.render(file_out, current_ind + self.indent) # was: .write(str(stuff_str)) ### watch it if it is self.tag
'''

class Hr (SelfClosingTag):
    tag = "hr"
    pass

class Br (SelfClosingTag):
    tag = "br"
    pass

class A (Element):
    tag = "a"



    def __init__(self, content=None, link="link",**attributes):
        self.attributes = "href="
        contentstr = "href=" + '"'+content+'">' + link
        super().__init__(contentstr,**attributes) #!!! not quite right - needs the format:  <a href="http://google.com"> link </a>

        #self.link = link
    pass

class Ul (Element):
    tag = "ul"

class Li (Element):
    tag = "li"

class H (OneLineTag):
    tag = "header"

    def __init__(self,header,content = None,**attributes):
        switchdict = {1:"h1",2:"h2",3:"h3"}

        self.header = switchdict[int(header)]
        self.tag = self.header
        super().__init__(content,**attributes)
