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
        self.items.append(item)

    def calculate_subtotal(self):  
        # TODO 2:
        # Return the sum of all item prices in this order.
        subtotal = 0
        for item in self.items:
            subtotal += item.price
        return subtotal

    def calculate_total(self):
        # TODO 3:
        # Meals get a 9% VAT.
        # Drinks get a 19% VAT.
        # Return the final total.
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
        # TODO 4:
        # Add the order to the end of the queue.
        self.order_queue.append(order)

    def prepare_next_order(self):
        # TODO 5:
        # 1. If the queue is empty, print a message and return None.
        # 2. Remove the oldest order from the queue.
        # 3. For each Meal in the order, subtract 1 from inventory
        #    for every ingredient it uses.
        # 4. If an ingredient drops below 0, print a warning.
        # 5. Print that the order is ready and return the order.
        if len(self.order_queue) == 0:
            print(f"No orders in queue.")
            return None

        order = self.order_queue[0]
# Process each item from the order
        for item in order.items: 
            if isinstance(item, Meal):   # Only meals consume ingredients
                for ingredient in item.ingredients:   # Update inventory for each ingredient
                    self.inventory[ingredient] = self.inventory.get(ingredient, 0) -1
                    if self.inventory[ingredient] < 0:  # Warn if inventory becomes negative
                        print(f"Warning: {ingredient} is below 0 !")

        print(f"Order for {order.table_name} is ready.")
        return order

    def show_inventory(self):
        print("\nCurrent inventory:")
        for name, amount in self.inventory.items():
            print(f"- {name}: {amount}")


def count_item_names(orders):
    # OPTIONAL TASK:
    # Return a dictionary counting how many times each item name appears.
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
    run_quick_checks()


if __name__ == "__main__":
    main()