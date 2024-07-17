# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By

site = "https://sbis.ru/"
site_tensor = "https://tensor.ru/about"
driver = webdriver.Chrome()

try:
    driver.maximize_window()
    driver.get(site)
    assert driver.current_url == site, "Не верно открыт сайт"
    button_contact = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item [href="/contacts"]')
    button_contact.click()
    baner_tensor = driver.find_element(By.CSS_SELECTOR, ' .sbisru-Contacts__logo-tensor')
    assert baner_tensor, 'Не отобразился баннер Тензор'
    baner_tensor.click()
    driver.switch_to.window(driver.window_handles[1])
    block_news = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content .tensor_ru-Index__card-title')
    driver.execute_script("return arguments[0].scrollIntoView(true);", block_news)
    assert "Сила в людях" in block_news.text, "Заголовок 'Сила в людях' не найден в тексте элемента"
    button_info = driver.find_element(By.CSS_SELECTOR, ".tensor_ru-link[href='/about']")
    button_info.click()
    assert driver.current_url == site_tensor, "Не удалось перейти на страницу tensor.ru/about"
    print("Тест пройден успешно!")

finally:
    driver.quit()
