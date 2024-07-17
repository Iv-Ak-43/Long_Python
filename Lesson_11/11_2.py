# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from time import sleep


site = "https://fix-sso.sbis.ru/auth-online/?ret=fix-online.sbis.ru/"
site_fix = "https://fix-online.sbis.ru/"
driver = webdriver.Chrome()


try:
    driver.maximize_window()
    driver.get(site)
    login_value, password_value = "Бетмен", "Бетмен123"
    assert driver.current_url == site, "Не верно открыт сайт"
    sleep(1)

    """Авторизация"""

    login_input = driver.find_element(By.CSS_SELECTOR, '.controls-Field[type="text"]')
    login_input.send_keys(login_value, Keys.ENTER)
    assert login_input.get_attribute('value') == login_value, "Для входа укажите логин или телефон"  # Проверка ввода логина
    sleep(1)
    password_input = driver.find_element(By.CSS_SELECTOR, '.controls-Field[type="password"]')
    password_input.send_keys(password_value, Keys.ENTER)
    assert password_input.get_attribute('value') == password_value, "Неверный логин или пароль"  # Проверка ввода пароля
    sleep(5)
    assert driver.current_url == site_fix  # Проверка что мы на сайте https://fix-online.sbis.ru/

    """Раздел контакты"""

    contacts = driver.find_element(By.CSS_SELECTOR,
                                   '.NavigationPanels-Accordion__title.NavigationPanels-Accordion__title_level-1')
    actions_contacts = ActionChains(driver)
    actions_contacts.double_click(contacts)
    actions_contacts.perform()
    sleep(3)
    close_button = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__closeIcon')
    assert driver.current_url == 'https://fix-online.sbis.ru/page/dialogs' # Проверка что открыто окно "Диалоги"
    actions_close = ActionChains(driver)
    actions_close.click(close_button)
    actions_close.perform()
    sleep(3)

    """Выбор сотрудника, ввод и отправка сообщения"""

    contact_value = 'Белоярова Ирина'
    new_message = driver.find_element(By.CSS_SELECTOR, '.icon-EmptyMessage.controls-icon_size-s').click()
    sleep(2)
    search_string = driver.find_element(By.CSS_SELECTOR, '.controls-StackTemplate__headerContentTemplate .controls-Search__nativeField_caretEmpty_theme_default')
    search_string.send_keys(contact_value, Keys.ENTER)
    sleep(3)
    click_name = driver.find_element(By.CSS_SELECTOR, '[data-qa="person-Information__fio"]')
    actions_search = ActionChains(driver)
    actions_search.move_to_element(click_name).click(click_name)
    actions_search.perform()
    sleep(2)
    message = 'Сегодня прекрасный день! Бетмен рулит!'
    message_input = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    message_input.send_keys(message, Keys.ENTER)
    push_message = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]').click()  # Отправка сообщения
    close_message = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-stack-Button__close"]').click()  # Закрытие окна
    sleep(2)
    all_message = driver.find_elements(By.CSS_SELECTOR, '.msg-entity-expander .ws-flex-shrink-1')
    assert all_message[0].text == message  # Проверка что сообщение появилось в реестре
    sleep(2)

    """Удаление сообщения"""

    actions_del_message = ActionChains(driver)
    actions_del_message.move_to_element(all_message[0])
    actions_del_message.context_click(all_message[0])
    actions_del_message.perform()
    sleep(5)
    del_button = driver.find_element(By.XPATH, '//*[@id="popup"]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div[3]/div[11]/div/div/div/div')
    sleep(2)
    del_button.click()
    sleep(2)
    # Проверка удаления сообщения
    all_message_after_delete = driver.find_elements(By.CSS_SELECTOR, '.msg-entity-expander .ws-flex-shrink-1')
    assert message not in all_message_after_delete[0].text, 'Сообщение не удалено из реестра'

    print("Тест пройден успешно!")

finally:
    driver.quit()

