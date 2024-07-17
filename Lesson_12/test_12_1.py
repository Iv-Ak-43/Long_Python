# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты Отправить сообщение самому себеУбедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from atf.ui import *
from atf import log
import time


class AuthPage(Region):
    login = TextField(By.CSS_SELECTOR, '.controls-Field[type="text"]', 'логин')
    password = TextField(By.CSS_SELECTOR, '.controls-Field[type="password"]', 'пароль')


class Contact(Region):
    page_contacts = TextField(By.CSS_SELECTOR, '[data-qa="Контакты"]', 'раздел контакты')

class NewMessage(Region):
    button_new_message = Button(By.CSS_SELECTOR, '.icon-EmptyMessage.controls-icon_size-s', 'кнопка создания нового '
                                                                                            'сообщения')
    search_string = TextField(By.CSS_SELECTOR,'.controls-StackTemplate__headerContentTemplate '
                                              '.controls-Search__nativeField_caretEmpty_theme_default',
                              'поиск сотрудника')
    click_name = Element(By.XPATH, '//*[@id="popup"]/div[1]/div/div[2]/div/div[3]/div[2]/div[3]/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div[1]/div/div[3]', 'выбор сотрудника')
    message_input = TextField(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]', 'ввод сообщения')
    push_message = Button(By.CSS_SELECTOR,'[data-qa="msg-send-editor__send-button"]', 'отправка сообщения')
    close_message = Button(By.CSS_SELECTOR, '[data-qa="controls-stack-Button__close"]', 'закрытие окна')


class DellMessage(Region):
    all_message = CustomList(By.CSS_SELECTOR, '.msg-entity-expander .ws-flex-shrink-1','Все сообщения')
    del_button = Button(By.XPATH, '//*[@id="popup"]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div[3]/div[11]/div/div/div/div', 'удаление сообщения')


class Test(TestCaseUI):
    def test(self):
        sbis_site = self.config.get('SBIS_SITE')
        sbis_auth = self.config.get('SBIS_AUTH')
        message = 'Сегодня прекрасный день! BetMan рулит'
        self.browser.open(sbis_site)

        log('Проверка вкладки авторизация')
        self.browser.should_be(UrlContains(sbis_auth))

        log('Авторизоваться')
        user_login, user_password = self.config.get('USER_LOGIN'), self.config.get('USER_PASSWORD')
        auth_page = AuthPage(self.driver)
        auth_page.login.type_in(user_login + Keys.ENTER)
        auth_page.login.should_be(ExactText(user_login))
        auth_page.password.type_in(user_password + Keys.ENTER)

        log('Раздел контакты')
        contacts = Contact(self.driver)
        contacts.page_contacts.click()
        time.sleep(1)
        contacts.page_contacts.click()
        self.browser.should_be(UrlExact('https://fix-online.sbis.ru/page/dialogs'))

        log('Выбор сотрудника, ввод и отправка сообщения')
        NewMessage(self.driver)
        NewMessage.button_new_message.click()
        NewMessage.search_string.send_keys('Белоярова Ирина' + Keys.ENTER)
        NewMessage.click_name.click()
        NewMessage.message_input.send_keys(message)
        NewMessage.push_message.click()
        NewMessage.close_message.click()
        #self.browser.should_be(ExactText(message))

        log('Удаление сообщения')
        DellMessage(self.driver)
        DellMessage.all_message.item(contains_text=message).should_be(Visible).context_click()
        DellMessage.del_button.click()
        DellMessage.all_message.item(contains_text=message).should_not_be(Visible)
