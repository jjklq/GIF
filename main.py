import requests

def search_gifs(search_query):
   
    api_key = 'p0WB6gK7OYTgXogR5ePWRqxyuLLpjOBO'
    base_url = 'https://api.giphy.com/v1/gifs/search'
    params = {
        'q': search_query,
        'api_key': api_key,
        'limit': 5  
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        for gif in data['data']:
            gif_url = gif['images']['original']['url']
            print(gif_url)

    except requests.exceptions.RequestException as e:
        print(f"Произошла ошибка при запросе к API Giphy: {e}")

if __name__ == "__main__":
    search_word = input("Введите слово для поиска GIF-изображений: ")
    search_gifs(search_word)
