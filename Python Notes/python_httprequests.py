# In order to send HTTP requests and recieve responses we need the requests module
# We have to pip install it first (make sure you're in a virtual environment)
import requests

# UNlike othe rllanguages, we don't have to do things like set up some sort of
# HTTP client object, we don't need a model for the return, etc. We can just send the request and work with the response assuming it is a JSON

print("Enter a pokemon name or dex number:")
query = input()

found_pokemon = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")

print(found_pokemon.json())