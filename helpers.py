import random


class Helpers:

    login = f"Courier_Testikovich_{random.randint(1000, 10000)}"
    password = str(random.randint(1000, 99999))
    first_name = f"Courier_{random.randint(1, 999)}"

    correct_test_user_payload = {
        "login": "test_user_fayustov_ar",
        "password": "1234",
    }

    incorrect_test_user_payload = {
        "login": login,
        "password": password
    }
