import requests


"""Список HTTP методов"""

class HttpMethod:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod # статические методы можно вызывать где угодно
    def get(url):
        result = requests.get(url, headers=HttpMethod.headers, cookies=HttpMethod.cookie, verify=False)
        return result

    @staticmethod
    def post(url, body):
        result = requests.post(url, json=body, headers=HttpMethod.headers, cookies=HttpMethod.cookie)
        return result

    @staticmethod
    def put(url, body):
        result = requests.put(url, json=body, headers=HttpMethod.headers, cookies=HttpMethod.cookie)
        return result

    @staticmethod
    def delete(url, body):
        result = requests.delete(url, json=body, headers=HttpMethod.headers, cookies=HttpMethod.cookie)
        return result