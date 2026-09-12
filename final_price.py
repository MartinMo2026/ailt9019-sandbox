"""Worked Example 3 · Write and test a function.

Run me with: python final_price.py
"""


def final_price(price, discount):
    """Return the discounted price.

    `price` is the original amount; `discount` is a fraction
    between 0 and 1 (e.g. 0.2 means 20% off).
    """
    return price * (1 - discount)


if __name__ == "__main__":
    # Test 1: $100 with a 20% discount -> $80.0
    print("Test 1: $100 with 20% off ->", final_price(100, 0.2))

    # Test 2: $50 with no discount (discount = 0) -> $50.0
    print("Test 2: $50 with 0% off  ->", final_price(50, 0))