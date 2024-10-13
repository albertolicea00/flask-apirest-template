import random


def process_payment():
    success = random.choice([True, False])
    return "success" if success else "failure"
