import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def fetch_data(animal_name):
    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    # Fetch the API key from the environment variables
    api_key = os.getenv("API_KEY")


    headers = {
        "X-Api-Key": api_key
    }

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()

        if response.json():
            return response.json()

        # Return an empty list if no data is found
        else:
            return []

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []
