import pytest
import allure
import requests
from jsonschema import validate
from schemas.keyword_schema import keyword_search_schema, keyword_error_schema

pytestmark = [pytest.mark.api, pytest.mark.keyword]

BASE_URL = "https://" + "api." + "hh.ru"
HEADERS = {"HH-User-Agent": "QA_guru_student_api/1.0 (test_guru_api@mail.com)"}
ENDPOINT = '/suggests/vacancy_search_keyword'


@allure.epic("Поиск")
@allure.feature("Поисковые подсказки")
@allure.story("Поиск вакансии")
@allure.title("Отображение подсказок по ключевому слову на английском языке")
@allure.tag("Positive")
def test_search_keyword_english():
    params = {"text": "qa"}

    with allure.step(f"Отправить GET-запрос на {ENDPOINT} с параметрами {params}"):
        response = requests.get(BASE_URL + ENDPOINT, params=params, headers=HEADERS)

    with allure.step("Проверить, что статус-код ответа равен 200"):
        assert response.status_code == 200

    with allure.step("Провалидировать JSON-схему ответа"):
        body = response.json()
        validate(body, keyword_search_schema)

    with allure.step("Проверить, что список подсказок не пуст и первый элемент содержит 'qa'"):
        assert len(body["items"]) > 0
        assert "qa" in body["items"][0]["text"].lower()


@allure.epic("Поиск")
@allure.feature("Поисковые подсказки")
@allure.story("Поиск вакансии")
@allure.title("Отображение подсказок по ключевому слову на русском языке")
@allure.tag("Positive")
def test_search_keyword_russian():
    params = {"text": "тестировщик"}

    with allure.step(f"Отправить GET-запрос на {ENDPOINT} с параметрами {params}"):
        response = requests.get(BASE_URL + ENDPOINT, params=params, headers=HEADERS)

    with allure.step("Проверить, что статус-код ответа равен 200"):
        assert response.status_code == 200

    with allure.step("Провалидировать JSON-схему ответа"):
        body = response.json()
        validate(body, keyword_search_schema)

    with allure.step("Проверить, что список подсказок не пуст и первый элемент содержит 'тестировщик'"):
        assert len(body["items"]) > 0
        assert "тестировщик" in body["items"][0]["text"].lower()


@allure.epic("Поиск")
@allure.feature("Поисковые подсказки")
@allure.story("Поиск вакансии")
@allure.title("Отображение подсказок по некорректному запросу")
@allure.tag("Positive")
def test_search_keyword_incorrect_negative():
    params = {"text": "олрлврмдljkhklhjождвыл"}

    with allure.step(f"Отправить GET-запрос на {ENDPOINT} с параметрами {params}"):
        response = requests.get(BASE_URL + ENDPOINT, params=params, headers=HEADERS)

    with allure.step("Проверить, что статус-код ответа равен 200"):
        assert response.status_code == 200

    with allure.step("Провалидировать JSON-схему ответа"):
        body = response.json()
        validate(body, keyword_search_schema)

    with allure.step("Проверить, что список подсказок пуст"):
        assert len(body["items"]) == 0


@allure.epic("Поиск")
@allure.feature("Поисковые подсказки")
@allure.story("Поиск вакансии")
@allure.title("Отображение подсказок по короткому запросу")
@allure.tag("Positive")
def test_search_keyword_short_negative():
    params = {"text": "q"}

    with allure.step(f"Отправить GET-запрос на {ENDPOINT} с параметрами {params}"):
        response = requests.get(BASE_URL + ENDPOINT, params=params, headers=HEADERS)

    with allure.step("Проверить, что статус-код ответа равен 400"):
        assert response.status_code == 400

    with allure.step("Провалидировать JSON-схему ошибки"):
        body = response.json()
        validate(body, keyword_error_schema)

    with allure.step("Проверить наличие блока 'errors' в теле ответа"):
        assert "errors" in body


@allure.epic("Поиск")
@allure.feature("Поисковые подсказки")
@allure.story("Поиск вакансии")
@allure.title("Отображение подсказок без параметров")
@allure.tag("Positive")
def test_search_keyword_without_params_negative():
    with allure.step(f"Отправить GET-запрос на {ENDPOINT} без параметров"):
        response = requests.get(BASE_URL + ENDPOINT, headers=HEADERS)

    with allure.step("Проверить, что статус-код ответа равен 400"):
        assert response.status_code == 400

    with allure.step("Провалидировать JSON-схему ошибки"):
        body = response.json()
        validate(body, keyword_error_schema)

    with allure.step("Проверить наличие блока 'errors' в теле ответа"):
        assert "errors" in body
