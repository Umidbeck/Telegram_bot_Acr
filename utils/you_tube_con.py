import requests


async def you_tube(name):
    try:
        url = "https://simple-youtube-search.p.rapidapi.com/search"

        querystring = {"query": f"{name}", "safesearch": "false"}

        headers = {
            "X-RapidAPI-Host": "simple-youtube-search.p.rapidapi.com",
            "X-RapidAPI-Key": "bdfa1ef989msh3de9d39bc391f6fp109f47jsn55a496cc04a3"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        r = response.json()['results'][0]['url']
        return r
    except:
        text = 'You tube link topilmadi'
        return text
