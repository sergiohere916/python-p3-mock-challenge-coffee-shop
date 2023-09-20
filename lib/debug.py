#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")
    coffee1 = Coffee("black")
    coffee2 = Coffee("latte")
    coffee3 = Coffee("iced")
    serg = Customer("Sergio")
    eman = Customer("Eman")
    order1 = Order(serg, coffee1, 5.0)
    order2 = Order(serg, coffee1, 7.0)
    order3 = Order(eman, coffee1, 10.0)
    print(Customer.most_aficionado(coffee1))


    ipdb.set_trace()
