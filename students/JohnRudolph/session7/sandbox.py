#!/usr/bin/env python

"""
a simple script can run and test your html rendering classes.

Uncomment the steps as you add to your rendering.

"""

from io import StringIO

# importing the html_rendering code with a short name for easy typing.
import html_render as hr
# reloading in case you are running this in iPython
#  -- we want to make sure the latest version is used
import importlib
importlib.reload(hr)


# writing the file out:
def render_page(page, filename):
    """
    render the tree of elements

    This uses StringIO to render to memory, then dump to console and
    write to file -- very handy!
    """

    f = StringIO()
    page.render(f, "    ")

    f.seek(0)

    print(f.read())

    f.seek(0)
    open(filename, 'w').write(f.read())


# Step 1
#########

page = hr.Html()

page.append("Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text")

page.append("And here is another piece of text -- you should be able to add any number")

render_page(page, "classsandbox.html")

# ## Step 2
# ##########

page = hr.Html()

body = hr.Body()

body.append(hr.P("Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text"))

body.append(hr.P("And here is another piece of text -- you should be able to add any number"))

page.append(body)

render_page(page, "test_html_output2.html")

#Step 3
page = hr.Html()

head = hr.Head()
head.append(hr.Title("PythonClass = Revision 1087:"))

page.append(head)

body = hr.Body()

body.append(hr.P("Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text"))
body.append(hr.P("And here is another piece of text -- you should be able to add any number"))

page.append(body)

render_page(page, "test_html_output3.html")