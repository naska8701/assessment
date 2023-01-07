from fastapi import FastAPI
import random

app = FastAPI()

# Keep track of the last 10 API calls made to the server
api_calls = []

@app.get("/jumble/{word}")
def jumble_word(word: str):
    # Shuffle the characters in the word randomly
    word = list(word)
    random.shuffle(word)
    jumbled_word = "".join(word)

    # Add this API call to the list of calls
    api_calls.append({"api": "/jumble", "payload": word})
    # Keep the list at a maximum of 10 items
    api_calls[-10:]

    return {"jumbled_word": jumbled_word}

@app.get("/audit")
def get_api_calls():
    return {"api_calls": api_calls}
