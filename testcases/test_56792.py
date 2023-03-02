@pytest.mark.skip(reason="Template")
def test_56792_1(app, credo_db, forpost_db):
    """
    {#
        :id:                56792_1
        :priority:          Средний
        :module:            ЕФР
        :description:       Проверка назначения задачи "Контрольная точка" после первого сохранения сессии
        :precondition:      Пользователь levdanskij авторизован
        :precondition:      Пользователь levdanskij инициатор заявки с ролью credit_expert (без доступа к варианту "Регистрация/изменение данных клиента"), middle_office и front_office (с доступом к варианту "Регистрация/изменение данных клиента")
        :precondition:      Пользователь petrukovich с ролью credit_expert (без доступа к варианту "Регистрация/изменение данных клиента")
        :precondition:      Пользователь semenov с ролью middle_office (с доступом к варианту "Регистрация/изменение данных клиента")
        :precondition:      Пользователь maslov с ролью front_office (с доступом к варианту "Регистрация/изменение данных клиента")
        :precondition:      Пользователь gulevich с ролью admins (с доступом к варианту "Регистрация/изменение данных клиента")
        :precondition:      Пользователь abramchuk с ролью admins (без доступа к варианту "Регистрация/изменение данных клиента")
        :precondition:      Параметр варианта cabinet_showTasks = да
        :precondition:      В файле Save.groovy в конце блока кода с id="_66" после строки "onExit();" вставляем строку "throw new RuntimeException("Тестирование контрольной точки!!!");"
        :source_point:      RM56792;
        :tc_type:           +
        :db_env:            База FORPOST: forp_d8; Тестовая дата: 09.04.2021
        :client_env:        Google Chrome 94 [Windows 10; openSuSE Linux Leap 15.3]
        :client_env:        Mozilla Firefox 92 [Windows 10; openSuSE Linux Leap 15.3]
        :client_env:        Microsoft EDGE 94 [Windows 10]
        :time_of_test:      40
        :precondition_time: 20
        :count_of_check:    8
    }#
        :param: app: фикстура приложения
        :param: credo_db: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'changing_customer'
    VARIANT = 'CustomerFind'

    # :newpage: #######################################################################################################

    # :step: На форме "Поиск клиента" заполняем поле "Личный номер"
    value = '7134528A385PB2'

    # :step: Нажимаем кнопку "Искать"
    # :step: Выбираем найденную карточку клиента

    # :newpage: #######################################################################################################

    # :step: На форме "Данные клиента" нажимаем кнопку "Изменить"
    # :step: На форме "Реквизиты клиента" редактируем поле "Отчество"
    value = 'ОТЧЕСТВОО'
    # :step: Нажимем кнопку "Далее"

    # :newpage: #######################################################################################################

    # :step: На форме "Контрольная точка" нажимаем кнопку "Отменить"
    # :assert: Переход в профиль клиента, в блоке активные заявки по тестовой заявке с задачей "Контрольная точка" доступно действие "Продолжить"
    # :assert: Задача "Контрольная точка" назначена на роли инициатора заявки, которые имеют права доступа к созданию заявок на варианте "Регистрация/изменение данных физического лица" и роль admins (Служебная информация о заявке, поле Performers: admins, front_office, middle_office).

    # :newpage: #######################################################################################################

    # :step: В списке пользователей у пользователя levdanskij оставляем только роль credit_expert
    # :step: Выходим из системы

    # :newpage: #######################################################################################################

    # :step: Авторизируемся пользователем levdanskij

    # :newpage: #######################################################################################################

    # :step: Переходим на форму "Мои задачи" (меню-гамбургер)
    # :assert: На форме "Мои задачи" отсутствует задача "Контрольная точка" по тестовой заявке
    # :step: Выходим из системы

    # :newpage: #######################################################################################################

    # :step: Авторизируемся пользователем petrukovich

    # :newpage: #######################################################################################################

    # :step: Переходим на форму "Мои задачи" (меню-гамбургер)
    # :assert: На форме "Мои задачи" отсутствует задача "Контрольная точка" по тестовой заявке
    # :step: Выходим из системы

    # :newpage: #######################################################################################################

    # :step: Авторизируемся пользователем semenov

    # :newpage: #######################################################################################################

    # :step: Переходим на форму "Мои задачи" (меню-гамбургер)
    # :assert: На форме "Мои задачи" присутствует задача "Контрольная точка" по тестовой заявке
    # :step: Выходим из системы

    # :newpage: #######################################################################################################

    # :step: Авторизируемся пользователем maslov

    # :newpage: #######################################################################################################

    # :step: Переходим на форму "Мои задачи" (меню-гамбургер)
    # :assert: На форме "Мои задачи" присутствует задача "Контрольная точка" по тестовой заявке
    # :step: Выходим из системы

    # :newpage: #######################################################################################################

    # :step: Авторизируемся пользователем gulevich

    # :newpage: #######################################################################################################

    # :step: Переходим на форму "Мои задачи" (меню-гамбургер)
    # :assert: На форме "Мои задачи" присутствует задача "Контрольная точка" по тестовой заявке
    # :step: Выходим из системы

    # :newpage: #######################################################################################################

    # :step: Авторизируемся пользователем abramchuk

    # :newpage: #######################################################################################################

    # :step: Переходим на форму "Мои задачи" (меню-гамбургер)
    # :assert: На форме "Мои задачи" присутствует задача "Контрольная точка" по тестовой заявке


    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


@pytest.mark.skip(reason="Template")
def test_56792_2(app, credo_db, forpost_db):
    """
    {#
        :id:                56792_2
        :priority:          Средний
        :module:            ЕФР
        :description:       Проверка назначения задачи "Контрольная точка" перед заявлением
        :precondition:      Пользователь levdanskij авторизован
        :precondition:      Пользователь levdanskij инициатор заявки с ролью credit_expert (без доступа к варианту "Регистрация/изменение данных клиента"), middle_office и front_office (с доступом к варианту "Регистрация/изменение данных клиента")
        :precondition:      Пользователь petrukovich с ролью credit_expert (без доступа к варианту "Регистрация/изменение данных клиента")
        :precondition:      Пользователь semenov с ролью middle_office (с доступом к варианту "Регистрация/изменение данных клиента")
        :precondition:      Пользователь maslov с ролью front_office (с доступом к варианту "Регистрация/изменение данных клиента")
        :precondition:      Пользователь gulevich с ролью admins (с доступом к варианту "Регистрация/изменение данных клиента")
        :precondition:      Пользователь abramchuk с ролью admins (без доступа к варианту "Регистрация/изменение данных клиента")
        :precondition:      Параметр варианта cabinet_showTasks = да
        :precondition:      В файле Save.groovy в конце блока кода с id="_63" после строки "onExit();" вставляем строку "throw new RuntimeException("Тестирование контрольной точки!!!");"
        :source_point:      RM56792;
        :tc_type:           +
        :db_env:            База FORPOST: forp_d8; Тестовая дата: 09.04.2021
        :client_env:        Google Chrome 94 [Windows 10; openSuSE Linux Leap 15.3]
        :client_env:        Mozilla Firefox 92 [Windows 10; openSuSE Linux Leap 15.3]
        :client_env:        Microsoft EDGE 94 [Windows 10]
        :time_of_test:      40
        :precondition_time: 20
        :count_of_check:    8
    }#
        :param: app: фикстура приложения
        :param: credo_db: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'changing_customer'
    VARIANT = 'CustomerFind'

    # :newpage: #######################################################################################################

    # :step: На форме "Поиск клиента" заполняем поле "Личный номер"
    value = '7134528A385PB2'

    # :step: Нажимаем кнопку "Искать"
    # :step: Выбираем найденную карточку клиента

    # :newpage: #######################################################################################################

    # :step: На форме "Данные клиента" нажимаем кнопку "Изменить"
    # :step: На форме "Реквизиты клиента" редактируем поле "Отчество"
    value = 'ОТЧЕСТВОО'
    # :step: Нажимем кнопку "Далее"

    # :newpage: #######################################################################################################

    # :step: На форме "Контрольная точка" нажимаем кнопку "Отменить"
    # :assert: Переход в профиль клиента, в блоке активные заявки по тестовой заявке с задачей "Контрольная точка" доступно действие "Продолжить"
    # :assert: Задача "Контрольная точка" назначена на роли инициатора заявки, которые имеют права доступа к созданию заявок на варианте "Регистрация/изменение данных физического лица" и роль admins (Служебная информация о заявке, поле Performers: admins, front_office, middle_office).

    # :newpage: #######################################################################################################

    # :step: В списке пользователей у пользователя levdanskij оставляем только роль credit_expert
    # :step: Выходим из системы

    # :newpage: #######################################################################################################

    # :step: Авторизируемся пользователем levdanskij

    # :newpage: #######################################################################################################

    # :step: Переходим на форму "Мои задачи" (меню-гамбургер)
    # :assert: На форме "Мои задачи" отсутствует задача "Контрольная точка" по тестовой заявке
    # :step: Выходим из системы

    # :newpage: #######################################################################################################

    # :step: Авторизируемся пользователем petrukovich

    # :newpage: #######################################################################################################

    # :step: Переходим на форму "Мои задачи" (меню-гамбургер)
    # :assert: На форме "Мои задачи" отсутствует задача "Контрольная точка" по тестовой заявке
    # :step: Выходим из системы

    # :newpage: #######################################################################################################

    # :step: Авторизируемся пользователем semenov

    # :newpage: #######################################################################################################

    # :step: Переходим на форму "Мои задачи" (меню-гамбургер)
    # :assert: На форме "Мои задачи" присутствует задача "Контрольная точка" по тестовой заявке
    # :step: Выходим из системы

    # :newpage: #######################################################################################################

    # :step: Авторизируемся пользователем maslov

    # :newpage: #######################################################################################################

    # :step: Переходим на форму "Мои задачи" (меню-гамбургер)
    # :assert: На форме "Мои задачи" присутствует задача "Контрольная точка" по тестовой заявке
    # :step: Выходим из системы

    # :newpage: #######################################################################################################

    # :step: Авторизируемся пользователем gulevich

    # :newpage: #######################################################################################################

    # :step: Переходим на форму "Мои задачи" (меню-гамбургер)
    # :assert: На форме "Мои задачи" присутствует задача "Контрольная точка" по тестовой заявке
    # :step: Выходим из системы

    # :newpage: #######################################################################################################

    # :step: Авторизируемся пользователем abramchuk

    # :newpage: #######################################################################################################

    # :step: Переходим на форму "Мои задачи" (меню-гамбургер)
    # :assert: На форме "Мои задачи" присутствует задача "Контрольная точка" по тестовой заявке


    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


@pytest.mark.skip(reason="Template")
def test_56792_3(app, credo_db, forpost_db):
    """
    {#
        :id:                56792_3
        :priority:          Средний
        :module:            ЕФР
        :description:       Проверка назначения задачи "Контрольная точка" после отправки на контент сервер
        :precondition:      Пользователь levdanskij авторизован
        :precondition:      Пользователь levdanskij инициатор заявки с ролью credit_expert (без доступа к варианту "Регистрация/изменение данных клиента"), middle_office и front_office (с доступом к варианту "Регистрация/изменение данных клиента")
        :precondition:      Пользователь petrukovich с ролью credit_expert (без доступа к варианту "Регистрация/изменение данных клиента")
        :precondition:      Пользователь semenov с ролью middle_office (с доступом к варианту "Регистрация/изменение данных клиента")
        :precondition:      Пользователь maslov с ролью front_office (с доступом к варианту "Регистрация/изменение данных клиента")
        :precondition:      Пользователь gulevich с ролью admins (с доступом к варианту "Регистрация/изменение данных клиента")
        :precondition:      Пользователь abramchuk с ролью admins (без доступа к варианту "Регистрация/изменение данных клиента")
        :precondition:      Параметр варианта cabinet_showTasks = да
        :precondition:      Параметр пользователя using_scanner (Доступность сканирования) = "да"
        :precondition:      На машине с подключенным сканером установлено требуемое локальное ПО, сканер запущен. Запущены Станция администратора и Контент-сервер Сканирования. ДУЛ присутствует в сканере.
        :precondition:      В файле Save.groovy в конце блока кода с id="_64" после строки "onExit();" вставляем строку "throw new RuntimeException("Тестирование контрольной точки!!!");"
        :source_point:      RM56792;
        :tc_type:           +
        :db_env:            База FORPOST: forp_d8; Тестовая дата: 09.04.2021
        :client_env:        Google Chrome 94 [Windows 10; openSuSE Linux Leap 15.3]
        :client_env:        Mozilla Firefox 92 [Windows 10; openSuSE Linux Leap 15.3]
        :client_env:        Microsoft EDGE 94 [Windows 10]
        :time_of_test:      40
        :precondition_time: 20
        :count_of_check:    8
    }#
        :param: app: фикстура приложения
        :param: credo_db: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'changing_customer'
    VARIANT = 'CustomerFind'

    # :newpage: #######################################################################################################

    # :step: На форме "Поиск клиента" заполняем поле "Личный номер"
    value = '7134528A385PB2'

    # :step: Нажимаем кнопку "Искать"
    # :step: Выбираем найденную карточку клиента

    # :newpage: #######################################################################################################

    # :step: На форме "Данные клиента" нажимаем кнопку "Изменить"
    # :step: На форме "Реквизиты клиента" редактируем поле "Отчество"
    value = 'ОТЧЕСТВОО'
    # :step: В сканировании сопроводительного документа устанавливаем чек-бокс
    value = 'Планшет'
    # :step: Нажимаем кнопку "Сканировать сопроводительный документ"
    # :step: В сканировании документа вводим название сопроводительного документа
    value = '1'
    # :step: Нажимаем кнопку "Продолжить"
    # :step: Нажимаем кнопку "Завершить"
    # :step: Нажимем кнопку "Далее"

    # :newpage: #######################################################################################################

    # :step: На форме "Контрольная точка" нажимаем кнопку "Отменить"
    # :assert: Переход в профиль клиента, в блоке активные заявки по тестовой заявке с задачей "Контрольная точка" доступно действие "Продолжить"
    # :assert: Задача "Контрольная точка" назначена на роли инициатора заявки, которые имеют права доступа к созданию заявок на варианте "Регистрация/изменение данных физического лица" и роль admins (Служебная информация о заявке, поле Performers: admins, front_office, middle_office).

    # :newpage: #######################################################################################################

    # :step: В списке пользователей у пользователя levdanskij оставляем только роль credit_expert
    # :step: Выходим из системы

    # :newpage: #######################################################################################################

    # :step: Авторизируемся пользователем levdanskij

    # :newpage: #######################################################################################################

    # :step: Переходим на форму "Мои задачи" (меню-гамбургер)
    # :assert: На форме "Мои задачи" отсутствует задача "Контрольная точка" по тестовой заявке
    # :step: Выходим из системы

    # :newpage: #######################################################################################################

    # :step: Авторизируемся пользователем petrukovich

    # :newpage: #######################################################################################################

    # :step: Переходим на форму "Мои задачи" (меню-гамбургер)
    # :assert: На форме "Мои задачи" отсутствует задача "Контрольная точка" по тестовой заявке
    # :step: Выходим из системы

    # :newpage: #######################################################################################################

    # :step: Авторизируемся пользователем semenov

    # :newpage: #######################################################################################################

    # :step: Переходим на форму "Мои задачи" (меню-гамбургер)
    # :assert: На форме "Мои задачи" присутствует задача "Контрольная точка" по тестовой заявке
    # :step: Выходим из системы

    # :newpage: #######################################################################################################

    # :step: Авторизируемся пользователем maslov

    # :newpage: #######################################################################################################

    # :step: Переходим на форму "Мои задачи" (меню-гамбургер)
    # :assert: На форме "Мои задачи" присутствует задача "Контрольная точка" по тестовой заявке
    # :step: Выходим из системы

    # :newpage: #######################################################################################################

    # :step: Авторизируемся пользователем gulevich

    # :newpage: #######################################################################################################

    # :step: Переходим на форму "Мои задачи" (меню-гамбургер)
    # :assert: На форме "Мои задачи" присутствует задача "Контрольная точка" по тестовой заявке
    # :step: Выходим из системы

    # :newpage: #######################################################################################################

    # :step: Авторизируемся пользователем abramchuk

    # :newpage: #######################################################################################################

    # :step: Переходим на форму "Мои задачи" (меню-гамбургер)
    # :assert: На форме "Мои задачи" присутствует задача "Контрольная точка" по тестовой заявке


    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


@pytest.mark.skip(reason="Template")
def test_56792_4(app, credo_db, forpost_db):
    """
    {#
        :id:                56792_4
        :priority:          Средний
        :module:            ЕФР
        :description:       Проверка назначения задачи "Контрольная точка" после обновления в СОУ
        :precondition:      Пользователь levdanskij авторизован
        :precondition:      Пользователь levdanskij инициатор заявки с ролью credit_expert (без доступа к варианту "Регистрация/изменение данных клиента"), middle_office и front_office (с доступом к варианту "Регистрация/изменение данных клиента")
        :precondition:      Пользователь petrukovich с ролью credit_expert (без доступа к варианту "Регистрация/изменение данных клиента")
        :precondition:      Пользователь semenov с ролью middle_office (с доступом к варианту "Регистрация/изменение данных клиента")
        :precondition:      Пользователь maslov с ролью front_office (с доступом к варианту "Регистрация/изменение данных клиента")
        :precondition:      Пользователь gulevich с ролью admins (с доступом к варианту "Регистрация/изменение данных клиента")
        :precondition:      Пользователь abramchuk с ролью admins (без доступа к варианту "Регистрация/изменение данных клиента")
        :precondition:      Параметр варианта cabinet_showTasks = да
        :precondition:      В файле Save.groovy в конце блока кода с id="_65" после строки "onExit();" вставляем строку "throw new RuntimeException("Тестирование контрольной точки!!!");"
        :source_point:      RM56792;
        :tc_type:           +
        :db_env:            База FORPOST: forp_d8; Тестовая дата: 09.04.2021
        :client_env:        Google Chrome 94 [Windows 10; openSuSE Linux Leap 15.3]
        :client_env:        Mozilla Firefox 92 [Windows 10; openSuSE Linux Leap 15.3]
        :client_env:        Microsoft EDGE 94 [Windows 10]
        :time_of_test:      40
        :precondition_time: 20
        :count_of_check:    8
    }#
        :param: app: фикстура приложения
        :param: credo_db: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'changing_customer'
    VARIANT = 'CustomerFind'

    # :newpage: #######################################################################################################

    # :step: На форме "Поиск клиента" заполняем поле "Личный номер"
    value = '7134528A385PB2'

    # :step: Нажимаем кнопку "Искать"
    # :step: Выбираем найденную карточку клиента

    # :newpage: #######################################################################################################

    # :step: На форме "Данные клиента" нажимаем кнопку "Изменить"
    # :step: На форме "Реквизиты клиента" редактируем поле "Отчество"
    value = 'ОТЧЕСТВОО'
    # :step: Нажимем кнопку "Далее"

    # :newpage: #######################################################################################################

    # :step: На форме "Контрольная точка" нажимаем кнопку "Отменить"
    # :assert: Переход в профиль клиента, в блоке активные заявки по тестовой заявке с задачей "Контрольная точка" доступно действие "Продолжить"
    # :assert: Задача "Контрольная точка" назначена на роли инициатора заявки, которые имеют права доступа к созданию заявок на варианте "Регистрация/изменение данных физического лица" и роль admins (Служебная информация о заявке, поле Performers: admins, front_office, middle_office).

    # :newpage: #######################################################################################################

    # :step: В списке пользователей у пользователя levdanskij оставляем только роль credit_expert
    # :step: Выходим из системы

    # :newpage: #######################################################################################################

    # :step: Авторизируемся пользователем levdanskij

    # :newpage: #######################################################################################################

    # :step: Переходим на форму "Мои задачи" (меню-гамбургер)
    # :assert: На форме "Мои задачи" отсутствует задача "Контрольная точка" по тестовой заявке
    # :step: Выходим из системы

    # :newpage: #######################################################################################################

    # :step: Авторизируемся пользователем petrukovich

    # :newpage: #######################################################################################################

    # :step: Переходим на форму "Мои задачи" (меню-гамбургер)
    # :assert: На форме "Мои задачи" отсутствует задача "Контрольная точка" по тестовой заявке
    # :step: Выходим из системы

    # :newpage: #######################################################################################################

    # :step: Авторизируемся пользователем semenov

    # :newpage: #######################################################################################################

    # :step: Переходим на форму "Мои задачи" (меню-гамбургер)
    # :assert: На форме "Мои задачи" присутствует задача "Контрольная точка" по тестовой заявке
    # :step: Выходим из системы

    # :newpage: #######################################################################################################

    # :step: Авторизируемся пользователем maslov

    # :newpage: #######################################################################################################

    # :step: Переходим на форму "Мои задачи" (меню-гамбургер)
    # :assert: На форме "Мои задачи" присутствует задача "Контрольная точка" по тестовой заявке
    # :step: Выходим из системы

    # :newpage: #######################################################################################################

    # :step: Авторизируемся пользователем gulevich

    # :newpage: #######################################################################################################

    # :step: Переходим на форму "Мои задачи" (меню-гамбургер)
    # :assert: На форме "Мои задачи" присутствует задача "Контрольная точка" по тестовой заявке
    # :step: Выходим из системы

    # :newpage: #######################################################################################################

    # :step: Авторизируемся пользователем abramchuk

    # :newpage: #######################################################################################################

    # :step: Переходим на форму "Мои задачи" (меню-гамбургер)
    # :assert: На форме "Мои задачи" присутствует задача "Контрольная точка" по тестовой заявке


    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)