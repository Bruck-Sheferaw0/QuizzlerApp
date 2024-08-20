import requests


def get_questions():
    start = requests.get(url="https://opentdb.com/api.php?amount=15&difficulty=medium&type=boolean")
    start.raise_for_status()
    return start.json()['results']

question_data = get_questions()



