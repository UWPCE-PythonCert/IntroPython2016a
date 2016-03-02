import html_render as hr
import pytest



def test_init_without_content():
    inst = hr.Element()
    assert (len(inst.data) == 0)


def test_init_with_string_content():
    inst = hr.Element('abcd')
    assert (inst.data[0] == 'abcd')


def test_append_string():
    inst = hr.Element('abcd')
    inst.append('efgh')
    assert (inst.data[0] == 'abcd' and
            inst.data[1] == 'efgh')


def test_append_incompatible_data():
    inst = hr.Element('abcd')
    with pytest.raises(ValueError):
        inst.append(1)

