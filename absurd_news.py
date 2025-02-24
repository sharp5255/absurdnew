
### Код скрипта (`absurd_news.py`)

```python
import random
import sys

# Lists of words to combine
nouns = ["cat", "pigeon", "toaster", "croissant", "penguin", "cloud", "grandma"]
verbs = ["stole", "launched", "hijacked", "organized", "demanded", "befriended", "chased"]
locations = ["Tokyo", "Paris", "New York", "Lviv", "Kyiv", "London", "Sydney"]
details = [
    "to escape a local bakery",
    "to impress the Eiffel Tower",
    "to confuse tourists",
    "to avoid rush hour",
    "to join a secret club",
    "to demand a salary raise",
    "to win a dance competition"
]

def generate_headline(city=None):
    # Use provided city or pick a random one
    location = city if city else random.choice(locations)
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    detail = random.choice(details)
    
    # Construct the headline
    headline = f"In {location}, a {noun} {verb} a {random.choice(nouns)} {detail}!"
    return headline

def main():
    # Check if a custom city is provided via command line
    if len(sys.argv) > 1:
        custom_city = sys.argv[1]
        print(generate_headline(custom_city))
    else:
        print(generate_headline())

if __name__ == "__main__":
    main()
