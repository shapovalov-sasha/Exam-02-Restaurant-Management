
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
        # TODO 1
        self.items.append(item)

    def calculate_subtotal(self):
        # TODO 2
        subtotal = 0

        for item in self.items:
            subtotal += item.price

        return subtotal

    def calculate_total(self):
        # TODO 3
        total = 0

        for item in self.items:
            if isinstance(item, Meal):
                total += item.price * 1.09
            elif isinstance(item, Drink):
                total += item.price * 1.19

        return total


class Kitchen:
    def __init__(self, inventory):
        self.inventory = inventory
        self.order_queue = []

    def add_order(self, order):
        # TODO 4
        self.order_queue.append(order)

    def prepare_next_order(self):
        # TODO 5
        if len(self.order_queue) == 0:
            print("The order queue is empty.")
            return None

        order = self.order_queue.pop(0)

        for item in order.items:
            if isinstance(item, Meal):
                for ingredient in item.ingredients:
                    if ingredient not in self.inventory:
                        self.inventory[ingredient] = 0

                    self.inventory[ingredient] -= 1

                    if self.inventory[ingredient] < 0:
                        print(f"Warning: Not enough {ingredient}!")

        print(f"Order for {order.table_name} is ready.")
        return order

    def show_inventory(self):
        print("\nCurrent inventory:")
        for name, amount in self.inventory.items():
            print(f"- {name}: {amount}")


def count_item_names(orders):
    # OPTIONAL TASK
    counts = {}

    for order in orders:
        for item in order.items:
            if item.name in counts:
                counts[item.name] += 1
            else:
                counts[item.name] = 1

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
    run_quick_checks()
    print("All quick checks passed!")
