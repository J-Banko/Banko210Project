import random

def get_random_quote():
    quotes = [
        "Believe you can and you're halfway there.",
        "You are stronger than you think.",
        "Dream big and dare to fail.",
        "Keep going. Everything you need will come to you.",
        "The best time to start was yesterday. The next best time is now."
    ]
    return random.choice(quotes)

def main():
    print("Here's your motivational quote:")
    print(get_random_quote())

if __name__ == "__main__":
    main()
