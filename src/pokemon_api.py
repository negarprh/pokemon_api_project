import requests
from typing import Dict, Any


def get_pokemon(name: str) -> Dict[str, Any]:  # Type annotations
    """
    Get information about a specific Pokemon

    Args:
        name (str): Name of the Pokemon

    Returns:
        Dict[str, Any]: Pokemon data or error message
    """
    base_url = "https://pokeapi.co/api/v2"

    try:
        response = requests.get(f"{base_url}/pokemon/{name.lower()}")
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {e}"}


def format_pokemon_info(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Format raw Pokemon data into a cleaner structure

    Args:
        data (Dict[str, Any]): Raw Pokemon data

    Returns:
        Dict[str, Any]: Formatted Pokemon data
    """
    if "error" in data:
        return data

    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "abilities": [ability["ability"]["name"]
                      for ability in data["abilities"]],
        "types": [type_info["type"]["name"]
                  for type_info in data["types"]]
    }


if __name__ == "__main__":
    # Example usage
    pokemon_name = input("Enter a Pokemon name: ")
    pokemon_data = get_pokemon(pokemon_name)
    formatted_data = format_pokemon_info(pokemon_data)

    for key, value in formatted_data.items():
        print(f"{key.title()}: {value}")