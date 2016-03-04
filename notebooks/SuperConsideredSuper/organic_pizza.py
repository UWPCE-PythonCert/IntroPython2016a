# organic_pizza.py

from pizza import DoughFactory, Pizza


class OrganicDoughFactory(DoughFactory):
    def get_dough(self):
        return "pure untreated wheat dough"


class OrganicPizza(Pizza, OrganicDoughFactory):
    pass


if __name__ == '__main__':
    my_pie = OrganicPizza()
    my_pie.order_pizza('pepperoni', 'shrooms')
