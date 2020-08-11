class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        return cls(store.name + " - franchise")

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return '{}, total stock price: {}'.format(store.name, int(store.stock_price()))

test = Store("Test")
amazon = Store("Amazon")
amazon.add_item("Keyboard", 160)
print(amazon.items)

print(Store.franchise(test))
print(Store.franchise(amazon))

print(amazon.store_details(amazon))