import sys
sys.path.append("C:\\Users\\uaaar\\Лена. Обучение\\ApiProject\\utils")

from api import GoogleMapsApi
from asserts import Asserts


class TestCreatePlace:
    """Класс содержащий тест по работе с локацией"""

    def test_create_new_location(self):
        """Тест по созданию, изменние и удаление новой локации"""

        print("Метод POST")
        result_post = GoogleMapsApi.create_new_place()
        place_id = result_post.json().get('place_id')
        print(place_id)
        Asserts.assert_status_code(result_post, 200)
        Asserts.assert_field_value(result_post, "status", "OK")


        print("Метод GET")
        get_result = GoogleMapsApi.get_new_location(place_id)
        Asserts.assert_status_code(get_result, 200)
        Asserts.assert_field_value(get_result, "address", "29, side layout, cohen 09")


        print("Метод PUT")
        put_result = GoogleMapsApi.put_new_location(place_id)
        Asserts.assert_status_code(put_result, 200)
        Asserts.assert_json_fields(put_result, ["msg"])
        Asserts.assert_field_value(put_result, "msg", "Address successfully updated")

        print("Метод GET PUT")
        get_put_result = GoogleMapsApi.get_new_location(place_id)
        Asserts.assert_status_code(get_put_result, 200)

        print("Метод DELETE")
        delete_result = GoogleMapsApi.delete_new_location(place_id)
        Asserts.assert_status_code(delete_result, 200)
        Asserts.assert_json_fields(delete_result, ["status"])
        Asserts.assert_field_value(delete_result, "status", "OK")

        print("Метод GET DELETE")
        get_delete_result = GoogleMapsApi.get_new_location(place_id)
        Asserts.assert_status_code(get_delete_result, 404)
        Asserts.assert_json_fields(get_delete_result, ["msg"])
        Asserts.assert_field_value(get_delete_result, "msg", f"Get operation failed, looks like place_id  doesn't exists")
