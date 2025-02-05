# fetch_reviews.py
import requests
from config import GOOGLE_API_KEY, PLACE_ID

def fetch_google_reviews():
    url = f"https://maps.googleapis.com/maps/api/place/details/json?placeid={PLACE_ID}&fields=review&key={GOOGLE_API_KEY}"
    reviews = []
    try:
        # Make the API request
        response = requests.get(url)
        response_data = response.json()

        # Debugging: Print the entire response for inspection
        print("API Response:", response_data)

        if response_data.get('status') == 'OK':
            reviews_data = response_data.get('result', {}).get('reviews', [])
            reviews.extend(reviews_data)

        # Handle pagination if there are more than 5 reviews (Google API paginates results)
        while 'next_page_token' in response_data:
            next_page_token = response_data['next_page_token']
            url = f"https://maps.googleapis.com/maps/api/place/details/json?placeid={PLACE_ID}&fields=review&key={GOOGLE_API_KEY}&pagetoken={next_page_token}"
            response = requests.get(url)
            response_data = response.json()

            # Debugging: Print the pagination response for inspection
            print("Next Page Response:", response_data)

            if response_data.get('status') == 'OK':
                reviews_data = response_data.get('result', {}).get('reviews', [])
                reviews.extend(reviews_data)

        # Limit to the first 500 reviews
        return reviews[:50]

    except Exception as e:
        print(f"Error fetching reviews: {e}")
        return []
