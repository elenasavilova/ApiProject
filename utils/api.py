import json
import sys
sys.path.append("C:\\Users\\esavilova\\PycharmProjects\\ApiProject\\utils")

from http_method import HttpMethod

base_url = "http://rahulshettyacademy.com"
key = "?key=qaclick123"

"""Методы для тестирования Google maps api"""


class GoogleMapsApi:

    @staticmethod
    def create_new_location():
        """Метод для создания новой локации"""

        post_resourse = "/maps/api/place/add/json"  # путь к ресурсу метода post
        post_url = base_url + post_resourse + key
        print(post_url)

        json_body = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        result_post = HttpMethod.post(url=post_url, body=json_body)
        print(result_post.json())
        print(result_post.status_code)
        return result_post

    @staticmethod
    def get_location(place_id):
        """Метод для проверки созданной локации"""
        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)

        result_get = HttpMethod.get(get_url)
        print(result_get.text)
        return result_get

