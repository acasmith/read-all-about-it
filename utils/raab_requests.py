import requests
class Raab_Requests:
    base_url = "https://newsapi.org/v2/"
    urls = {
        "top_headlines": base_url + "top-headlines",
        "top_sources": base_url + "sources"
    }

    @staticmethod
    def make_request(request_type, params):
        url = Raab_Requests.urls[request_type]
        try:
            response = requests.get(url, params)
            response = response.json()  #formatting done here for convinience as all responses from this API are JSON.
            return response
        except requests.exceptions.RequestException as e:
            print(e)
            return None
        except ValueError as e: #Could not parse response as JSON
            print(e)
            return None
