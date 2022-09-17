import json

with open("languages/english.json", "r") as file:
    LANGUAGE = json.loads(file.read())

def score(message):
    # used for ranking cypher breaks (sorting the list in order of probability)
    score = 0

    # + points for each common word in the cypher
    for word in LANGUAGE["common words"]:
        if f" {word} " in message:
            score += 1

    return score