#!/usr/bin/env python
from filecmp import cmp

"""
Test for steps in html render lab
"""

#Test part 1
def test_html1():
    f1path = 'test_html_output1.html'    
    f2path = '/home/johnr_000/py101/IntroPython2016a/Examples/Session07/html_render/test_html_output1.html'
    assert cmp(f1path, f2path, shallow=False)

#Test part 2
def test_html2():
    f1path = 'test_html_output2.html'    
    f2path = '/home/johnr_000/py101/IntroPython2016a/Examples/Session07/html_render/test_html_output2.html'
    assert cmp(f1path, f2path, shallow=False)

#Test part 3
def test_html3():
    f1path = 'test_html_output3.html'    
    f2path = '/home/johnr_000/py101/IntroPython2016a/Examples/Session07/html_render/test_html_output3.html'
    assert cmp(f1path, f2path, shallow=False)

#Test part 4
def test_html4():
    f1path = 'test_html_output4.html'    
    f2path = '/home/johnr_000/py101/IntroPython2016a/Examples/Session07/html_render/test_html_output4.html'
    assert cmp(f1path, f2path, shallow=False)

#Test part 5
def test_html5():
    f1path = 'test_html_output5.html'    
    f2path = '/home/johnr_000/py101/IntroPython2016a/Examples/Session07/html_render/test_html_output5.html'
    assert cmp(f1path, f2path, shallow=False)


#Test part 5
def test_html6():
    f1path = 'test_html_output6.html'    
    f2path = '/home/johnr_000/py101/IntroPython2016a/Examples/Session07/html_render/test_html_output6.html'
    assert cmp(f1path, f2path, shallow=False)

