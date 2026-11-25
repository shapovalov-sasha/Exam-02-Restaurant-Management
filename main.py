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
        self.items.append(item)

    def calculate_subtotal(self):
        subtotal = 0
        for item in self.items:
            subtotal += item.price
        return subtotal

    def calculate_total(self):
        total = 0
        for item in self.items:
            if isinstance(item, Meal):
                total += item.price * 1.09
            elif isinstance(item, Drink):
                total += item.price * 1.19
            else:
                total += item.price
        return round(total, 2)


class Kitchen:
    def __init__(self, inventory):
        self.inventory = inventory
        self.order_queue = []

    def add_order(self, order):
        self.order_queue.append(order)

    def prepare_next_order(self):
        if not self.order_queue:
            print("Nu exista comenzi in coada.")
            return None

        order = self.order_queue.pop(0)  # FIFO

        for item in order.items:
            if isinstance(item, Meal):
                for ingredient in item.ingredients:
                    self.inventory[ingredient] = self.inventory.get(ingredient, 0) - 1
                    if self.inventory[ingredient] < 0:
                        print(f"Avertisment: '{ingredient}' a scazut sub 0!")

        print(f"Comanda pentru {order.table_name} este gata.")
        return order

    def show_inventory(self):
        print("\nCurrent inventory:")
        for name, amount in self.inventory.items():
            print(f"- {name}: {amount}")


def count_item_names(orders):
    counts = {}
    for order in orders:
        for item in order.items:
            counts[item.name] = counts.get(item.name, 0) + 1
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

    assert order.calculate_subtotal() == 30
    assert round(order.calculate_total(), 2) == 33.7
    prepared = kitchen.prepare_next_order()
    assert prepared is order
    assert kitchen.inventory["carrots"] == 1


def run_readme_example():
    salata = Meal("Salata de Rosii", 10, ["tomatoes", "tomatoes"])
    apa = Drink("Apa", 5, True)

    order = Order("Masa 1")
    order.add_item(salata)
    order.add_item(apa)

    kitchen = Kitchen({"tomatoes": 5, "bread": 2})
    kitchen.add_order(order)

    assert order.calculate_subtotal() == 15
    assert order.calculate_total() == 16.85
    kitchen.prepare_next_order()
    assert kitchen.inventory["tomatoes"] == 3


def run_extra_checks():
    # FIFO
    o1, o2 = Order("A"), Order("B")
    kitchen = Kitchen({})
    kitchen.add_order(o1)
    kitchen.add_order(o2)
    assert kitchen.prepare_next_order() is o1
    assert kitchen.prepare_next_order() is o2
    assert kitchen.prepare_next_order() is None

    # Avertisment sub 0
    kitchen = Kitchen({"bread": 0})
    order = Order("C")
    order.add_item(Meal("Pain", 5, ["bread"]))
    kitchen.add_order(order)
    kitchen.prepare_next_order()
    assert kitchen.inventory["bread"] == -1

    # Bonus
    tea = Drink("Tea", 8, False)
    o3, o4 = Order("D"), Order("E")
    o3.add_item(tea)
    o4.add_item(tea)
    o4.add_item(Meal("Pain", 5, ["bread"]))
    assert count_item_names([o3, o4]) == {"Tea": 2, "Pain": 1}


def main():
    starting_inventory = {
        "bread": 6,
        "cheese": 4,
        "tomatoes": 5,
        "tea_bags": 8,
    }

    sandwich = Meal("Cheese Sandwich", 18, ["bread", "cheese", "tomatoes"])
    salad = Meal("Tomato Salad", 14, ["tomatoes", "tomatoes"])
    tea = Drink("Tea", 8, False)

    starter_menu = [sandwich, salad, tea]

    print_story_setup(starter_menu, starting_inventory)
    print_checklist()

    run_quick_checks()
    run_readme_example()
    run_extra_checks()
    print("\nToate verificarile au trecut!")


if __name__ == "__main__":
    main()