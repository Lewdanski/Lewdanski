@pytest.mark.skip(reason="Template")
def test_57458_1(app, db_credo):
    """
    {#
        :id:                57458_1
        :priority:          Средний
        :module:            ЕФР
        :description:       Ошибка при создании заявки
        :precondition:      Пользователь авторизирован в СКЗ. Параметр пользователя using_scanner (Доступность сканирования) = "да"
        :precondition:      Тестовый клиент существует в ЕРК, все ключевые данные присутствуют
        :precondition:      Станция администратора сканирования, внешние серверы SmartCapture и контент-сервер запущены
        :precondition:      Справочник «Типы документов удостоверяющих личность для выбора при сканировании» (docTypesForScan) заполнен
        :precondition:      Параметр пользователя using_scanner (Доступность сканирования) = "да".
        :precondition:      В файле itwCredo-scanner.properties присутствует параметр с путём к файлу "fake_response scanner.fakeresponsefile=d:/fake_response.xml"
        :precondition:      в itwCredo-scanner.properties прописаны scanner.proxy.host, scanner.proxy.port
        :precondition:      В файле fake_response.xml установлена дата рождения: "-25.05.1999"
        :precondition:      В файле fake_response.xml установлена дата выдачи:   "-25.05.1999"
        :precondition:      В файле fake_response.xml установлен срок действия:  "-25.05.1999"
        :comment:           Тестовые случаи моделировали через использование файла fake_response.xml
        :comment:           Пример файла прикреплён к задаче
        :source_point:      RM_57458
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 09.12.2021
        :client_env:        Google Chrome 97 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 97 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 97 [Windows 10; openSuSE Linux Leap 15.1]
        :precondition_time: 10
        :time_of_test:      10
        :count_of_check:    4
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'changing_customer'
    VARIANT = 'CustomerCard'

    # :newpage: #######################################################################################################

    # :step: На форме "Поиск карточки клиента в учетной системе Банка" нажимаем кнопку-список «Сканировать документ»

    # :step: Из списка ДУЛ кнопки «Сканировать документ» выбираем сканируемый документ
    value = 'Паспорт гражданина РБ'

    # :newpage: #######################################################################################################

    # :step: В диалоговом окне с предложением отсканировать следующую страницу документа нажимаем кнопку "Да"

    # :newpage: #######################################################################################################

    # :step: На форме "Поиск клиента" с результатами поиска нажимаем на найденную краткую карточку клиента

    # :newpage: #######################################################################################################

    # :step: На форме "Данные клиента" нажимаем кнопку "Изменить"

    # :newpage: #######################################################################################################

    # :assert: Поле "Дата рождения" очищено
    # :assert: Поле "Дата выдачи" очищено
    # :assert: Поле "Срок действия документа" очищено
    # :assert: В request.log в параметре клиента scanner_data переданы данные из fake_response.xml


    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


@pytest.mark.skip(reason="Template")
def test_57458_2(app, db_credo):
    """
    {#
        :id:                57458_2
        :priority:          Средний
        :module:            ЕФР
        :description:       Ошибка при создании заявки
        :precondition:      Пользователь авторизирован в СКЗ. Параметр пользователя using_scanner (Доступность сканирования) = "да"
        :precondition:      Тестовый клиент существует в ЕРК, все ключевые данные присутствуют
        :precondition:      Станция администратора сканирования, внешние серверы SmartCapture и контент-сервер запущены
        :precondition:      Справочник «Типы документов удостоверяющих личность для выбора при сканировании» (docTypesForScan) заполнен
        :precondition:      Параметр пользователя using_scanner (Доступность сканирования) = "да".
        :precondition:      В файле itwCredo-scanner.properties присутствует параметр с путём к файлу "fake_response scanner.fakeresponsefile=d:/fake_response.xml"
        :precondition:      в itwCredo-scanner.properties прописаны scanner.proxy.host, scanner.proxy.port
        :precondition:      В файле fake_response.xml установлена дата рождения: "Текст"
        :precondition:      В файле fake_response.xml установлена дата выдачи:   "Текст"
        :precondition:      В файле fake_response.xml установлен срок действия:  "Текст"
        :comment:           Тестовые случаи моделировали через использование файла fake_response.xml
        :comment:           Пример файла прикреплён к задаче
        :source_point:      RM_57458
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 09.12.2021
        :client_env:        Google Chrome 97 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 97 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 97 [Windows 10; openSuSE Linux Leap 15.1]
        :precondition_time: 10
        :time_of_test:      10
        :count_of_check:    4
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'changing_customer'
    VARIANT = 'CustomerCard'

    # :newpage: #######################################################################################################

    # :step: На форме "Поиск карточки клиента в учетной системе Банка" нажимаем кнопку-список «Сканировать документ»

    # :step: Из списка ДУЛ кнопки «Сканировать документ» выбираем сканируемый документ
    value = 'Паспорт гражданина РБ'

    # :newpage: #######################################################################################################

    # :step: В диалоговом окне с предложением отсканировать следующую страницу документа нажимаем кнопку "Да"

    # :newpage: #######################################################################################################

    # :step: На форме "Поиск клиента" с результатами поиска нажимаем на найденную краткую карточку клиента

    # :newpage: #######################################################################################################

    # :step: На форме "Данные клиента" нажимаем кнопку "Изменить"

    # :newpage: #######################################################################################################

    # :assert: Поле "Дата рождения" очищено
    # :assert: Поле "Дата выдачи" очищено
    # :assert: Поле "Срок действия документа" очищено
    # :assert: В request.log в параметре клиента scanner_data переданы данные из fake_response.xml


    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


@pytest.mark.skip(reason="Template")
def test_57458_3(app, db_credo):
    """
    {#
        :id:                57458_3
        :priority:          Средний
        :module:            ЕФР
        :description:       Ошибка при создании заявки
        :precondition:      Пользователь авторизирован в СКЗ. Параметр пользователя using_scanner (Доступность сканирования) = "да"
        :precondition:      Тестовый клиент существует в ЕРК, все ключевые данные присутствуют
        :precondition:      Станция администратора сканирования, внешние серверы SmartCapture и контент-сервер запущены
        :precondition:      Справочник «Типы документов удостоверяющих личность для выбора при сканировании» (docTypesForScan) заполнен
        :precondition:      Параметр пользователя using_scanner (Доступность сканирования) = "да".
        :precondition:      В файле itwCredo-scanner.properties присутствует параметр с путём к файлу "fake_response scanner.fakeresponsefile=d:/fake_response.xml"
        :precondition:      в itwCredo-scanner.properties прописаны scanner.proxy.host, scanner.proxy.port
        :precondition:      В файле fake_response.xml установлена дата рождения: "!@#$%^&?*()-=+\/][{}'<>.,"
        :precondition:      В файле fake_response.xml установлена дата выдачи:   "!@#$%^&?*()-=+\/][{}'<>.,"
        :precondition:      В файле fake_response.xml установлен срок действия:  "!@#$%^&?*()-=+\/][{}'<>.,"
        :comment:           Тестовые случаи моделировали через использование файла fake_response.xml
        :comment:           Пример файла прикреплён к задаче
        :source_point:      RM_57458
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 09.12.2021
        :client_env:        Google Chrome 97 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 97 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 97 [Windows 10; openSuSE Linux Leap 15.1]
        :precondition_time: 10
        :time_of_test:      10
        :count_of_check:    4
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'changing_customer'
    VARIANT = 'CustomerCard'

    # :newpage: #######################################################################################################

    # :step: На форме "Поиск карточки клиента в учетной системе Банка" нажимаем кнопку-список «Сканировать документ»

    # :step: Из списка ДУЛ кнопки «Сканировать документ» выбираем сканируемый документ
    value = 'Паспорт гражданина РБ'

    # :newpage: #######################################################################################################

    # :step: В диалоговом окне с предложением отсканировать следующую страницу документа нажимаем кнопку "Да"

    # :newpage: #######################################################################################################

    # :step: На форме "Поиск клиента" с результатами поиска нажимаем на найденную краткую карточку клиента

    # :newpage: #######################################################################################################

    # :step: На форме "Данные клиента" нажимаем кнопку "Изменить"

    # :newpage: #######################################################################################################

    # :assert: Поле "Дата рождения" очищено
    # :assert: Поле "Дата выдачи" очищено
    # :assert: Поле "Срок действия документа" очищено
    # :assert: В request.log в параметре клиента scanner_data переданы данные из fake_response.xml


    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


@pytest.mark.skip(reason="Template")
def test_57458_4(app, db_credo):
    """
    {#
        :id:                57458_4
        :priority:          Средний
        :module:            ЕФР
        :description:       Ошибка при создании заявки
        :precondition:      Пользователь авторизирован в СКЗ. Параметр пользователя using_scanner (Доступность сканирования) = "да"
        :precondition:      Тестовый клиент существует в ЕРК, все ключевые данные присутствуют
        :precondition:      Станция администратора сканирования, внешние серверы SmartCapture и контент-сервер запущены
        :precondition:      Справочник «Типы документов удостоверяющих личность для выбора при сканировании» (docTypesForScan) заполнен
        :precondition:      Параметр пользователя using_scanner (Доступность сканирования) = "да".
        :precondition:      В файле itwCredo-scanner.properties присутствует параметр с путём к файлу "fake_response scanner.fakeresponsefile=d:/fake_response.xml"
        :precondition:      в itwCredo-scanner.properties прописаны scanner.proxy.host, scanner.proxy.port
        :precondition:      В файле fake_response.xml установлена дата рождения: "    "
        :precondition:      В файле fake_response.xml установлена дата выдачи:   "    "
        :precondition:      В файле fake_response.xml установлен срок действия:  "    "
        :comment:           Тестовые случаи моделировали через использование файла fake_response.xml
        :comment:           Пример файла прикреплён к задаче
        :source_point:      RM_57458
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 09.12.2021
        :client_env:        Google Chrome 97 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 97 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 97 [Windows 10; openSuSE Linux Leap 15.1]
        :precondition_time: 10
        :time_of_test:      10
        :count_of_check:    4
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'changing_customer'
    VARIANT = 'CustomerCard'

    # :newpage: #######################################################################################################

    # :step: На форме "Поиск карточки клиента в учетной системе Банка" нажимаем кнопку-список «Сканировать документ»

    # :step: Из списка ДУЛ кнопки «Сканировать документ» выбираем сканируемый документ
    value = 'Паспорт гражданина РБ'

    # :newpage: #######################################################################################################

    # :step: В диалоговом окне с предложением отсканировать следующую страницу документа нажимаем кнопку "Да"

    # :newpage: #######################################################################################################

    # :step: На форме "Поиск клиента" с результатами поиска нажимаем на найденную краткую карточку клиента

    # :newpage: #######################################################################################################

    # :step: На форме "Данные клиента" нажимаем кнопку "Изменить"

    # :newpage: #######################################################################################################

    # :assert: Поле "Дата рождения" очищено
    # :assert: Поле "Дата выдачи" очищено
    # :assert: Поле "Срок действия документа" очищено
    # :assert: В request.log в параметре клиента scanner_data переданы данные из fake_response.xml


    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


@pytest.mark.skip(reason="Template")
def test_57458_5(app, db_credo):
    """
    {#
        :id:                57458_5
        :priority:          Средний
        :module:            ЕФР
        :description:       Ошибка при создании заявки
        :precondition:      Пользователь авторизирован в СКЗ. Параметр пользователя using_scanner (Доступность сканирования) = "да"
        :precondition:      Тестовый клиент существует в ЕРК, все ключевые данные присутствуют
        :precondition:      Станция администратора сканирования, внешние серверы SmartCapture и контент-сервер запущены
        :precondition:      Справочник «Типы документов удостоверяющих личность для выбора при сканировании» (docTypesForScan) заполнен
        :precondition:      Параметр пользователя using_scanner (Доступность сканирования) = "да".
        :precondition:      В файле itwCredo-scanner.properties присутствует параметр с путём к файлу "fake_response scanner.fakeresponsefile=d:/fake_response.xml"
        :precondition:      в itwCredo-scanner.properties прописаны scanner.proxy.host, scanner.proxy.port
        :precondition:      В файле fake_response.xml установлена дата рождения: "25051999"
        :precondition:      В файле fake_response.xml установлена дата выдачи:   "25051999"
        :precondition:      В файле fake_response.xml установлен срок действия:  "25051999"
        :comment:           Тестовые случаи моделировали через использование файла fake_response.xml
        :comment:           Пример файла прикреплён к задаче
        :source_point:      RM_57458
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 09.12.2021
        :client_env:        Google Chrome 97 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 97 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 97 [Windows 10; openSuSE Linux Leap 15.1]
        :precondition_time: 10
        :time_of_test:      10
        :count_of_check:    4
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'changing_customer'
    VARIANT = 'CustomerCard'

    # :newpage: #######################################################################################################

    # :step: На форме "Поиск карточки клиента в учетной системе Банка" нажимаем кнопку-список «Сканировать документ»

    # :step: Из списка ДУЛ кнопки «Сканировать документ» выбираем сканируемый документ
    value = 'Паспорт гражданина РБ'

    # :newpage: #######################################################################################################

    # :step: В диалоговом окне с предложением отсканировать следующую страницу документа нажимаем кнопку "Да"

    # :newpage: #######################################################################################################

    # :step: На форме "Поиск клиента" с результатами поиска нажимаем на найденную краткую карточку клиента

    # :newpage: #######################################################################################################

    # :step: На форме "Данные клиента" нажимаем кнопку "Изменить"

    # :newpage: #######################################################################################################

    # :assert: Поле "Дата рождения" очищено
    # :assert: Поле "Дата выдачи" очищено
    # :assert: Поле "Срок действия документа" очищено
    # :assert: В request.log в параметре клиента scanner_data переданы данные из fake_response.xml


    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


@pytest.mark.skip(reason="Template")
def test_57458_6(app, db_credo):
    """
    {#
        :id:                57458_6
        :priority:          Средний
        :module:            ЕФР
        :description:       Ошибка при создании заявки
        :precondition:      Пользователь авторизирован в СКЗ. Параметр пользователя using_scanner (Доступность сканирования) = "да"
        :precondition:      Тестовый клиент существует в ЕРК, все ключевые данные присутствуют
        :precondition:      Станция администратора сканирования, внешние серверы SmartCapture и контент-сервер запущены
        :precondition:      Справочник «Типы документов удостоверяющих личность для выбора при сканировании» (docTypesForScan) заполнен
        :precondition:      Параметр пользователя using_scanner (Доступность сканирования) = "да".
        :precondition:      В файле itwCredo-scanner.properties присутствует параметр с путём к файлу "fake_response scanner.fakeresponsefile=d:/fake_response.xml"
        :precondition:      в itwCredo-scanner.properties прописаны scanner.proxy.host, scanner.proxy.port
        :precondition:      В файле fake_response.xml установлена дата рождения: "255.05.1999"
        :precondition:      В файле fake_response.xml установлена дата выдачи:   "255.05.1999"
        :precondition:      В файле fake_response.xml установлен срок действия:  "255.05.1999"
        :comment:           Тестовые случаи моделировали через использование файла fake_response.xml
        :comment:           Пример файла прикреплён к задаче
        :source_point:      RM_57458
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 09.12.2021
        :client_env:        Google Chrome 97 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 97 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 97 [Windows 10; openSuSE Linux Leap 15.1]
        :precondition_time: 10
        :time_of_test:      10
        :count_of_check:    4
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'changing_customer'
    VARIANT = 'CustomerCard'

    # :newpage: #######################################################################################################

    # :step: На форме "Поиск карточки клиента в учетной системе Банка" нажимаем кнопку-список «Сканировать документ»

    # :step: Из списка ДУЛ кнопки «Сканировать документ» выбираем сканируемый документ
    value = 'Паспорт гражданина РБ'

    # :newpage: #######################################################################################################

    # :step: В диалоговом окне с предложением отсканировать следующую страницу документа нажимаем кнопку "Да"

    # :newpage: #######################################################################################################

    # :step: На форме "Поиск клиента" с результатами поиска нажимаем на найденную краткую карточку клиента

    # :newpage: #######################################################################################################

    # :step: На форме "Данные клиента" нажимаем кнопку "Изменить"

    # :newpage: #######################################################################################################

    # :assert: Поле "Дата рождения" очищено
    # :assert: Поле "Дата выдачи" очищено
    # :assert: Поле "Срок действия документа" очищено
    # :assert: В request.log в параметре клиента scanner_data переданы данные из fake_response.xml


    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


@pytest.mark.skip(reason="Template")
def test_57458_7(app, db_credo):
    """
    {#
        :id:                57458_7
        :priority:          Средний
        :module:            ЕФР
        :description:       Ошибка при создании заявки
        :precondition:      Пользователь авторизирован в СКЗ. Параметр пользователя using_scanner (Доступность сканирования) = "да"
        :precondition:      Тестовый клиент существует в ЕРК, все ключевые данные присутствуют
        :precondition:      Станция администратора сканирования, внешние серверы SmartCapture и контент-сервер запущены
        :precondition:      Справочник «Типы документов удостоверяющих личность для выбора при сканировании» (docTypesForScan) заполнен
        :precondition:      Параметр пользователя using_scanner (Доступность сканирования) = "да".
        :precondition:      В файле itwCredo-scanner.properties присутствует параметр с путём к файлу "fake_response scanner.fakeresponsefile=d:/fake_response.xml"
        :precondition:      в itwCredo-scanner.properties прописаны scanner.proxy.host, scanner.proxy.port
        :precondition:      В файле fake_response.xml установлена дата рождения: "25.555.1999"
        :precondition:      В файле fake_response.xml установлена дата выдачи:   "25.555.1999"
        :precondition:      В файле fake_response.xml установлен срок действия:  "25.555.1999"
        :comment:           Тестовые случаи моделировали через использование файла fake_response.xml
        :comment:           Пример файла прикреплён к задаче
        :source_point:      RM_57458
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 09.12.2021
        :client_env:        Google Chrome 97 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 97 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 97 [Windows 10; openSuSE Linux Leap 15.1]
        :precondition_time: 10
        :time_of_test:      10
        :count_of_check:    4
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'changing_customer'
    VARIANT = 'CustomerCard'

    # :newpage: #######################################################################################################

    # :step: На форме "Поиск карточки клиента в учетной системе Банка" нажимаем кнопку-список «Сканировать документ»

    # :step: Из списка ДУЛ кнопки «Сканировать документ» выбираем сканируемый документ
    value = 'Паспорт гражданина РБ'

    # :newpage: #######################################################################################################

    # :step: В диалоговом окне с предложением отсканировать следующую страницу документа нажимаем кнопку "Да"

    # :newpage: #######################################################################################################

    # :step: На форме "Поиск клиента" с результатами поиска нажимаем на найденную краткую карточку клиента

    # :newpage: #######################################################################################################

    # :step: На форме "Данные клиента" нажимаем кнопку "Изменить"

    # :newpage: #######################################################################################################

    # :assert: Поле "Дата рождения" очищено
    # :assert: Поле "Дата выдачи" очищено
    # :assert: Поле "Срок действия документа" очищено
    # :assert: В request.log в параметре клиента scanner_data переданы данные из fake_response.xml


    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


@pytest.mark.skip(reason="Template")
def test_57458_8(app, db_credo):
    """
    {#
        :id:                57458_8
        :priority:          Средний
        :module:            ЕФР
        :description:       Ошибка при создании заявки
        :precondition:      Пользователь авторизирован в СКЗ. Параметр пользователя using_scanner (Доступность сканирования) = "да"
        :precondition:      Тестовый клиент существует в ЕРК, все ключевые данные присутствуют
        :precondition:      Станция администратора сканирования, внешние серверы SmartCapture и контент-сервер запущены
        :precondition:      Справочник «Типы документов удостоверяющих личность для выбора при сканировании» (docTypesForScan) заполнен
        :precondition:      Параметр пользователя using_scanner (Доступность сканирования) = "да".
        :precondition:      В файле itwCredo-scanner.properties присутствует параметр с путём к файлу "fake_response scanner.fakeresponsefile=d:/fake_response.xml"
        :precondition:      в itwCredo-scanner.properties прописаны scanner.proxy.host, scanner.proxy.port
        :precondition:      В файле fake_response.xml установлена дата рождения: "25.05.19999"
        :precondition:      В файле fake_response.xml установлена дата выдачи:   "25.05.19999"
        :precondition:      В файле fake_response.xml установлен срок действия:  "25.05.19999"
        :comment:           Тестовые случаи моделировали через использование файла fake_response.xml
        :comment:           Пример файла прикреплён к задаче
        :source_point:      RM_57458
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 09.12.2021
        :client_env:        Google Chrome 97 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 97 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 97 [Windows 10; openSuSE Linux Leap 15.1]
        :precondition_time: 10
        :time_of_test:      10
        :count_of_check:    4
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'changing_customer'
    VARIANT = 'CustomerCard'

    # :newpage: #######################################################################################################

    # :step: На форме "Поиск карточки клиента в учетной системе Банка" нажимаем кнопку-список «Сканировать документ»

    # :step: Из списка ДУЛ кнопки «Сканировать документ» выбираем сканируемый документ
    value = 'Паспорт гражданина РБ'

    # :newpage: #######################################################################################################

    # :step: В диалоговом окне с предложением отсканировать следующую страницу документа нажимаем кнопку "Да"

    # :newpage: #######################################################################################################

    # :step: На форме "Поиск клиента" с результатами поиска нажимаем на найденную краткую карточку клиента

    # :newpage: #######################################################################################################

    # :step: На форме "Данные клиента" нажимаем кнопку "Изменить"

    # :newpage: #######################################################################################################

    # :assert: Поле "Дата рождения" очищено
    # :assert: Поле "Дата выдачи" очищено
    # :assert: Поле "Срок действия документа" очищено
    # :assert: В request.log в параметре клиента scanner_data переданы данные из fake_response.xml


    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


@pytest.mark.skip(reason="Template")
def test_57458_9(app, db_credo):
    """
    {#
        :id:                57458_9
        :priority:          Средний
        :module:            ЕФР
        :description:       Ошибка при создании заявки
        :precondition:      Пользователь авторизирован в СКЗ. Параметр пользователя using_scanner (Доступность сканирования) = "да"
        :precondition:      Тестовый клиент существует в ЕРК, все ключевые данные присутствуют
        :precondition:      Станция администратора сканирования, внешние серверы SmartCapture и контент-сервер запущены
        :precondition:      Справочник «Типы документов удостоверяющих личность для выбора при сканировании» (docTypesForScan) заполнен
        :precondition:      Параметр пользователя using_scanner (Доступность сканирования) = "да".
        :precondition:      В файле itwCredo-scanner.properties присутствует параметр с путём к файлу "fake_response scanner.fakeresponsefile=d:/fake_response.xml"
        :precondition:      в itwCredo-scanner.properties прописаны scanner.proxy.host, scanner.proxy.port
        :precondition:      В файле fake_response.xml установлена дата рождения: "25.05.199"
        :precondition:      В файле fake_response.xml установлена дата выдачи:   "25.05.199"
        :precondition:      В файле fake_response.xml установлен срок действия:  "25.05.199"
        :comment:           Тестовые случаи моделировали через использование файла fake_response.xml
        :comment:           Пример файла прикреплён к задаче
        :source_point:      RM_57458
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 09.12.2021
        :client_env:        Google Chrome 97 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 97 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 97 [Windows 10; openSuSE Linux Leap 15.1]
        :precondition_time: 10
        :time_of_test:      10
        :count_of_check:    4
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'changing_customer'
    VARIANT = 'CustomerCard'

    # :newpage: #######################################################################################################

    # :step: На форме "Поиск карточки клиента в учетной системе Банка" нажимаем кнопку-список «Сканировать документ»

    # :step: Из списка ДУЛ кнопки «Сканировать документ» выбираем сканируемый документ
    value = 'Паспорт гражданина РБ'

    # :newpage: #######################################################################################################

    # :step: В диалоговом окне с предложением отсканировать следующую страницу документа нажимаем кнопку "Да"

    # :newpage: #######################################################################################################

    # :step: На форме "Поиск клиента" с результатами поиска нажимаем на найденную краткую карточку клиента

    # :newpage: #######################################################################################################

    # :step: На форме "Данные клиента" нажимаем кнопку "Изменить"

    # :newpage: #######################################################################################################

    # :assert: Поле "Дата рождения" очищено
    # :assert: Поле "Дата выдачи" очищено
    # :assert: Поле "Срок действия документа" очищено
    # :assert: В request.log в параметре клиента scanner_data переданы данные из fake_response.xml


    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


@pytest.mark.skip(reason="Template")
def test_57458_10(app, db_credo):
    """
    {#
        :id:                57458_10
        :priority:          Средний
        :module:            ЕФР
        :description:       Ошибка при создании заявки
        :precondition:      Пользователь авторизирован в СКЗ. Параметр пользователя using_scanner (Доступность сканирования) = "да"
        :precondition:      Тестовый клиент существует в ЕРК, все ключевые данные присутствуют
        :precondition:      Станция администратора сканирования, внешние серверы SmartCapture и контент-сервер запущены
        :precondition:      Справочник «Типы документов удостоверяющих личность для выбора при сканировании» (docTypesForScan) заполнен
        :precondition:      Параметр пользователя using_scanner (Доступность сканирования) = "да".
        :precondition:      В файле itwCredo-scanner.properties присутствует параметр с путём к файлу "fake_response scanner.fakeresponsefile=d:/fake_response.xml"
        :precondition:      в itwCredo-scanner.properties прописаны scanner.proxy.host, scanner.proxy.port
        :precondition:      В файле fake_response.xml установлена дата рождения: "8.05.1999"
        :precondition:      В файле fake_response.xml установлена дата выдачи:   "8.05.1999"
        :precondition:      В файле fake_response.xml установлен срок действия:  "8.05.1999"
        :comment:           Тестовые случаи моделировали через использование файла fake_response.xml
        :comment:           Пример файла прикреплён к задаче
        :source_point:      RM_57458
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 09.12.2021
        :client_env:        Google Chrome 97 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 97 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 97 [Windows 10; openSuSE Linux Leap 15.1]
        :precondition_time: 10
        :time_of_test:      10
        :count_of_check:    4
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'changing_customer'
    VARIANT = 'CustomerCard'

    # :newpage: #######################################################################################################

    # :step: На форме "Поиск карточки клиента в учетной системе Банка" нажимаем кнопку-список «Сканировать документ»

    # :step: Из списка ДУЛ кнопки «Сканировать документ» выбираем сканируемый документ
    value = 'Паспорт гражданина РБ'

    # :newpage: #######################################################################################################

    # :step: В диалоговом окне с предложением отсканировать следующую страницу документа нажимаем кнопку "Да"

    # :newpage: #######################################################################################################

    # :step: На форме "Поиск клиента" с результатами поиска нажимаем на найденную краткую карточку клиента

    # :newpage: #######################################################################################################

    # :step: На форме "Данные клиента" нажимаем кнопку "Изменить"

    # :newpage: #######################################################################################################

    # :assert: Поле "Дата рождения" заполнилось значением "08.05.1999"
    # :assert: Поле "Дата выдачи" заполнилось значением "08.05.1999"
    # :assert: Поле "Срок действия документа" заполнилось значением "08.05.1999"
    # :assert: В request.log в параметре клиента scanner_data переданы данные из fake_response.xml


    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


@pytest.mark.skip(reason="Template")
def test_57458_11(app, db_credo):
    """
    {#
        :id:                57458_11
        :priority:          Средний
        :module:            ЕФР
        :description:       Ошибка при создании заявки
        :precondition:      Пользователь авторизирован в СКЗ. Параметр пользователя using_scanner (Доступность сканирования) = "да"
        :precondition:      Тестовый клиент существует в ЕРК, все ключевые данные присутствуют
        :precondition:      Станция администратора сканирования, внешние серверы SmartCapture и контент-сервер запущены
        :precondition:      Справочник «Типы документов удостоверяющих личность для выбора при сканировании» (docTypesForScan) заполнен
        :precondition:      Параметр пользователя using_scanner (Доступность сканирования) = "да".
        :precondition:      В файле itwCredo-scanner.properties присутствует параметр с путём к файлу "fake_response scanner.fakeresponsefile=d:/fake_response.xml"
        :precondition:      в itwCredo-scanner.properties прописаны scanner.proxy.host, scanner.proxy.port
        :precondition:      В файле fake_response.xml установлена дата рождения: "08.5.1999"
        :precondition:      В файле fake_response.xml установлена дата выдачи:   "08.5.1999"
        :precondition:      В файле fake_response.xml установлен срок действия:  "08.5.1999"
        :comment:           Тестовые случаи моделировали через использование файла fake_response.xml
        :comment:           Пример файла прикреплён к задаче
        :source_point:      RM_57458
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 09.12.2021
        :client_env:        Google Chrome 97 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 97 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 97 [Windows 10; openSuSE Linux Leap 15.1]
        :precondition_time: 10
        :time_of_test:      10
        :count_of_check:    4
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'changing_customer'
    VARIANT = 'CustomerCard'

    # :newpage: #######################################################################################################

    # :step: На форме "Поиск карточки клиента в учетной системе Банка" нажимаем кнопку-список «Сканировать документ»

    # :step: Из списка ДУЛ кнопки «Сканировать документ» выбираем сканируемый документ
    value = 'Паспорт гражданина РБ'

    # :newpage: #######################################################################################################

    # :step: В диалоговом окне с предложением отсканировать следующую страницу документа нажимаем кнопку "Да"

    # :newpage: #######################################################################################################

    # :step: На форме "Поиск клиента" с результатами поиска нажимаем на найденную краткую карточку клиента

    # :newpage: #######################################################################################################

    # :step: На форме "Данные клиента" нажимаем кнопку "Изменить"

    # :newpage: #######################################################################################################

    # :assert: Поле "Дата рождения" заполнилось значением "08.05.1999"
    # :assert: Поле "Дата выдачи" заполнилось значением "08.05.1999"
    # :assert: Поле "Срок действия документа" заполнилось значением "08.05.1999"
    # :assert: В request.log в параметре клиента scanner_data переданы данные из fake_response.xml


    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)
