import pytest


@pytest.mark.parametrize("search_query, expected_city", [
    ("Москва", "Москва"),
    ("Yjdujhjl", "Новгород"),
],
    ids=["ru","wrong_keyboard_layout"])
def test_selection_geo_search(main_page, search_query, expected_city):
    main_page.header.click_geo_button()
    main_page.geo_dropdown.search(search_query)
    main_page.geo_dropdown.select_city(expected_city)

    actual_geo = main_page.header.get_current_geo()
    assert expected_city in actual_geo, f"Ожидалось '{expected_city}', отображается '{actual_geo}'"


def test_selection_geo_scroll(main_page):
    main_page.header.click_geo_button()
    cities = main_page.geo_dropdown.get_available_cities()
    assert cities, "Список городов в дропдауне пуст"

    last_city = cities[-1]
    main_page.geo_dropdown.scroll_to_city(last_city)
    main_page.geo_dropdown.select_city(last_city)

    actual_geo = main_page.header.get_current_geo()
    assert last_city in actual_geo, f"Ожидалось '{last_city}', отображается '{actual_geo}'"


def test_clear_geo_input(main_page):
    text = "jkhjhgj"
    main_page.header.click_geo_button()
    main_page.geo_dropdown.search(text)
    main_page.geo_dropdown.clear_search_input()

    actual_text = main_page.geo_dropdown.get_text_in_input()
    assert actual_text == "", f"Поле поиска не очищено, отображается '{actual_text}'"

def test_close_geo_dropdown(main_page):
    main_page.header.click_geo_button()
    main_page.geo_dropdown.close_dropdown()

    assert main_page.geo_dropdown.is_closed(), "Дропдаун выбора города не закрылся"

# TODO: добавить тест на закрытие тапом мимо списка
