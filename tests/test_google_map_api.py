import sys
sys.path.append("C:\\Users\\esavilova\\PycharmProjects\\ApiProject\\utils")

from requests import Response
from api import GoogleMapsApi


class TestCreateNewLocation:

    def test_add_location(self):

        print("Метод POST")
        result_post = GoogleMapsApi.create_new_location()
        # place_id = result_post.json().get('place_id')
        # print(place_id)

        # print("Метод GET")
        # result_get = GoogleMapsApi.get_location(place_id)

cla_obj = TestCreateNewLocation()
cla_obj.test_add_location()