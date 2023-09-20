class Coffee:
    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if hasattr(self, "name"):
            raise Exception("cannot change the name of coffee")
        elif isinstance(name, str) and len(name) >=3:
            self._name = name
        else:
            raise Exception("Name must be a string and greater than 2 characters")
   
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        return sum([order.price for order in self.orders()]) / len(self.orders())

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception("no") 
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price):
       return Order(self, coffee, price)
    @classmethod
    def most_aficionado(cls, coffee):
        coffee_orders = [order for order in Order.all if order.coffee == coffee]
        if len(coffee_orders) == 0:
            return None

        max_total = 0
        most_afficiando = [1]

        for order in coffee_orders:
            print(order.price)
            curr_customer = order.customer
            curr_cust_sum = sum([order.price for order in coffee_orders if order.customer == curr_customer])
            if curr_cust_sum > max_total:
                max_total = curr_cust_sum
                most_afficiando.clear()
                most_afficiando.append(curr_customer)
        return most_afficiando[0]
    
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price):
        if hasattr(self, "price"):
            print("Cannot change price of order")
        elif isinstance(price, float) and 1.0 <= price <=10.0:
            self._price = price
    @property
    def customer(self):
        return self._customer
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            print("customer must be of the class Customer")
    @property
    def coffee(self):
        return self._coffee
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee 
    