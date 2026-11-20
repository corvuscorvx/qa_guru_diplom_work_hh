import allure

@allure.epic("Помощь и поддержка")
@allure.feature("Модальное окно помощи")
@allure.story("Закрытие окна")
@allure.title("Закрытие модального окна 'Нужна помощь?'")
@allure.tag("Positive")
def test_close_help_modal(main_page):
    main_page.header.click_help_button()
    main_page.help_modal.click_close_button()

    assert main_page.help_modal.is_closed(), "Модальное окно 'Нужна помощь?' не закрылось"


@allure.epic("Помощь и поддержка")
@allure.feature("Чат поддержки")
@allure.story("Открытие и закрытие")
@allure.title("Открытие чата с технической поддержкой из окна помощи")
@allure.tag("Positive")
def test_open_support_chat(main_page):
    main_page.header.click_help_button()
    main_page.help_modal.click_support_button()

    assert main_page.help_modal.is_closed(), "Модальное окно помощи не закрылось после перехода в чат"
    assert main_page.chat_widget.is_opened(), "Виджет 'Чат' не отобразился"

    main_page.chat_widget.switch_to_frame()

    assert main_page.chat_widget.get_chat_title() == "Техническая поддержка", "Неверный заголовок открытого чата"


@allure.epic("Помощь и поддержка")
@allure.feature("Чат поддержки")
@allure.story("Навигация")
@allure.title("Переход к списку всех чатов по кнопке 'Назад'")
@allure.tag("Positive")
def test_open_all_chats_list(opened_chat_widget):
    opened_chat_widget.click_back_button()

    assert opened_chat_widget.is_chats_list_displayed(), "Экран со списком 'Чаты' не отобразился"


@allure.epic("Помощь и поддержка")
@allure.feature("Чат поддержки")
@allure.story("Меню чата")
@allure.title("Включение и отключение уведомлений в чате")
@allure.tag("Positive")
def test_switch_toggle_notification(opened_chat_widget):
    opened_chat_widget.open_menu()

    assert opened_chat_widget.is_opened_bottom_sheet(), "Ботомшит не открылся"
    assert opened_chat_widget.get_notifications_button_text() == "Отключить уведомления в чате"

    opened_chat_widget.switch_toggle_notifications()
    assert opened_chat_widget.is_closed_bottom_sheet(), "Ботомшит не закрылся после переключения уведомлений"

    opened_chat_widget.open_menu()
    assert opened_chat_widget.get_notifications_button_text() == "Включить уведомления в чате"


@allure.epic("Помощь и поддержка")
@allure.feature("Чат поддержки")
@allure.story("Меню чата")
@allure.title("Оценить пустой диалог с поддержкой")
@allure.tag("Negative")
def test_rate_empty_dialog(opened_chat_widget):
    expected_substring = "Оценить качество обслуживания можно, после того, как вы начнете диалог."

    opened_chat_widget.open_menu()
    assert opened_chat_widget.is_opened_bottom_sheet(), "Ботомшит не открылось"

    opened_chat_widget.click_rate_chat()
    assert opened_chat_widget.is_closed_bottom_sheet(), "Ботомшит не закрылось после нажатия на оценку"

    actual_message = opened_chat_widget.wait_for_last_message(expected_substring)
    assert expected_substring in actual_message, f"Ожидалось сообщение '{expected_substring}', получено '{actual_message}'"


@allure.epic("Помощь и поддержка")
@allure.feature("Чат поддержки")
@allure.story("Открытие и закрытие")
@allure.title("Закрытие виджета чата")
@allure.tag("Positive")
def test_close_chat(opened_chat_widget):
    opened_chat_widget.close()

    assert opened_chat_widget.is_closed(), "Виджет чата не закрылся"