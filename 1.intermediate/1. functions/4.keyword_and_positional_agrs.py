""" Named(keyword) and Unnamed(positional) arguments """

def current_price(*price, discount=0): 
    return sum(price)*(1-(discount/100))


print(current_price(100, 200, 300)) 
print(current_price(100, 200, 300, discount=10)) # Named argument


def current_price(*price, discount=0, **details):
    total = sum(price) * (1 - discount / 100)

    print("Item details:", details)
    return total


print(
    current_price(
        100, 200, 300,
        discount=10,
        name="Laptop bundle",
        category="Electronics"
    )
)