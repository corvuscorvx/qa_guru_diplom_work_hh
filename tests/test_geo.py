import pytest
import allure

@allure.epic("Геолокация")
@allure.feature("Изменение геолокации")
@allure.story("Поиск")
@allure.title("Поиск города по тексту ({search_query})")
@allure.tag("Positive")
@pytest.mark.parametrize("search_query, expected_substring", [
    ("Уфа", "уфа"),
    ("А", "а"),
    ("Yjdujhjl", "новгород")
],
    ids=["ru", "one_symbol", "wrong_keyboard_layout"])
def test_geo_search_positive(main_page, search_query, expected_substring):
    main_page.header.click_geo_button()
    main_page.geo_dropdown.search(search_query)

    results = main_page.geo_dropdown.wait_for_search_results(expected_substring)

    assert len(results) > 0, f"По запросу '{search_query}' список результатов пуст"
    assert all(expected_substring in card.lower() for card in results), f"Найдены нерелевантные карточки по запросу '{search_query}': {results}"


@allure.epic("Геолокация")
@allure.feature("Изменение геолокации")
@allure.story("Поиск")
@allure.title("Поиск несуществующего города отображает заглушку")
@allure.tag("Negative")
def test_geo_search_negative(main_page):
    main_page.header.click_geo_button()
    main_page.geo_dropdown.search("ловрблми")

    actual_message = main_page.geo_dropdown.get_empty_search_message()
    assert actual_message == "Не нашли такого города", f"Ожидалось сообщение 'Не нашли такого города', получено '{actual_message}'"


@allure.epic("Геолокация")
@allure.feature("Изменение геолокации")
@allure.story("Поиск")
@allure.title("Скролл")
@allure.tag("Positive")
def test_geo_selection_scroll(main_page):
    main_page.header.click_geo_button()
    cities = main_page.geo_dropdown.get_available_cities()
    assert cities, "Список городов в дропдауне пуст"

    last_city = cities[-1]
    main_page.geo_dropdown.scroll_to_city(last_city)
    main_page.geo_dropdown.select_city(last_city)

    actual_geo = main_page.header.get_current_geo()
    assert last_city in actual_geo, f"Ожидалось '{last_city}', отображается '{actual_geo}'"


@allure.epic("Геолокация")
@allure.feature("Изменение геолокации")
@allure.story("Поиск")
@allure.title("Очистка поля поиска")
@allure.tag("Positive")
def test_geo_clear_input(main_page):
    text = "jkhjhgj"
    main_page.header.click_geo_button()
    main_page.geo_dropdown.search(text)
    main_page.geo_dropdown.clear_search_input()

    actual_text = main_page.geo_dropdown.get_text_in_input()
    assert actual_text == "", f"Поле поиска не очищено, отображается '{actual_text}'"


@allure.epic("Геолокация")
@allure.feature("Изменение геолокации")
@allure.story("Поиск")
@allure.title("Закрыть выпадающий список")
@allure.tag("Positive")
def test_geo_close_dropdown(main_page):
    main_page.header.click_geo_button()
    main_page.geo_dropdown.close_dropdown()

    assert main_page.geo_dropdown.is_closed(), "Дропдаун выбора города не закрылся"
