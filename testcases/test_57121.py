@pytest.mark.skip(reason="Template")
def test_57121_1(app, credo_db, forpost_db):
    """
    {#
        :id:                57121_1
        :priority:          Средний
        :module:            Курсы/ДМ
        :description:       Проверка добавления новых полей в Список типов курсов и Список кодов металла
        :precondition:      Пользователь admin авторизован
        :precondition:      В Списке кодов металла для золота, серебра, платины и палладия имеются слитки номиналом 1 гр.
        :source_point:      RM57121_Приложение_1;
        :tc_type:           +
        :db_env:            БД: Node9_Rates;
        :client_env:        Google Chrome 96 [Windows 10; openSuSE Linux Leap 15.3]
        :client_env:        Mozilla Firefox 94 [Windows 10; openSuSE Linux Leap 15.3]
        :client_env:        Microsoft EDGE 96 [Windows 10]
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


    PRODUCT = ''
    VARIANT = ''

    # :newpage: #######################################################################################################

    # :step: Переходим в Драгоценные металлы/Список типов курсов (таблица JEWEL_RATE_TYPE)
    # :assert: В таблице добавлен новый тип "Учетная цена НБРБ"
    # :step: Переходим в Драгоценные металлы/Список кодов металла (таблица JEWELS)

    # :newpage: #######################################################################################################

    # :assert: В списке кодов металла присутствует столбец "Приоритет" с возможностью ввода отрицательного значения


    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


@pytest.mark.skip(reason="Template")
def test_57121_2(app, credo_db, forpost_db):
    """
    {#
        :id:                57121_2
        :priority:          Средний
        :module:            Курсы/ДМ
        :description:       Проверка отображения металлов при создании заявки в зависимости от приоритета ДМ
        :precondition:      Пользователь admin авторизован
        :precondition:      В Списке кодов металла для золота, серебра, платины и палладия имеются слитки номиналом 1 гр.
        :precondition:      В Списке кодов металла для металла "Золото" с номиналом = 1, устанавливаем приоритет = 1
        :precondition:      В Списке кодов металла для металла "Серебро" с номиналом = 1, устанавливаем приоритет = 2
        :precondition:      В Списке кодов металла для металла "Платина" с номиналом = 1, устанавливаем приоритет = 0
        :precondition:      В Списке кодов металла для металла "Палладий" с номиналом = 1, устанавливаем приоритет = -1
        :source_point:      RM57121_Ф.02;
        :tc_type:           +
        :db_env:            БД: Node9_Rates;
        :client_env:        Google Chrome 96 [Windows 10; openSuSE Linux Leap 15.3]
        :client_env:        Mozilla Firefox 94 [Windows 10; openSuSE Linux Leap 15.3]
        :client_env:        Microsoft EDGE 96 [Windows 10]
        :time_of_test:      40
        :precondition_time: 20
        :count_of_check:    2
    }#
        :param: app: фикстура приложения
        :param: credo_db: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = ''
    VARIANT = ''

    # :newpage: #######################################################################################################

    # :step: Переходим в Заявки/Список заявок
    # :step: Нажимаем на кнопку "Новая заявка"
    # :step: В поле "Вариант" выбираем значение
    value = 'Установка цен драгметаллов'
    # :step: Нажимаем на кнопку "Создать заявку"

    # :newpage: #######################################################################################################

    # :assert: На форме "Выбор групп для ввода цен драгметаллов и ценных монет" по Металлам отображаются для выбора номиналы = 1 и приоритетом > 0 (золото, серебро)
    # :assert: На форме "Выбор групп для ввода цен драгметаллов и ценных монет" по Металлам не отображаются для выбора номиналы = 1 и приоритетом < = 0 (платина, палладий)


    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


@pytest.mark.skip(reason="Template")
def test_57121_3(app, credo_db, forpost_db):
    """
    {#
        :id:                57121_3
        :priority:          Средний
        :module:            Курсы/ДМ
        :description:       Проверка запроса учетных цен по драгоценным металлам с сайта НБРБ и передача их в в кассовое решение
        :precondition:      Пользователь admin авторизован
        :precondition:      Конфигурационный параметр gate.timeout = 60000
        :precondition:      Запрос учетных цен по драгоценным металлам на сайт НБРБ выполняется с периодичностью nb.timeout = 10
        :precondition:      В Списке кодов металла для золота, серебра, платины и палладия имеются слитки номиналом 1 гр.
        :precondition:      Текущая дата 06.12.2021
        :precondition:      На начало тестирования отсутствуют курсы на дату <текущая системная дата + 1 день> (в ЦСКВ и на сайте НБРБ)
        :precondition:      Пример запроса учётной цены за 07.12.2021 "https://www.nbrb.by/services/xmlmetals.aspx?fromdate=12/07/2021&todate=12/07/2021"
        :precondition:      В кассовом решении реализована загрузка из ЦСВКВ учетных цен ДМ (RM57122)
        :source_point:      RM57121_Ф.01_Ф.03_Приложение_2;
        :tc_type:           +
        :db_env:            БД: Node9_Rates;
        :client_env:        Google Chrome 96 [Windows 10; openSuSE Linux Leap 15.3]
        :client_env:        Mozilla Firefox 94 [Windows 10; openSuSE Linux Leap 15.3]
        :client_env:        Microsoft EDGE 96 [Windows 10]
        :time_of_test:      60
        :precondition_time: 30
        :count_of_check:    10
    }#
        :param: app: фикстура приложения
        :param: credo_db: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = ''
    VARIANT = ''

    # :newpage: #######################################################################################################

    # :step: Переходим в Драгоценные металлы/Cписок курсов для металлов
    # :assert: Отсутствуют курсы на дату 07.12.2021, соответствующие запросу учётной цены
    # :step: Обновляем страницу после размещения курсов на сайте НБРБ
    # :assert: На дату 07.12.2021 (<текущая системная дата + 1 день> ) появились курсы, соответствующие запросу учётной цены, и зафиксировались в JEWEL_RATE_HISTORY

    # :newpage: #######################################################################################################

    # :assert: JEWEL_RATE_HISTORY.JRH_RATE_BEGIN = дата из Date (вложенный элемент AccountPrice ответа с сайта НБРБ)
    # :assert: JEWEL_RATE_HISTORY.JRH_VALUE = значение из Price (вложенный элемент AccountPrice ответа с сайта НБРБ)
    # :assert: JEWEL_RATE_HISTORY.JRH_AGENCY_ID = 1 (агентство с кодом 000000)
    # :assert: JEWEL_RATE_HISTORY.JRH_CURRENCY_ISO_CODE = 933
    # :assert: JEWEL_RATE_HISTORY.JRH_JEWEL_ID = JEWELS.J_ID, у которого JEWELS.J_NOMINAL = 1, JEWELS.J_GROUP равным JEWEL_GROUP.JG_ID при JEWEL_GROUP.JG_IDNBRB = MetalId
    # :assert: JRH_AGENCY_ID .JRH_RATE_TYPE_ID = JEWEL_RATE_TYPE.JRT_ID
    # :assert: После передачи курсов в кассовое решение JEWEL_RATE_HISTORY.JRH_EXPORT =0 изменилось на JEWEL_RATE_HISTORY.JRH_EXPORT =1 (для курсов на 07.12.2021)
    # :assert: Переданные курсы фиксируются в TRADE_TERMS кассового решения


    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)