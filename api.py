import requests
from config import ENDPOINTS


def get_all_items():
    return requests.get(ENDPOINTS["inventory"]).json()


def get_item(material_id):
    return requests.get(f"{ENDPOINTS['inventory']}/{material_id}").json()


def create_item(data):
    return requests.post(ENDPOINTS["inventory"], json=data).json()


def replace_item(material_id, data):
    return requests.put(f"{ENDPOINTS['inventory']}/{material_id}", json=data).json()


def patch_item(material_id, data):
    return requests.patch(f"{ENDPOINTS['inventory']}/{material_id}", json=data).json()


def delete_item(material_id):
    res = requests.delete(f"{ENDPOINTS['inventory']}/{material_id}")
    return res.json()

def search_items(query):
    url = f"{ENDPOINTS['inventory']}/search"
    response = requests.get(url, params={"q": query})

    # 🔥 DEBUG HELP (optional but recommended)
    if response.status_code != 200:
        return {
            "error": response.status_code,
            "message": response.text
        }

    try:
        return response.json()
    except Exception:
        return {
            "error": "Invalid JSON response",
            "raw": response.text
        }
