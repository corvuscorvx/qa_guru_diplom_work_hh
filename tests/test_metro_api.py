import allure
import requests
from jsonschema import validate
from schemas.metro_schema import all_city_metro_schema, city_metro_schema, error_metro_schema

BASE_URL = "https://" + "api." + "hh.ru"
HEADERS = {"HH-User-Agent": "QA_guru_student_api/1.0 (test_guru_api@mail.com)"}


@allure.epic("Справочники")
@allure.feature("Метро")
@allure.story("Фильтрация по метро")
@allure.title("Получить список городов в которых есть метро")
@allure.tag("Positive")
def test_get_all_metro_cities():
    with allure.step("Отправить GET-запрос на /metro"):
        response = requests.get(f"{BASE_URL}/metro", headers=HEADERS)

    with allure.step("Проверить, что статус-код ответа равен 200"):
        assert response.status_code == 200

    with allure.step("Провалидировать JSON-схему ответа"):
        body = response.json()
        validate(body, all_city_metro_schema)

    with allure.step("Проверить наличие Москвы (id=1) и Санкт-Петербурга (id=2) в списке"):
        assert len(body) > 0
        city_ids = [city["id"] for city in body]
        assert "1" in city_ids
        assert "2" in city_ids


@allure.epic("Справочники")
@allure.feature("Метро")
@allure.story("Фильтрация по метро")
@allure.title("Получение веток и станций метро для одного города")
@allure.tag("Positive")
def test_get_city_metro_stations():
    with allure.step("Отправить GET-запрос на /metro/2"):
        response = requests.get(f"{BASE_URL}/metro/2", headers=HEADERS)

    with allure.step("Проверить, что статус-код ответа равен 200"):
        assert response.status_code == 200

    with allure.step("Провалидировать JSON-схему ответа"):
        body = response.json()
        validate(body, city_metro_schema)

    with allure.step("Проверить данные города и наличие веток метро"):
        assert body["id"] == "2"
        assert body["name"] == "Санкт-Петербург"
        assert len(body["lines"]) > 0


@allure.epic("Справочники")
@allure.feature("Метро")
@allure.story("Фильтрация по метро")
@allure.title("Получить станции метро для несуществующего города")
@allure.tag("Negative")
def test_get_city_metro_negative():
    with allure.step("Отправить GET-запрос на /metro/999999"):
        response = requests.get(f"{BASE_URL}/metro/999999", headers=HEADERS)

    with allure.step("Проверить, что статус-код ответа равен 404"):
        assert response.status_code == 404

    with allure.step("Провалидировать JSON-схему ошибки"):
        body = response.json()
        validate(body, error_metro_schema)

    with allure.step("Проверить, что тип ошибки равен 'not_found'"):
        assert body["errors"][0]["type"] == "not_found"
