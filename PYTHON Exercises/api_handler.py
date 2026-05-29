import requests

def get_weather():
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/todos/1",
            timeout=5
        )

        if response.status_code == 404:
            print("API Not Found")
            return

        data = response.json()

        print("Sample API Data")
        print("ID:", data.get("id"))
        print("Title:", data.get("title"))

    except requests.exceptions.RequestException:
        print("Network Error")

    except ValueError:
        print("Invalid JSON response")


get_weather()