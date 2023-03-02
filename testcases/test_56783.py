@pytest.mark.skip(reason="Template")
def test_save_index_coato_code(app, credo_db, forpost_db):
    """
    {#
        :id:                48353_8
        :priority:          Средний
        :module:            ЕФР
        :description:       Сохранение параметров «индекс» и «Кода СОАТО» на параметрах клиента СКЗ и ЕРК
        :precondition:      Пользователь авторизирован в СКЗ
        :precondition:      У пользователя СКЗ параметр useNewCabinet ("Использование нового интерфейса") = "да"
        :precondition:      Клиент отсутствует в ЕРК
        :precondition:      В таблице-справочнике post_codes ("Справочник почтовых кодов") присутствуют строки, для которых "Наименование населенного пункта" = "БРЕСТ"
        :precondition:      В таблице-справочнике post_codes ("Справочник почтовых кодов") для населенного пункта "БРЕСТ" присутствует строка с "Наименование улицы" = "СОВЕТСКАЯ"
        :precondition:      В таблице-справочнике post_codes ("Справочник почтовых кодов") для населенного пункта "БРЕСТ" с улицей "СОВЕТСКАЯ", номера "Дом" = "1,3,10,33"
        :precondition:      В параметрах варианта "CUSTOMERFIND" "Оформление расчетной карточки" устанавливаем checkSoatoFields = да
        :source_point:      Регрессионный тест. RM48353, RM56030
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 09.04.2021
        :client_env:        Google Chrome 93 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 92 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 93 [Windows 10]
        :time_of_test:      20
        :precondition_time: 10
        :count_of_check:    1
    }#
        :param: app: фикстура приложения
        :param: credo_db: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'CHANGING_CUSTOMER'
    VARIANT = 'CUSTOMERFIND'

    # :newpage: #######################################################################################################

    # :step: На форме "Поиск клиента" заполняем поле "Личный номер"
    value = '7424901A637PB5'

    # :step: Нажимаем на кнопку "Искать"
    # :step: Заполняем фамилию
    value = 'Старин'
    # :step: Заполняем имя
    value = 'Мушараф'
    # :step: Заполняем мобильный телефон
    value = '+375299623388'
    # :step: Нажимаем на кнопку "Создать клиента"

    # :newpage: #######################################################################################################

    # :step: На форме "Профиль клиента" нажимаем кнопку "Изменить"

    # :newpage: #######################################################################################################

    # :step: На форме "Реквизиты клиента", заполняем пол
    value = 'Мужской'
    # :step: Заполняем имя латинскими буквами
    value = 'Musharaf'
    # :step: Заполняем фамилию латинскими буквами
    value = 'Starin'
    # :step: Заполняем гражданство
    value = 'БЕЛАРУСЬ'
    # :step: Заполняем дату рождения
    value = '11.11.1970'
    # :step: Заполняем тип документа
    value = 'Паспорт'
    # :step: Заполняем серия и номер документа
    value = 'ES7035739'
    # :step: Заполняем кем выдан документ
    value = 'Ленинский РОВД, г.Брест'
    # :step: Заполняем дату выдачи
    value = '14.03.2018'
    # :step: Заполняем срок действия документа
    value = '22.03.2024'
    # :step: Заполняем страна рождения
    value = 'BLR БЕЛАРУСЬ'
    # :step: Заполняем тип населенного пункта
    value = 'Город'
    # :step: Заполняем населенный пункт
    value = 'Пинск'
    # :step: Заполняем страну
    value = 'БЕЛАРУСЬ'
    # :step: Заполняем город или населенный пункт
    value = 'БРЕСТ г, БРЕСТСКАЯ обл'
    # :step: Заполняем улицу
    value = 'СОВЕТСКАЯ ул'
    # :step: Заполняем дом
    value = '33'
    # :step: Заполняем квартиру
    value = '2'
    # :step: Устанавливаем флаг место проживания аналогично месту регистрации
    # :step: Нажимаем "Далее"

    # :newpage: #######################################################################################################

    # :step: На форме "Заявление на изменение персональных данных клиента" нажимаем кнопку "Подтвердить выполнение указанных действий и закрыть"
    # :assert: На параметрах клиента СКЗ и ЕРК сохранились индекс регистрации "reg_index", индекс проживания "home_index", Код СОАТО (Место регистрации) "reg_soato_code" и  Код СОАТО (Место проживания) "home_soato_code"


    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


@pytest.mark.skip(reason="Template")
def test_save_only_index_code(app, credo_db, forpost_db):
    """
    {#
        :id:                48353_8_1
        :priority:          Средний
        :module:            ЕФР
        :description:       Сохранение параметра «индекс» на параметрах клиента СКЗ и ЕРК, без сохранения «Кода СОАТО»
        :precondition:      Пользователь авторизирован в СКЗ
        :precondition:      У пользователя СКЗ параметр useNewCabinet ("Использование нового интерфейса") = "да"
        :precondition:      Клиент отсутствует в ЕРК
        :precondition:      В таблице-справочнике post_codes ("Справочник почтовых кодов") присутствуют строки, для которых "Наименование населенного пункта" = "БРЕСТ"
        :precondition:      В таблице-справочнике post_codes ("Справочник почтовых кодов") для населенного пункта "БРЕСТ" присутствует строка с "Наименование улицы" = "СОВЕТСКАЯ"
        :precondition:      В таблице-справочнике post_codes ("Справочник почтовых кодов") для населенного пункта "БРЕСТ" с улицей "СОВЕТСКАЯ", номера "Дом" = "2,4,8"
        :precondition:      В параметрах варианта "CUSTOMERFIND" "Оформление расчетной карточки" устанавливаем checkSoatoFields = да
        :source_point:      Регрессионный тест. RM48353, RM56030
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 09.04.2021
        :client_env:        Google Chrome 93 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 92 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 93 [Windows 10]
        :time_of_test:      20
        :precondition_time: 10
        :count_of_check:    2
    }#
        :param: app: фикстура приложения
        :param: credo_db: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'CHANGING_CUSTOMER'
    VARIANT = 'CUSTOMERFIND'
    # :newpage: #######################################################################################################

    # :step: На форме "Поиск клиента" заполняем поле "Личный номер"
    value = '5020289C177PB3'

    # :step: Нажимаем на кнопку "Искать"
    # :step: Заполняем фамилию
    value = 'Мушараф'
    # :step: Заполняем имя
    value = 'Старин'
    # :step: Заполняем мобильный телефон
    value = '+375299623388'
    # :step: Нажимаем на кнопку "Создать клиента"

    # :newpage: #######################################################################################################

    # :step: На форме "Профиль клиента" нажимаем кнопку "Изменить"

    # :newpage: #######################################################################################################

    # :step: На форме "Реквизиты клиента", заполняем пол
    value = 'Мужской'
    # :step: Заполняем имя латинскими буквами
    value = 'Starin'
    # :step: Заполняем фамилию латинскими буквами
    value = 'Musharaf'
    # :step: Заполняем гражданство
    value = 'БЕЛАРУСЬ'
    # :step: Заполняем дату рождения
    value = '11.11.1970'
    # :step: Заполняем тип документа
    value = 'Паспорт'
    # :step: Заполняем серия и номер документа
    value = 'EW5739096'
    # :step: Заполняем кем выдан документ
    value = 'Ленинский РОВД, г.Брест'
    # :step: Заполняем дату выдачи
    value = '14.03.2018'
    # :step: Заполняем срок действия документа
    value = '22.03.2024'
    # :step: Заполняем страна рождения
    value = 'BLR БЕЛАРУСЬ'
    # :step: Заполняем тип населенного пункта
    value = 'Город'
    # :step: Заполняем населенный пункт
    value = 'Пинск'
    # :step: Заполняем страну
    value = 'БЕЛАРУСЬ'
    # :step: Заполняем город или населенный пункт
    value = 'БРЕСТ г, БРЕСТСКАЯ обл'
    # :step: Заполняем улицу
    value = 'СОВЕТСКАЯ ул'
    # :step: Заполняем дом
    value = '3324'
    # :step: Заполняем квартиру
    value = '2'
    # :step: Заполняем индекс
    value = '224000'
    # :step: Устанавливаем флаг место проживания аналогично месту регистрации
    # :step: Нажимаем "Далее"

    # :newpage: #######################################################################################################

    # :step: На форме "Заявление на изменение персональных данных клиента" нажимаем кнопку "Подтвердить выполнение указанных действий и закрыть"
    # :assert: На параметрах клиента СКЗ и ЕРК сохранились индекс регистрации "reg_index", индекс проживания "home_index"
    # :assert: На параметрах клиента СКЗ и ЕРК НЕ сохранились Код СОАТО (Место регистрации) "reg_soato_code" и  Код СОАТО (Место проживания) "home_soato_code"


    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)