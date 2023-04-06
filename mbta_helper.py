import urllib.request
import json
from pprint import pprint
from config import MAPBOX_TOKEN, MBTA_API_KEY


def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode("utf-8")
        response_data = json.loads(response_text)
        # pprint(response_data)
        return response_data


def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    place_name = place_name.replace(" ", "+") + ",Boston,MA"
    MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
    url = f"{MAPBOX_BASE_URL}/{place_name}.json?access_token={MAPBOX_TOKEN}"
    response_data = get_json(url)
    longitude, latitude = response_data["features"][0][
        "center"
    ]  # coordinates are longitude then latitude
    return latitude, longitude


def get_nearest_station(
    latitude: str, longitude: str, sortby="distance", radius="0.01"
) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    MBTA_BASE_URL = "https://api-v3.mbta.com/stops"
    MBTA_url = f"{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&sort={sortby}&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}&radius%5D={radius}"
    # pprint(get_json(MBTA_url)) #: list
    data = get_json(MBTA_url)["data"][0]  #: dict
    # pprint(data)
    station = data["attributes"]["name"]
    # print(station)
    wheelchair_access = data["attributes"]["wheelchair_boarding"]
    # if wheelchair_access == 1:
    #     wheelchair_access = "Yes"
    # else:
    #     wheelchair_access = "No"
    wheelchair_access = "Yes" if wheelchair_access == 1 else "No"
    return station, wheelchair_access


def get_nearest_station_coor(
    place_name: str, sortby="distance", radius="0.01"
) -> tuple[str, str]:
    """
    Given latitude and longitude strings, return a (latitude, longitude) tuple for the nearest MBTA station to the given current coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    latitude, longitude = get_lat_long(place_name)
    MBTA_BASE_URL = "https://api-v3.mbta.com/stops"
    MBTA_url = f"{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}&radius%5D={radius}"
    # pprint(get_json(MBTA_url)) #: list
    data = get_json(MBTA_url)["data"][0]  #: dict
    pprint(data)
    station_latitude = data["attributes"]["latitude"]
    station_longitude = data["attributes"]["longitude"]
    return station_latitude, station_longitude


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    place_name = place_name.replace(" ", "+")
    lat, long = get_lat_long(place_name)
    return get_nearest_station(str(lat), str(long))


def main():
    """
    Testing of all the functions here.
    """
    # MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
    # query = "Babson+College"
    # url = f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}'
    # # url='https://api.mapbox.com/geocoding/v5/mapbox.places/Boston.json?access_token=pk.eyJ1IjoiYWJieXRqaWUiLCJhIjoiY2xnMDB1cGg3MTJwNTNlbWsyM2N5Zjc1ZyJ9.MuR9ei396i_ZGyZ43G6GvQ'

    # """
    # Hardcode: Kept getting "bad request" error, but then requested a new mapbox token without limit to url, attempted hard code
    # "Babson%College" 400 Error: Bad Request - the request could not be satisfied
    # """

    # """
    # Get Latitude and Longitude Tuples
    # """
    # Home = get_lat_long('Congress Street Boston')
    # print(Home)
    # # print(type(Home)) #tuple
    # # coordinates: (42.35188, -71.04957)

    """
    Get the name of nearest station
    """
    # Gables_lat = 42.34845515783725
    # Gables_long = -71.04221613687264
    # print(get_nearest_station(Gables_lat, Gables_long))

    # NS_latitude, NS_longitude = get_lat_long('Newbury Street')
    # station = get_nearest_station(NS_latitude, NS_longitude)
    # print(station)

    # print(find_stop_near('Newbury Street'))
    # get_nearest_station_coor('newbury street')
    print(find_stop_near("newbury street"))


if __name__ == "__main__":
    main()
