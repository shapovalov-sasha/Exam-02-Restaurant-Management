class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Meal(MenuItem):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price)
        self.ingredients = ingredients


class Drink(MenuItem):
    def __init__(self, name, price, served_cold):
        super().__init__(name, price)
        self.served_cold = served_cold


class Order:
    def __init__(self, table_name):
        self.table_name = table_name
        self.items = []

    def add_item(self, item):
        # TODO 1:
        # Add the item to self.items.
        self.items.append(item) ## adaug produsul in lista

    def calculate_subtotal(self):
        # TODO 2:
        # Return the sum of all item prices in this order.
        total = 0 #pornesc totalul de la 0
        for item in self.items: # trec prin fiecare produs din comanda
            total += item.price #adun pretul produsului la suma
        return total # returnez suma finala

    def calculate_total(self):
        # TODO 3:
        # Meals get a 9% VAT.
        # Drinks get a 19% VAT.
        # Return the final total.
        total = 0 #pornesc totalul de la 0
        for item in self.items: #trec prin fiecare produs din comanda
            if isinstance(item, Meal): # verific daca produsul e mancare
                total = total + item.price * 1.09 #adaug pretul cu TVA 9%
            elif isinstance(item, Drink): #verific daca produsul e bautura
                total = total + item.price * 1.19  #adaug pretul cu TVA 19%
        return total # returnez totalul cu TVA


class Kitchen:
    def __init__(self, inventory):
        self.inventory = inventory
        self.order_queue = []

    def add_order(self, order):
        # TODO 4:
        # Add the order to the end of the queue.
        self.order_queue.append(order) #pun comanda la finalul cozii

    def prepare_next_order(self):
        # TODO 5:
        # 1. If the queue is empty, print a message and return None.
        # 2. Remove the oldest order from the queue.
        # 3. For each Meal in the order, subtract 1 from inventory
        #    for every ingredient it uses.
        # 4. If an ingredient drops below 0, print a warning.
        # 5. Print that the order is ready and return the order.
        if len(self.order_queue) == 0:  # verific daca coada de comenzi e goala
            print(f"No orders in queue.") #afisez ca nu sunt comenzi
            return None #ies din functie fara sa returnez o comanda

        order = self.order_queue.pop(0) #scot cea mai veche comanda din coada (FIFO)

        for item in order.items: #trec prin fiecare produs din comanda
            if isinstance(item, Meal): #verific daca produsul e mancare
                for ingredient in item.ingredients: # trec prin fiecare ingredient al mancarii
                    self.inventory[ingredient] = self.inventory.get(ingredient, 0) - 1 #scad 1 din stocul ingredientului
                    if self.inventory[ingredient] < 0: #verific daca stocul a scazut sub 0
                        print(f"Warning: {ingredient} is below 0 !") #afisez avertisment pentru ingredient

        print(f"Order for {order.table_name} is ready.") # anunt ca a fost pregatita comanda pentru masa respectiva
        return order #returnez comanda pregatita

    def show_inventory(self):
        print("\nCurrent inventory:")
        for name, amount in self.inventory.items():
            print(f"- {name}: {amount}")


def count_item_names(orders):
    # OPTIONAL TASK:
    # Return a dictionary counting how many times each item name appears.
    counts = {}
    for order in orders: # trec prin fiecare comanda din lista
        for item in order.items: #trec prin fiecare produs din comanda
            if item.name in counts: #verific daca produsul exista deja in dictionar
                counts[item.name] += 1 #cresc numarul aparitiilor cu 1
            else: #daca produsul nu aparea
                counts[item.name] = 1 #il adaug in dictionar cu valoarea 1
    return counts


def print_story_setup(menu_items, inventory):
    print("=== County Training Center Canteen ===")
    print("The lunch break has started, and the canteen queue is growing.\n")
    print("Starter menu:")
    for item in menu_items:
        print(f"- {item.name}: {item.price} lei")

    print("\nStarter inventory:")
    for name, amount in inventory.items():
        print(f"- {name}: {amount}")


def print_checklist():
    print("\nFinish the TODOs, then test these checks:")
    print("1. An order should keep every item that you add.")
    print("2. calculate_subtotal() should add base prices only.")
    print("3. calculate_total() should apply the correct tax by item type.")
    print("4. The kitchen should prepare orders in FIFO order.")
    print("5. Meal ingredients should reduce the inventory correctly.")
    print("6. Optional: count_item_names() should build a frequency dictionary.")


def run_quick_checks():
    soup = Meal("Vegetable Soup", 20, ["carrots", "potatoes"])
    tea = Drink("Black Tea", 10, False)
    order = Order("Table 3")
    order.add_item(soup)
    order.add_item(tea)

    kitchen = Kitchen({"carrots": 2, "potatoes": 1})
    kitchen.add_order(order)

    # What is 'assert'?
    # 'assert' is a testing tool. It evaluates the expression next to it.
    # If the expression is True (e.g., your calculate_subtotal() actually returns 30), it passes silently.
    # If it is False, it crashes with an AssertionError. This ensures your math is perfectly correct!
    assert order.calculate_subtotal() == 30
    assert round(order.calculate_total(), 2) == 33.7
    prepared = kitchen.prepare_next_order()
    assert prepared is order
    assert kitchen.inventory["carrots"] == 1


def main():
    starting_inventory = {
        "bread": 6,
        "cheese": 4,
        "tomatoes": 5,
        "tea_bags": 8,
    }

    sandwich = Meal(
        "Cheese Sandwich",
        18,
        ["bread", "cheese", "tomatoes"],
    )
    salad = Meal("Tomato Salad", 14, ["tomatoes", "tomatoes"])
    tea = Drink("Tea", 8, False)

    starter_menu = [sandwich, salad, tea]

    print_story_setup(starter_menu, starting_inventory)
    print_checklist()
    print("\nAfter finishing the TODOs, run run_quick_checks() to self-test.")


if __name__ == "__main__":
    main()
    run_quick_checks() # rulez testul
