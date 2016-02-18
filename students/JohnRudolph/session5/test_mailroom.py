
from mailroom import createDonors
from mailroom import actionPrompt

# test that # of donors generated in correct
def test_creatdonorslen():
    assert len(createDonors(5)) == 5

# test that # of donations for each donor is between 1-3
def test_creatdonorsdons():
    for n in createDonors(5):
        assert 1 <= len(n) <= 3
