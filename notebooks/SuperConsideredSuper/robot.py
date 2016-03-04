# robot.py

class Robot(object):

    def fetch(self, tool):
        print("Physical Movement: Fetching")

    def move_forward(self, tool):
        print("Physical Movement: Moving forward")

    def move_backward(self, tool):
        print("Physical Movement: Moving backward")

    def replace(self, tool):
        print("Physical Movement: Replacing")


class CleaningRobot(Robot):

    def clean(self, tool, times=3):
        super().fetch(tool)
        for _ in range(times):
            super().move_forward(tool)
            super().move_backward(tool)
        super().replace(tool)


if __name__ == '__main__':
    t = CleaningRobot()
    t.clean('broom')
