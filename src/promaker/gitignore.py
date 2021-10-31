import requests


def get_gitignore(*ignores):
    items = ",".join(ignores)
    response = requests.get(f"https://www.toptal.com/developers/gitignore/api/{items}")
    return response.text
