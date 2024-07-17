# Предварительные действия (Создайте эталонную задачу, заполнив обязательные поля)
# Авторизоваться на сайте https://fix-online.sbis.ru/.
# Откройте эталонную задачу по прямой ссылке в новом окне
# Убедитесь, что в заголовке вкладки отображается "Задача №НОМЕР от ДАТА", где ДАТА и НОМЕР - это ваши эталонные значения
# Проверьте, что поля: Исполнитель, дата, номер, описание и автор отображаются с эталонными значениями
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from atf.ui import *
from atf import log


class AuthPage(Region):
    login = TextField(By.CSS_SELECTOR, '.controls-Field[type="text"]', 'логин')
    password = TextField(By.CSS_SELECTOR, '.controls-Field[type="password"]', 'пароль')


class ParamsStandartTask(Region):
    date_task = Element(By.CSS_SELECTOR, '[data-qa="edo3-Document_docDate"]', 'Дата задачи')
    namber_task = Element(By.CSS_SELECTOR, '[title="ZK24071281292"]', 'номер задачи')
    author = Element(By.CSS_SELECTOR, '[data-qa="edo3-Sticker__mainInfo"]', 'автор')
    performer = Element(By.CSS_SELECTOR, '[data-qa="SelectedCollection__item"]', 'исполнитель')
    description = Element(By.CSS_SELECTOR, '[name="editorWrapper"]', 'описание')



class Test(TestCaseUI):
    def test(self):
        sbis_site = self.config.get('SBIS_SITE')
        sbis_auth = self.config.get('SBIS_AUTH')
        self.browser.open(sbis_site)
        standart_task = 'https://fix-online.sbis.ru/opendoc.html?guid=e226841e-0719-4581-9155-2c75d648e2de&client=3'

        log('Проверка вкладки авторизация')
        self.browser.should_be(UrlContains(sbis_auth))

        log('Авторизоваться')
        user_login, user_password = self.config.get('USER_LOGIN'), self.config.get('USER_PASSWORD')
        auth_page = AuthPage(self.driver)
        auth_page.login.type_in(user_login + Keys.ENTER)
        auth_page.login.should_be(ExactText(user_login))
        auth_page.password.type_in(user_password + Keys.ENTER)

        log('Открытие задачи в новом окне')
        self.browser.create_new_tab(standart_task)
        self.browser.switch_to_opened_window()

        log('Проверка заголовка страницы')
        self.browser.should_be(TitleExact(self.config.get('SBIS_TITLE')))

        log('Проверка: автора, исполнителя, описания, даты, номера')
        params_standert = ParamsStandartTask(self.driver)
        params_standert.author.should_be(Visible, ContainsText('Белоярова Ирина'))
        params_standert.performer.should_be(Visible, ContainsText('Белоярова Ирина'))
        params_standert.description.should_be(Visible, ContainsText('Эталонная задача'))
        params_standert.date_task.should_be(Visible, ContainsText('12 июл, пт'))
        params_standert.namber_task.should_be(Visible, ContainsText('...292'))


