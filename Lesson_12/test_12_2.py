# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Задачи на вкладку "В работе"
# Убедиться, что выделена папка "Входящие" и стоит маркер.
# Убедиться, что папка не пустая (в реестре есть задачи)
# Перейти в другую папку, убедиться, что теперь она выделена, а со "Входящие" выделение снято
# Создать новую папку и перейти в неё
# Убедиться, что она пустая
# Удалить новую папку, проверить, что её нет в списке папок
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from atf.ui import *
from atf import log


class AuthPage(Region):
    login = TextField(By.CSS_SELECTOR, '.controls-Field[type="text"]', 'логин')
    password = TextField(By.CSS_SELECTOR, '.controls-Field[type="password"]', 'пароль')


class Tasks(Region):
    task_all = Element(By.CSS_SELECTOR, '[data-qa="Задачи"]', 'Вкладка задачи')
    task_me = Element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle', 'Задачи на мне')
    task_in_work = Element(By.CSS_SELECTOR, '[data-qa="Controls-Tabs__item"]', 'в работе')
    task_in_coming = Element(By.CSS_SELECTOR, '[title="Входящие"]', 'Входящие')
    task_count = Element(By.CSS_SELECTOR, '[data-qa="controls-EditorList__additionalCounter"]', 'Количество задач')


class Folder(Region):
    another_folder = Element(By.CSS_SELECTOR, '[title="вапвапавпав"]', 'переход в другую папку')


class NewFolder(Region):
    button_plus = Button(By.CSS_SELECTOR, '[title="Создать задачу / Папку"]', 'кнопка + в задачах')
    create_new_folder = Element(By.CSS_SELECTOR, '.controls-ListView__item-rightPadding_menu-m .tw-flex', 'Папка')
    name = Element(By.CSS_SELECTOR, '.controls-InputBase__nativeField_caretFilled', 'Поле "название папки"')
    save = Button(By.CSS_SELECTOR, '.edws-UserFolderDialog__buttonSave', 'cохранить')
    created_folder = Element(By.CSS_SELECTOR, '[title="Папка для теста"]', 'Переход в созданную папку')
    no_task = Element(By.CSS_SELECTOR, '[data-qa="hint-EmptyView__title"]', 'Папка без задач')
    del_folder = Button(By.CSS_SELECTOR, '[title="Удалить папку"]', 'Удалить папку')
    del_folder_ok = Button(By.CSS_SELECTOR, '[data-qa="controls-ConfirmationDialog__button-true"]', 'Подтверждение')


class Test(TestCaseUI):
    def test(self):
        sbis_site = self.config.get('SBIS_SITE')
        sbis_auth = self.config.get('SBIS_AUTH')
        self.browser.open(sbis_site)

        log('Проверка вкладки авторизация')
        self.browser.should_be(UrlContains(sbis_auth))

        log('Авторизоваться')
        user_login, user_password = self.config.get('USER_LOGIN'), self.config.get('USER_PASSWORD')
        auth_page = AuthPage(self.driver)
        auth_page.login.type_in(user_login + Keys.ENTER)
        auth_page.login.should_be(ExactText(user_login))
        auth_page.password.type_in(user_password + Keys.ENTER)

        log('Раздел задачи --> в работе')
        tasks = Tasks(self.driver)
        tasks.task_all.click()
        tasks.task_me.click()
        self.browser.should_be(UrlExact('https://fix-online.sbis.ru/page/tasks-in-work'))
        tasks.task_in_work.click()
        tasks.task_in_coming.should_be(Visible, ContainsText('Входящие')).click().element('data-qa="marker"')
        tasks.task_count.should_be(Visible).should_not_be(ExactText('0'))

        log('Переход в другую папку')
        folder = Folder(self.driver)
        folder.another_folder.should_be(Visible, ContainsText('вапвапавпав')).click().element('data-qa="marker"')

        log('Создание новой папки, переход  и удаление')
        new_folder = NewFolder(self.driver)
        new_folder.button_plus.click()
        new_folder.create_new_folder.click()
        name_folder = self.config.get('NAME_FOLDER')
        new_folder.name.type_in(name_folder)
        new_folder.save.click()
        new_folder.created_folder.click()
        new_folder.no_task.should_be(Visible, ContainsText('В этой папке нет задач'))
        new_folder.created_folder.context_click()
        new_folder.del_folder.click()
        new_folder.del_folder_ok.click()
        new_folder.created_folder.should_not_be(Visible)

