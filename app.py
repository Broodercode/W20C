import json
import random
from flask import Flask, jsonify, request

app = Flask(__name__)

animals = ['lion', 'kitty', 'puppy', 'baby human', 'baby dinosaur', 'big dinosaur', 'ugly dinosaur', 'thinking dinosaur', 'owl', 'dead mouse', 'dead owl']
# animals = '{"animal": "lion", "animal": "kitty", "animal": "puppy"}'

@app.route('/')
def homepage():
    return "hello world"

@app.get('/animals')
def get_animals():
    aniLen = len(animals)
    randAnimal = random.randint(0, aniLen-1)
    Response = jsonify(animals[randAnimal])
    return Response

@app.post('/animals')
def post_animals():
    rData = json.loads(request.data)
    newAnimal = rData["animal"]
    animals.append(newAnimal)
    return 'Success!!!'

@app.patch('/animals')
def patch_animals():
    rData = json.loads(request.data)
    newAnimal = rData["new_animal"]
    oldAnimal = rData["old_animal"]
    for animal in animals:
        if animal == oldAnimal:
            index = animals.index(animal)
            animals[index] = newAnimal
    return "Patched Successfully"

@app.delete('/animals')
def delete_animals():
    rData = json.loads(request.data)
    deleted_animal = rData['animal']
    animals.remove(deleted_animal)
    return 'deleted successfully'