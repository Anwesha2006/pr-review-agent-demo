def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)


def get_discount(price, discount):
    # Bug: discount is added instead of subtracted
    return price + (price * discount / 100)


def find_maximum(numbers):
    return max(numbers)