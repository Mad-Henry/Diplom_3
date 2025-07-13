import allure
import string
import random
import requests
from URLs import BASE_URL, CREATE_USER_URL, DELETE_USER_URL


class HelpersMethods:


    @staticmethod
    @allure.step('Генерация строки')
    def generate_string(length):
        letters = string.ascii_lowercase
        gen_str = ''.join(random.choice(letters) for i in range(length))
        return gen_str


    @staticmethod
    @allure.step('Генерация email')
    def generate_email():
        gen_email = f'mad-henry-{HelpersMethods.generate_string(3)}@yandex.ru'
        return gen_email


    @staticmethod
    @allure.step('Генерация кредов (email, password, name)')
    def generate_creds():
        gen_email = f'"mad-henry-{HelpersMethods.generate_string(3)}@yandex.ru"'
        gen_password = f'"Mad-Henry-{HelpersMethods.generate_string(3)}-777"'
        gen_name = f'"mad-henry-{HelpersMethods.generate_string(5)}"'
        creds = {
            "email": f'{gen_email}',
            "password": f'{gen_password}',
            "name": f'{gen_name}'
                    }
        return creds
    

    @staticmethod
    def create_user(payload):
        response = requests.post(BASE_URL + CREATE_USER_URL, data=payload)
        return response.json(), response.status_code


    @staticmethod
    def delete_user(headers):
        response = requests.delete(BASE_URL + DELETE_USER_URL, headers=headers)
        return response.json(), response.status_code
