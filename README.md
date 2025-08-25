# 🐍 Python Mini Projects

This repository contains three beginner-friendly Python projects designed to practice programming fundamentals such as loops, conditionals, functions, data handling, and working with APIs.

---

## 🎮 Hangman Game
A classic word-guessing game where the player must guess letters to reveal the hidden word before running out of attempts.

**Features:**
- Random word selection
- ASCII visuals for wrong guesses
- Keeps track of attempts
- Replay option

  **CODE**
--------------------------------------------------------------------------------------------
# Hangman in Python
import random
hangman_art = {0: ("   ",
                                   "   ",
                                   "   "),
                             1: (" o ",
                                   "   ",
                                   "   "),
                             2: (" o ",
                                   " | ",
                                   "   "),
                             3: (" o ",
                                   "/| ",
                                   "   "),
                             4: (" o ",
                                  "/|\\",
                                   "   "),
                              5: (" o ",
                                   "/|\\",
                                   "/  "),
                              6: (" o ",
                                   "/|\\",
                                   "/ \\")}

words = ("aardvark", "alligator", "alpaca", "ant", "anteater", "antelope", "ape", "armadillo", "baboon", "badger", "bat", "bear", "beaver", "bee", "bison", "boar", "buffalo", "butterfly", "camel", "capybara", "caribou", "cat", "caterpillar", "cattle", "chamois", "cheetah", "chicken", "chimpanzee", "chinchilla", "chough", "clam", "cobra", "cockroach", "cod", "coyote", "crab", "crane", "crocodile", "crow", "curlew", "deer", "dinosaur", "dog", "dogfish", "dolphin", "donkey", "dormouse", "dotterel", "dove", "dragonfly", "duck", "dugong", "dunlin", "eagle", "echidna", "eel", "eland", "elephant",  "elk", "emu", "falcon", "ferret", "finch", "fish", "flamingo", "fly", "fox", "frog", "gaur", "gazelle", "gerbil", "giraffe", "gnat", "gnu", "goat", "goldfinch", "goldfish", "goose", "gorilla", "goshawk", "grasshopper", "grouse", "guanaco", "gull", "hamster", "hare", "hawk", "hedgehog", "heron", "herring", "hippopotamus", "hornet", "horse", "human", "hummingbird", "hyena", "ibex", "ibis", "jackal", "jaguar", "jay", "jellyfish", "kangaroo", "kingfisher", "koala", "kookabura", "kouprey", "kudu", "lapwing", "lark", "lemur", "leopard", "lion", "llama", "lobster", "locust", "loris", "louse", "lyrebird", "magpie", "mallard", "manatee", "mandrill", "mantis", "marten", "meerkat", "mink", "mole", "mongoose", "monkey", "moose", "mosquito", "mouse", "mule", "narwhal", "newt", "nightingale", "octopus", "okapi", "opossum", "oryx", "ostrich", "otter", "owl", "ox", "oyster", "panda", "panther", "parrot", "partridge", "peafowl", "pelican", "penguin", "pheasant", "pig", "pigeon", "polar-bear", "pony", "porcupine", "porpoise", "quail", "quelea", "quetzal", "rabbit", "raccoon", "rail", "ram", "rat", "raven", "red-deer", "red-panda", "reindeer", "rhinoceros", "rook", "salamander", "salmon", "sand-dollar", "sandpiper", "sardine", "scorpion", "seahorse", "seal", "shark", "sheep", "shrew", "skunk", "snail", "snake", "sparrow", "spider", "spoonbill", "squid", "squirrel", "starling", "stingray", "stoat", "stork", "swallow", "swan", "tapir", "tarsier", "termite", "tiger", "toad", "trout", "turkey", "turtle", "viper", "vulture", "wallaby", "walrus", "wasp", "weasel", "whale", "wildcat", "wolf", "wolverine", "wombat", "woodcock", "woodpecker", "worm", "wren", "yak", "zebra")

def display_man(wrong_guesses):
    print("**********")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("**********")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False

if __name__ == "__main__":
    main()
    
-----------------------------------------------------------------------------------------

---


...........................................................................................................................................................
## 📈 Stock Portfolio Tracker
A simple tool to help track and manage stock investments.

**Features:**
- Add/remove stocks from a portfolio
- Fetch live stock prices (if API is integrated)
- Calculate total portfolio value & gains/losses
- Display portfolio performance in a clean format

  **CODE**
--------------------------------------------------------------------------------------------
# stock prices dictionary
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 135,
    "MSFT": 300
}

# Portfolio dictionary to store user stocks
portfolio = {}

# Taking input from user
while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").strip().upper()
    if stock == "DONE":
        break
    
    # If stock not in dictionary, ask user to add it
    if stock not in stock_prices:
        try:
            price = float(input(f"Stock {stock} not found. Enter current price for {stock}: "))
            stock_prices[stock] = price
            print(f"✅ Added {stock} with price ${price}")
        except ValueError:
            print("⚠ Invalid price. Try again.")
            continue
    
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("⚠ Please enter a valid number.")

# Calculate total investment value
total_value = 0
print("\n📊 Portfolio Summary:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_value += value
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")

print(f"\n💰 Total Investment Value = ${total_value}")
}

--------------------------------------------------------------------------------------




...........................................................................................................................................................
## 🤖 Basic Chatbot
A beginner-friendly chatbot that uses rule-based logic to respond to user inputs.

**Features:**
- Predefined responses to common questions
- Interactive text-based conversation
- Easy to extend with custom responses

**CODE**
------------------------------------------------------------------------
def chatbot():
    print("Hello! I'm ChatPy. Type 'bye' to exit.\n")
    
    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("ChatPy: Goodbye! Have a great day.")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("ChatPy: Hello! How can I help you?")
        elif "how are you" in user_input:
            print("ChatPy: I'm just a program, but I'm doing fine. Thanks!")
        elif "your name" in user_input:
            print("ChatPy: I'm ChatPy, your AI Friend!")
        elif "help" in user_input or "ask" in user_input:
            print("ChatPy:Hey I cant Help You at this Moment as i am just a basic Chatbot.")
        else:
            print("ChatPy:Sorry i am not trained to answer this as far now.")

# run the code
chatbot()
----------------------------------------------------------------------------

---

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone (https://github.com/SidraAriff/CodeAlpha_pythonprogramming.git)s
