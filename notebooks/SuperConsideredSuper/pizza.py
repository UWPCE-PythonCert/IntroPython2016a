# pizza.py


class DoughFactory(object):

    def get_dough(self):
        return "insecticide treated wheat dough"


class Pizza(DoughFactory):

    def order_pizza(self, *toppings):
        print("Getting dough")

        # Uh oh, this is hard coded! What happens if we change the parent class?
        # dough = DoughFactory.get_dough(self)
        # dough = self.get_dough()
        dough = super().get_dough()

        print("Making pie with {}".format(dough))

        for topping in toppings:
            print("Adding {}".format(topping))


if __name__ == '__main__':
    my_pie = Pizza()
    my_pie.order_pizza('pepperoni', 'shrooms')
