# 56376 Выполнить доработку ЦСВКВ по получению информации по заявкам на валютном рынке

@pytest.mark.skip(reason="Template")
def test_56376_1(app, credo_db, forpost_db):
    """
    {#
        :id:                56376_1
        :priority:          Средний
        :module:            Ядро/Курсы
        :description:       Проверка создания справочника инструментов валютного рынка (bsce_instruments)
        :precondition:      Таблица bsce_instruments заполнена данными
        :comment:           Скрипт для заполнения таблицы bsce_instruments прикреплён к задаче по тестированию
        :source_point:      RM56376_Приложение_2;
        :tc_type:           +
        :db_env:            БД: Node9_Rates;
        :client_env:        Google Chrome 92 [Windows 10; openSuSE Linux Leap 15.3]
        :client_env:        Mozilla Firefox 91 [Windows 10; openSuSE Linux Leap 15.3]
        :client_env:        Microsoft EDGE 92 [Windows 10]
        :time_of_test:      240
        :precondition_time: 20
        :count_of_check:    19
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

    # :step: В базе данных открываем таблицу bsce_instruments
    # :assert: В таблице содержится столбец InstrumentCodes. Тип данных - целочисленное значение
    # :assert: В таблице содержится столбец InstrumentName. Тип данных - символьное значение
    # :assert: В таблице содержится столбец CurrCodes. Тип данных - целочисленное значение
    # :assert: В таблице содержится столбец AttendedCurrCodes. Тип данных - целочисленное значение
    # :assert: В таблице содержится столбец InstrumentStatus. Тип данных - одним из значений (1 или 0 или -1)
    # :assert: В таблице содержится столбец TradeModeId. Тип данных - целочисленное значение
    # :assert: В таблице содержится столбец TradeMode. Тип данных - символьное значение (с русскими буквами)
    # :assert: В таблице содержится столбец PaymentCodeId. Тип данных - целочисленное значение
    # :assert: В таблице содержится столбец PaymentCode. Тип данных - символьное значение
    # :assert: В таблице содержится столбец LotSize. Тип данных - целочисленное значение
    # :assert: В таблице содержится столбец PriceIncrement. Тип данных - числовое значение
    # :assert: В таблице содержится столбец RateCoef. Тип данных - целочисленное значение
    # :assert: В таблице содержится столбец Rate. Тип данных - числовое значение
    # :assert: В таблице содержится столбец RateN. Тип данных - числовое значение
    # :assert: В таблице содержится столбец PayTerm. Тип данных - целочисленное значение
    # :assert: В таблице содержится столбец PayTerm2. Тип данных - целочисленное значение
    # :assert: В таблице содержится столбец RATETYPEBUY. Тип данных - символьное значение
    # :assert: В таблице содержится столбец RATETYPESELL. Тип данных - символьное значение
    # :assert: В таблице содержится столбец PRTY. Тип данных - числовое значение

    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


@pytest.mark.skip(reason="Template")
def test_56376_2(app, credo_db, forpost_db):
    """
    {#
        :id:                56376_2
        :priority:          Средний
        :module:            Ядро/Курсы
        :description:       Проверка создания таблицы хранения информации по заявкам на валютном рынке (bsce_request)
        :precondition:      Таблица bsce_instruments заполнена данными
        :source_point:      RM56376_Приложение_1;
        :tc_type:           +
        :db_env:            БД: Node9_Rates;
        :client_env:        Google Chrome 92 [Windows 10; openSuSE Linux Leap 15.3]
        :client_env:        Mozilla Firefox 91 [Windows 10; openSuSE Linux Leap 15.3]
        :client_env:        Microsoft EDGE 92 [Windows 10]
        :time_of_test:      30
        :precondition_time: 20
        :count_of_check:    15
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

    # :step: В базе данных открываем таблицу bsce_request
    # :assert: В таблице содержится столбец REQUESTID. Тип данных - целочисленное значение
    # :assert: В таблице содержится столбец REQUESTDATETIME. Тип данных - дата(дд.мм.гггг чч:мм:сс)
    # :assert: В таблице содержится столбец DIRECTION. Тип данных - символьное значение
    # :assert: В таблице содержится столбец TRADEMODEID. Тип данных - целочисленное значение
    # :assert: В таблице содержится столбец INSTRUMENTCODES. Тип данных - целочисленное значение
    # :assert: В таблице содержится столбец CURRCODES. Тип данных - целочисленное значение
    # :assert: В таблице содержится столбец ATTENDEDCURRCODES. Тип данных - целочисленное значение
    # :assert: В таблице содержится столбец RATE. Тип данных - целочисленное значение
    # :assert: В таблице содержится столбец VOLUMECURR. Тип данных - целочисленное значение
    # :assert: В таблице содержится столбец VOLUMEATTENDEDCURR. Тип данных - целочисленное значение
    # :assert: В таблице содержится столбец PRICEINCREMENT. Тип данных - целочисленное значение
    # :assert: В таблице содержится столбец TYPE. Тип данных - символьное значение
    # :assert: В таблице содержится столбец PAYTERM. Тип данных - целочисленное значение
    # :assert: В таблице содержится столбец PAYTERM2. Тип данных - целочисленное значение
    # :assert: В таблице содержится столбец BR_DUID. Тип данных - дата(дд.мм.гггг чч:мм:сс)


    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


@pytest.mark.skip(reason="Template")
def test_56376_3(app, credo_db, forpost_db):
    """
    {#
        :id:                56376_3
        :priority:          Средний
        :module:            Ядро/Курсы
        :description:       Проверка добавления новых параметров конфигурации, полей CONFIG.CONF_UID (пользователь, внёсший изменения) и CONFIG.CONF_DUID (дата и время внесения последних изменений).
        :precondition:      Пользователь admin авторизован
        :source_point:      RM56376_Приложение_3;
        :tc_type:           +
        :db_env:            БД: Node9_Rates;
        :client_env:        Google Chrome 92 [Windows 10; openSuSE Linux Leap 15.3]
        :client_env:        Mozilla Firefox 91 [Windows 10; openSuSE Linux Leap 15.3]
        :client_env:        Microsoft EDGE 92 [Windows 10]
        :time_of_test:      30
        :precondition_time: 20
        :count_of_check:    8
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

    # :step: Переходим во вкладку "Конфигурация"

    # :newpage: #######################################################################################################

    # :assert: Параметр bsce.from "Начало торгов на валютном рынке (hh24:mi)" = 12:00. В таблице CONFIG для CONFIG.CONF_KEY = bsce.from заполнены CONFIG.CONF_UID, CONFIG.CONF_DUID.
    # :assert: Параметр bsce.till "Окончание торгов на валютном рынке (hh24:mi)" = 16:00. В таблице CONFIG для  CONFIG.CONF_KEY = bsce.till заполнены CONFIG.CONF_UID, CONFIG.CONF_DUID
    # :assert: Параметр bsce.interval "Время между запросами валютного стакана, сек" = 15. В таблице CONFIG для CONFIG.CONF_KEY = bsce.interval заполнены CONFIG.CONF_UID, CONFIG.CONF_DUID
    # :assert: Параметр bsce.tradeModes "Идентификатор режима торгов" не заполнен. В таблице CONFIG для CONFIG.CONF_KEY = bsce.trademodes заполнены CONFIG.CONF_UID, CONFIG.CONF_DUID
    # :assert: Параметр bsce.instrumentCodes "Код финансового инструмента" не заполнен. В таблице CONFIG для CONFIG.CONF_KEY = bsce.instrumentcodes заполнены CONFIG.CONF_UID, CONFIG.CONF_DUID
    # :assert: Параметр bsce.token "Токен авторизации для курсов БВФБ" не заполнен. В таблице CONFIG для CONFIG.CONF_KEY = bsce.token  заполнены CONFIG.CONF_UID, CONFIG.CONF_DUID

    # :step: В поле "Токен авторизации для курсов БВФБ" вводим значение
    value = '56465798749987984654949494'
    # :step: В поле "Время между запросами валютного стакана, сек" изменяем значение
    value = '30'
    # :step: Нажимаем кнопку "Сохранить"
    # :assert: В таблице CONFIG значения CONFIG.CONF_UID для CONFIG.CONF_KEY = bsce.token и CONFIG.CONF_KEY = bsce.interval обновились
    # :assert: В таблице CONFIG значение CONFIG.CONF_DUID для CONFIG.CONF_KEY = bsce.token и CONFIG.CONF_KEY = bsce.interval обновились


    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


@pytest.mark.skip(reason="Template")
def test_56376_4(app, credo_db, forpost_db):
    """
    {#
        :id:                56376_4
        :priority:          Средний
        :module:            Ядро/Курсы
        :description:       Проверка отправки писем с ошибками
        :precondition:      В конфигурации время начала торгов "00:00" и время окончания торгов "23:59"
        :precondition:      Пользователь admin авторизован
        :precondition:      Только у активного пользователя AMakarevich присутствует роль Administrators и уникальная почта (levdanskij@bgpb.by)
        :precondition:      К роли Administrators привязан Email (Administrators56376@bgpb.by) отличный от Email пользователя с ролью Administrators
        :precondition:      Параметр "Время между запросами валютного стакана, сек" (bsce.interval) = 15
        :precondition:      Таблица bsce_instruments заполнена данными
        :source_point:      RM56376_Ф.01_Ф.02;
        :tc_type:           +
        :db_env:            БД: Node9_Rates;
        :client_env:        Google Chrome 92 [Windows 10; openSuSE Linux Leap 15.3]
        :client_env:        Mozilla Firefox 91 [Windows 10; openSuSE Linux Leap 15.3]
        :client_env:        Microsoft EDGE 92 [Windows 10]
        :time_of_test:      60
        :precondition_time: 20
        :count_of_check:    3
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

    # :step: В файле BSCEGetSecurityToken_out.xsl удаляем строку <?xml version="1.0" encoding="UTF-8"?>
    # :step: Переходим во вкладку "Конфигурация"

    # :newpage: #######################################################################################################

    # :step: В поле "Токен авторизации для курсов БВФБ" (bsce.token) меняем значение на невалидное
    value = '56465798749987984654949494'
    # :step: Нажимаем кнопку "Сохранить"
    # :assert: Ошибка обновления токена авторизации. Значение параметра «Токен авторизации для курсов БВФБ» не изменилось.Пользователю с ролью "Administrators" отправилось сообщение об ошибке
    # :step: В файле BSCEGetSecurityToken_out.xsl возвращаем строку <?xml version="1.0" encoding="UTF-8"?>

    # :step: В файле BSCEGetRequestCurrencyOnline_out.xsl удаляем строку <?xml version="1.0" encoding="UTF-8"?>
    # :step: Очищаем поле "Токен авторизации для курсов БВФБ" (bsce.token)
    value = ''
    # :step: Нажимаем кнопку "Сохранить"
    # :assert: Ошибка выполнения запроса получения заявок, не содержащая слова «User claims not received». Пользователю с ролью "Administrators" отправилось сообщение об ошибке(содержащее значение из Message и из Details)
    # :step: В файле BSCEGetRequestCurrencyOnline_out.xsl возвращаем строку <?xml version="1.0" encoding="UTF-8"?>

    # :step: В триггере rate_history_rh_ID_TRG удаляем строку "TRIGGER "rate_history_rh_ID_TRG" BEFORE INSERT ON rate_history"
    # :assert: Ошибка сохранения информации в rate_history. Пользователю с ролью "Administrators" отправилось сообщение об ошибке


    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


@pytest.mark.skip(reason="Template")
def test_56376_5(app, credo_db, forpost_db):
    """
    {#
        :id:                56376_5
        :priority:          Средний
        :module:            Ядро/Курсы
        :description:       Проверка процесса обновления токена авторизации
        :precondition:      В конфигурации время начала торгов "00:00" и время окончания торгов "23:59"
        :precondition:      Пользователь admin авторизован
        :precondition:      Параметр "Время между запросами валютного стакана, сек" (bsce.interval) = 15
        :precondition:      Таблица bsce_instruments заполнена данными
        :comment:           Текущее время "10:00"
        :comment:           При изменении bsce.interval чтобы подхватился конфигурационный параметр необходимо перезапустить сервер
        :source_point:      RM56376_Ф.01;
        :tc_type:           +
        :db_env:            БД: Node9_Rates;
        :client_env:        Google Chrome 92 [Windows 10; openSuSE Linux Leap 15.3]
        :client_env:        Mozilla Firefox 91 [Windows 10; openSuSE Linux Leap 15.3]
        :client_env:        Microsoft EDGE 92 [Windows 10]
        :time_of_test:      480
        :precondition_time: 20
        :count_of_check:    8
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

    # :step: Переходим во вкладку "Конфигурация"

    # :newpage: #######################################################################################################

    # :step: Очищаем поле "Токен авторизации для курсов БВФБ" (bsce.token)
    value = ''
    # :step: Нажимаем кнопку "Сохранить"
    # :step: Обновляем страницу через 15 секунд
    # :assert: Поле "Токен авторизации для курсов БВФБ" (bsce.token) заполнилось

    # :step: Очищаем поле "Токен авторизации для курсов БВФБ" (bsce.token)
    value = ''
    # :step: В поле "Начало торгов на валютном рынке (hh24:mi)" (bsce.from) устанавливаем время больше текущего на 1 минуту
    value = '10:01'
    # :step: Нажимаем кнопку "Сохранить"
    # :step: Обновляем страницу
    # :assert: Запрос на получение заявки не производился
    # :assert: Поле "Токен авторизации для курсов БВФБ" (b08sce.token) не заполнилось

    # :step: В поле "Окончание торгов на валютном рынке (hh24:mi)" (bsce.till) устанавливаем время меньше текущего на 1 минуту
    value = '09:59'
    # :step: Нажимаем кнопку "Сохранить"
    # :step: Обновляем страницу
    # :assert: Запрос на получение заявки не производился
    # :assert: Поле "Токен авторизации для курсов БВФБ" (bsce.token) не заполнилось

    # :step: В поле "Начало торгов на валютном рынке (hh24:mi)" (bsce.from) устанавливаем время равное текущему
    value = '10:00'
    # :step: Нажимаем кнопку "Сохранить"
    # :step: Обновляем страницу через 15 секунд
    # :assert: Поле "Токен авторизации для курсов БВФБ" (bsce.token) заполнилось

    # :step: Очищаем поле "Токен авторизации для курсов БВФБ" (bsce.token)
    value = ''
    # :step: В поле "Окончание торгов на валютном рынке (hh24:mi)" (bsce.till) устанавливаем время равное текущему
    value = '10:00'
    # :step: Нажимаем кнопку "Сохранить"
    # :step: Обновляем страницу через 15 секунд
    # :assert: Поле "Токен авторизации для курсов БВФБ" (bsce.token) не заполнилось

    # :step: В поле "Токен авторизации для курсов БВФБ" (bsce.token) меняем значение на невалидное
    value = '56465798749987984654949494'
    # :step: В поле "Начало торгов на валютном рынке (hh24:mi)" (bsce.from) устанавливаем время меньше текущего
    value = '07:00'
    # :step: В поле "Окончание торгов на валютном рынке (hh24:mi)" (bsce.till) устанавливаем время больше текущего
    value = '17:00'
    # :step: Нажимаем кнопку "Сохранить"
    # :step: Обновляем страницу через 15 секунд
    # :assert: Поле "Токен авторизации для курсов БВФБ" (bsce.token) заполнилось валидным токеном


    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


@pytest.mark.skip(reason="Template")
def test_56376_6(app, credo_db, forpost_db):
    """
    {#
        :id:                56376_6
        :priority:          Средний
        :module:            Ядро/Курсы
        :description:       Проверка определения и установки оптимального курса валют
        :precondition:      В конфигурации время начала торгов "00:00" и время окончания торгов "23:59"
        :precondition:      Пользователь admin авторизован
        :precondition:      Параметр "Время между запросами валютного стакана, сек" (bsce.interval) = 15
        :precondition:      Создан тип курса курс покупки для биржи мнемоника test1 с id курса 55
        :precondition:      Создан тип курса курс продажи для биржи мнемоника test2 с id курса 79
        :precondition:      В таблице bsce_instruments для инструмента с кодом 1077 ratetypebuy = test1
        :precondition:      В таблице bsce_instruments для инструмента с кодом 1077 ratetypesell = test2
        :precondition:      В таблице bsce_instruments для инструмента с кодом 1076 ratetypebuy = test1
        :precondition:      В таблице bsce_instruments для инструмента с кодом 1076 ratetypesell = test2
        :precondition:      В таблице bsce_instruments для инструмента с кодом 1078 ratetypebuy = test1
        :precondition:      В таблице bsce_instruments для инструмента с кодом 1078 ratetypesell = test2
        :precondition:      В таблице bsce_instruments для инструмента с кодом 1077 установлена пара валют USD/BYN (CURRCODE = 840, ATTENDEDCURRCODE = 933)
        :precondition:      В таблице bsce_instruments для инструмента с кодом 1076 установлена пара валют EUR/BYN (CURRCODE = 978, ATTENDEDCURRCODE = 933)
        :precondition:      В таблице bsce_instruments для инструмента с кодом 1078 установлена пара валют RUB/BYN (CURRCODE = 643, ATTENDEDCURRCODE = 933)
        :precondition:      В таблице bsce_instruments для инструмента с кодом 1077 установлено значение TRADEMODEID = 1
        :precondition:      В таблице bsce_instruments для инструмента с кодом 1076 установлено значение TRADEMODEID = 2
        :precondition:      В таблице bsce_instruments для инструмента с кодом 1078 установлено значение TRADEMODEID = 3
        :precondition:      Таблица bsce_instruments заполнена данными
        :comment:           Ответ от сервиса валютной биржи получаем с помощью эумулятора - в системе 9 заявок
        :source_point:      RM56376_Приложение_3;
        :tc_type:           +
        :db_env:            БД: Node9_Rates;
        :client_env:        Google Chrome 92 [Windows 10; openSuSE Linux Leap 15.3]
        :client_env:        Mozilla Firefox 91 [Windows 10; openSuSE Linux Leap 15.3]
        :client_env:        Microsoft EDGE 92 [Windows 10]
        :time_of_test:      480
        :precondition_time: 20
        :count_of_check:    23
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

    # :step: Переходим во вкладку "Конфигурация"

    # :newpage: #######################################################################################################

    # :step: Параметр "Код финансового инструмента" (bsce.instrumentCodes) оставляем пустым
    value = ''
    # :step: Параметр "Идентификатор режима торгов" (bsce.tradeModes) оставляем пустым
    value = ''
    # :step: Нажимаем кнопку "Сохранить"
    # :assert: В таблице bsce_requests сохраняются записи по всем заявкам для каждого INSTRUMENTCODES и TRADEMODEID - 9 штук
    # :assert: В rate_history сохраняются записи с оптимальными курсами - 6 штук
    # :assert: В rate_history.rh_rate для EUR/BYN сохранён курс покупки равный минимальному значению среди заявок из bsce_request с direction = B
    # :assert: В rate_history.rh_rate для EUR/BYN сохранён курс продажи равный максимальному значению среди заявок из bsce_request с direction = S
    # :assert: В rate_history.rh_rate для USD/BYN сохранён курс покупки равный минимальному значению среди заявок из bsce_request с direction = B
    # :assert: В rate_history.rh_rate для USD/BYN сохранён курс продажи равный максимальному значению среди заявок из bsce_request с direction = S
    # :assert: В rate_history.rh_rate для RUB/BYN сохранён курс покупки равный минимальному значению среди заявок из bsce_request с direction = B
    # :assert: В rate_history.rh_rate для RUB/BYN сохранён курс продажи равный максимальному значению среди заявок из bsce_request с direction = S
    # :assert: В поле rate_history.rh_rate_begin отображается дата и время
    # :assert: В поле rate_history.rh_ag_id = 1
    # :assert: В поле rate_history.rh_crnc_code = bsce_instruments.currcodes для соответствующей пары валют
    # :assert: В поле rate_history.rh_base_crnc_code = bsce_instruments.attendedCurrCodes для соответствующей пары валют
    # :assert: В поле rate_history.rh_units = bsce_instruments.ratecoef для соответствующей пары валют
    # :assert: В поле rate_history.rh_limit максимально возможное значение лимита = 999999999999999
    # :assert: В поле rate_history.rh_export = 1 (передача данных в другие системы не производится)

    # :step: Параметр "Код финансового инструмента" (bsce.instrumentCodes) заполняем
    value = '1076,1077,1078'
    # :step: Параметр "Идентификатор режима торгов" (bsce.tradeModes) заполняем
    value = '2,3'
    # :assert: В таблице bsce_requests сохраняются записи по заявкам для INSTRUMENTCODES со значениями 1076,1078 и TRADEMODEID со значениями 2,3
    # :assert: В rate_history для EUR/BYN сохранён курс покупки равный минимальному значению среди заявок из bsce_request с direction = B
    # :assert: В rate_history для EUR/BYN сохранён курс продажи равный максимальному значению среди заявок из bsce_request с direction = S
    # :assert: В rate_history для RUB/BYN сохранён курс покупки равный минимальному значению среди заявок из bsce_request с direction = B
    # :assert: В rate_history для RUB/BYN сохранён курс продажи равный максимальному значению среди заявок из bsce_request с direction = S


    # :step: Параметр "Код финансового инструмента" (bsce.instrumentCodes) заполняем
    value = '1076,1078'
    # :step: Параметр "Идентификатор режима торгов" (bsce.tradeModes) заполняем
    value = '1'
    # :assert: В таблице bsce_requests отсутствуют записи

    # :step: Параметр "Код финансового инструмента" (bsce.instrumentCodes) оставляем пустым
    value = ''
    # :step: Параметр "Идентификатор режима торгов" (bsce.tradeModes) заполняем
    value = '1'
    # :assert: В таблице bsce_requests сохраняются записи по заявкам для INSTRUMENTCODES со значением 1077 и TRADEMODEID со значением 1
    # :assert: В rate_history.rh_rate для USD/BYN сохранён курс покупки равный минимальному значению среди заявок из bsce_request с direction = B
    # :assert: В rate_history.rh_rate для USD/BYN сохранён курс продажи равный максимальному значению среди заявок из bsce_request с direction = S


    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)
///