import requests
from requests.exceptions import HTTPError


def get_device_info(server_uri, token, address):
    """Fetch device information from macaddress server"""
    BASE_URI = "{}/v1/?output=json&search={}".format(server_uri, address)

    headers = {"X-Authentication-Token": token}
    response = requests.get(BASE_URI, headers=headers)

    try:
        response.raise_for_status()
        return response.json()

    except HTTPError as e:
        raise SystemExit("Error: " + str(e))
