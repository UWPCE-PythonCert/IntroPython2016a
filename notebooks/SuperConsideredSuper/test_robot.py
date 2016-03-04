# test_robot.py

from robot import Robot, CleaningRobot


class MockBot(Robot):

    def __init__(self):
        self.tasks = []

    def fetch(self, tool):
        self.tasks.append("fetching {}".format(tool))

    def move_forward(self, tool):
        self.tasks.append("forward {}".format(tool))

    def move_backward(self, tool):
        self.tasks.append("backward {}".format(tool))

    def replace(self, tool):
        self.tasks.append("replace {}".format(tool))


class MockedCleaningRobot(CleaningRobot, MockBot):
    pass


def test_clean():
    t = MockedCleaningRobot()
    t.clean('mop')
    expected = (
        ['fetching mop'] +
        ['forward mop', 'backward mop'] * 3 +
        ['replace mop']
    )
    assert t.tasks == expected


if __name__ == '__main__':
    t = MockedCleaningRobot()
    t.clean('broom')
