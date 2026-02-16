### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        for item in ingredients:
            if ingredients[item] > self.machine_resources[item]:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        print("Insert coins please.")
        dollars = int(input("how many dollars do you have? "))
        halves = int(input("how many halves do you have? "))
        quarters = int(input("how many quarters do you have? "))
        nickles = int(input("how many nickles do you have? "))

        total = (dollars * 1.0 + halves * 0.5 + quarters * 0.25 + nickles * 0.05)
        return total

    def transaction_result(self, coins, cost):
        if coins < cost:
            print(f"Sorry, there is not enough money.")
            return False
        change = round(coins - cost, 2)
        print(f"You earned {change} dollars.")
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"{sandwich_size} sandwiches were made.")

    def report(self):
        print(f"Bread: {self.machine_resources['bread']} slice(s)")
        print(f"Ham: {self.machine_resources['ham']} slice(s)")
        print(f"Cheese: {self.machine_resources['cheese']} pound(s)")

### Make an instance of SandwichMachine class and write the rest of the codes ###

machine = SandwichMachine(resources)

while True:
    choice = input("Choose your order. (small/ medium/ large/ off/ report): ").lower()

    if choice == "off":
       break

    if choice == "report":
        machine.report()
        continue

    if choice in recipes:
        sandwich = recipes[choice]
        if not machine.check_resources(sandwich["ingredients"]):
            continue

        payment = machine.process_coins()
        if machine.transaction_result(payment, sandwich["cost"]):
            machine.make_sandwich(choice, sandwich["ingredients"])
