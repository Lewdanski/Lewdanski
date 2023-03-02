# :suit_description: #52512 
# :revision_date: 21.12.2022

@pytest.mark.skip(reason="Template")
def test_52512_1(app, credo_db):
    """
    {#
        :id:                52512_1
        :priority:          Средний
        :module:            Ядро/фронт
        :description:       Проверка контроля обязательного значения LastName в ДБО, отправка сообщения пользователям с ролью admins
        :precondition:      Клиент авторизирован в ДБО
        :precondition:      У клиента в ерк не заполнен тег LastName
        :precondition:      в itwCredoFront-process.properties параметр IsCheckClientData="true"
        :precondition:      В справочнике "info_guide_for_ibank" для строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" заполнено поле "Информация"
        :source_point:      52512
        :comment:           
        :tc_type:           +
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 17.04.2020
        :client_env:        Google Chrome 84 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 78 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 44 [Windows 10]
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'ClientNewCardInner6'

    VARIANT = 'ClientAdditionalCardInner'


    # :newpage: #######################################################################################################

    # :step: На форме вкладки "Заявки" нажимаем кнопку "Новая заявка"

    # :newpage: ######################################################################################################

    # :step: Создаем заявку по ссылке "Заявка на выпуск дополнительной карточки"

    # :newpage: #######################################################################################################

    # :assert: На форме отобразилось сообщение из поля "Информация" строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" справочника info_guide_for_ibank
    # :assert: Пользователям с ролью admins пришло сообщение с темой: «ДБО. Отсутствует обязательное значение:Фамилия (surname)»
    # :assert: emailBody: ФИО клиента: ОБЯЗАТЕЛЬНЫЕ ЗНАЧЕНИЯ ДБО Код ЕРК ISPPM37426 Время оформления заявки: 01-04-2020 Оформляемая заявка: Выпуск дополнительной карточки в ДБО v2

    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)

@pytest.mark.skip(reason="Template")
def test_52512_2(app, credo_db):
    """
    {#
        :id:                52512_2
        :priority:          
        :module:            Ядро/фронт
        :description:       Проверка контроля обязательного значения FirstName в ДБО, отправка сообщения пользователям с ролью admins
        :precondition:      Клиент авторизирован в ДБО
        :precondition:      У клиента в ерк не заполнен тег FirstName
        :precondition:      в itwCredoFront-process.properties параметр IsCheckClientData="true"
        :precondition:      В справочнике "info_guide_for_ibank" для строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" заполнено поле "Информация"
        :source_point:      52512
        :comment:           
        :tc_type:           
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 17.04.2020
        :client_env:        Google Chrome 84 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 78 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 44 [Windows 10]
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'ClientNewCardInner6'

    VARIANT = 'ClientAdditionalCardInner'


    # :newpage: #######################################################################################################

    # :step: На форме вкладки "Заявки" нажимаем кнопку "Новая заявка"

    # :newpage: ######################################################################################################

    # :step: Создаем заявку по ссылке "Заявка на выпуск дополнительной карточки"

    # :newpage: #######################################################################################################

    # :assert: На форме отобразилось сообщение из поля "Информация" строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" справочника info_guide_for_ibank
    # :assert: Пользователям с ролью admins пришло сообщение с темой: «ДБО. Отсутствует обязательное значение:Имя (firstname)»
    # :assert: emailBody: ФИО клиента: ОБЯЗАТЕЛЬНЫЕ ЗНАЧЕНИЯ ДБО Код ЕРК ISPPM37426 Время оформления заявки: 01-04-2020 Оформляемая заявка: Выпуск дополнительной карточки в ДБО v2

    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)

@pytest.mark.skip(reason="Template")
def test_52512_13(app, credo_db):
    """
    {#
        :id:                52512_13
        :priority:          Средний
        :module:            Ядро/фронт
        :description:       Проверка контроля обязательного значения ДУЛ DocDateExpiry в ДБО, если sprcode=PASSPORT. Отправка сообщения пользователям с ролью admins
        :precondition:      Клиент авторизирован в ДБО
        :precondition:      У клиента в ерк есть ДУЛ со статусом 1 и незаполненным DocDateExpiry
        :precondition:      в itwCredoFront-process.properties параметр IsCheckClientData="true"
        :precondition:      В справочнике "info_guide_for_ibank" для строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" заполнено поле "Информация"
        :source_point:      52512
        :comment:           
        :tc_type:           +
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 17.04.2020
        :client_env:        Google Chrome 84 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 78 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 44 [Windows 10]
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'ClientNewCardInner6'

    VARIANT = 'ClientAdditionalCardInner'


    # :newpage: #######################################################################################################

    # :step: На форме вкладки "Заявки" нажимаем кнопку "Новая заявка"

    # :newpage: ######################################################################################################

    # :step: Создаем заявку по ссылке "Заявка на выпуск дополнительной карточки"

    # :newpage: #######################################################################################################

    # :assert: На форме отобразилось сообщение из поля "Информация" строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" справочника info_guide_for_ibank
    # :assert: Пользователям с ролью admins пришло сообщение с темой: «ДБО. Отсутствует обязательное значение:Дата окончания действия документа (DocDateExpiry)»
    # :assert: emailBody: ФИО клиента: ОБЯЗАТЕЛЬНЫЕ ЗНАЧЕНИЯ ДБО Код ЕРК ISPPM37426 Время оформления заявки: 01-04-2020 Оформляемая заявка: Выпуск дополнительной карточки в ДБО v2

    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)

@pytest.mark.skip(reason="Template")
def test_52512_18(app, credo_db):
    """
    {#
        :id:                52512_18
        :priority:          Средний
        :module:            Ядро/фронт
        :description:       Проверка контроля обязательного значения PersonalNumberBy в ДБО, отправка сообщения пользователям с ролью admins
        :precondition:      Клиент авторизирован в ДБО
        :precondition:      У клиента в ерк не заполнен тег PersonalNumberBy
        :precondition:      в itwCredoFront-process.properties параметр IsCheckClientData="true"
        :precondition:      В справочнике "info_guide_for_ibank" для строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" заполнено поле "Информация"
        :source_point:      52512
        :comment:           
        :tc_type:           +
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 17.04.2020
        :client_env:        Google Chrome 85 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 80 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 85 [Windows 10]
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'ClientNewCardInner'

    VARIANT = 'new_card_v2'


    # :newpage: #######################################################################################################

    # :step: На форме вкладки "Заявки" нажимаем кнопку "Новая заявка"

    # :newpage: ######################################################################################################

    # :step: Создаем заявку по ссылке "Заявка на выпуск платежной карточки"

    # :newpage: #######################################################################################################

    # :assert: На форме отобразилось сообщение из поля "Информация" строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" справочника info_guide_for_ibank
    # :assert: Пользователям с ролью admins пришло сообщение с темой: «ДБО. Отсутствует обязательное значение:Личный номер (idn)»
    # :assert: emailBody: ФИО клиента: ОБЯЗАТЕЛЬНЫЕ ЗНАЧЕНИЯ ДБО Код ЕРК ISPPM37426 Время оформления заявки: 01-04-2020 Оформляемая заявка: Заявка на выпуск платежной карточки v.6

    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)

@pytest.mark.skip(reason="Template")
def test_52512_21(app, credo_db):
    """
    {#
        :id:                52512_21
        :priority:          Средний
        :module:            Ядро/фронт
        :description:       Проверка контроля обязательного значения BirthDate в ДБО, отправка сообщения пользователям с ролью admins
        :precondition:      Клиент авторизирован в ДБО
        :precondition:      У клиента в ерк не заполнен тег BirthDate
        :precondition:      в itwCredoFront-process.properties параметр IsCheckClientData="true"
        :precondition:      В справочнике "info_guide_for_ibank" для строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" заполнено поле "Информация"
        :source_point:      52512
        :comment:           
        :tc_type:           +
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 17.04.2020
        :client_env:        Google Chrome 85 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 80 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 85 [Windows 10]
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'ClientNewCardInner'

    VARIANT = 'new_card_v2'


    # :newpage: #######################################################################################################

    # :step: На форме вкладки "Заявки" нажимаем кнопку "Новая заявка"

    # :newpage: ######################################################################################################

    # :step: Создаем заявку по ссылке "Заявка на выпуск платежной карточки"

    # :newpage: #######################################################################################################

    # :assert: На форме отобразилось сообщение из поля "Информация" строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" справочника info_guide_for_ibank
    # :assert: Пользователям с ролью admins пришло сообщение с темой: «ДБО. Отсутствует обязательное значение:Дата рождения (birth_date)»
    # :assert: emailBody: ФИО клиента: ОБЯЗАТЕЛЬНЫЕ ЗНАЧЕНИЯ ДБО Код ЕРК ISPPM37426 Время оформления заявки: 01-04-2020 Оформляемая заявка: Заявка на выпуск платежной карточки v.6

    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)

@pytest.mark.skip(reason="Template")
def test_52512_40(app, credo_db):
    """
    {#
        :id:                52512_40
        :priority:          Средний
        :module:            Ядро/фронт
        :description:       Проверка контроля обязательного значения ResidentCode в ДБО, отправка сообщения пользователям с ролью admins
        :precondition:      Клиент авторизирован в ДБО
        :precondition:      У клиента в ерк не заполнен тег ResidentCode
        :precondition:      в itwCredoFront-process.properties параметр IsCheckClientData="true"В справочнике "info_guide_for_ibank" для строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" заполнено поле "Информация"
        :source_point:      52512
        :comment:           
        :tc_type:           +
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 17.04.2020
        :client_env:        Google Chrome 85 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 80 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 85 [Windows 10]
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'ClientNewCardInner'

    VARIANT = 'reissue_maincard'


    # :newpage: #######################################################################################################

    # :step: На форме вкладки "Заявки" нажимаем кнопку "Новая заявка"

    # :newpage: ######################################################################################################

    # :step: Создаем заявку по ссылке "Заявка на перевыпуск платежной карточки"

    # :newpage: #######################################################################################################

    # :assert: На форме отобразилось сообщение из поля "Информация" строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" справочника info_guide_for_ibank
    # :assert: Пользователям с ролью admins пришло сообщение с темой: «ДБО. Отсутствует обязательное значение:Страна резидентства (res_cntr)»
    # :assert: emailBody: ФИО клиента: ОБЯЗАТЕЛЬНЫЕ ЗНАЧЕНИЯ ДБО Код ЕРК ISPPM37426 Время оформления заявки: 01-04-2020 Оформляемая заявка: Заявка на перевыпуск платежной карточки v.1

    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)

@pytest.mark.skip(reason="Template")
def test_52512_44(app, credo_db):
    """
    {#
        :id:                52512_44
        :priority:          Средний
        :module:            Ядро/фронт
        :description:       Проверка контроля обязательного значения ДУЛ CountryCode в ДБО, отправка сообщения пользователям с ролью admins
        :precondition:      Клиент авторизирован в ДБО
        :precondition:      У клиента в ерк есть ДУЛ со статусом 1 и незаполненным CountryCode
        :precondition:      в itwCredoFront-process.properties параметр IsCheckClientData="true"
        :precondition:      В справочнике "info_guide_for_ibank" для строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" заполнено поле "Информация"
        :source_point:      52512
        :comment:           
        :tc_type:           +
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 17.04.2020
        :client_env:        Google Chrome 85 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 80 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 85 [Windows 10]
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'ClientNewCardInner'

    VARIANT = 'reissue_maincard'


    # :newpage: #######################################################################################################

    # :step: На форме вкладки "Заявки" нажимаем кнопку "Новая заявка"

    # :newpage: ######################################################################################################

    # :step: Создаем заявку по ссылке "Заявка на перевыпуск платежной карточки"

    # :newpage: #######################################################################################################

    # :assert: На форме отобразилось сообщение из поля "Информация" строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" справочника info_guide_for_ibank
    # :assert: Пользователям с ролью admins пришло сообщение с темой: «ДБО. Отсутствует обязательное значение:Страна выдачи документа (doc_cntr)»
    # :assert: emailBody: ФИО клиента: ОБЯЗАТЕЛЬНЫЕ ЗНАЧЕНИЯ ДБО Код ЕРК ISPPM37426 Время оформления заявки: 01-04-2020 Оформляемая заявка: Заявка на перевыпуск платежной карточки v.1

    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)

@pytest.mark.skip(reason="Template")
def test_52512_58(app, credo_db):
    """
    {#
        :id:                52512_58
        :priority:          Средний
        :module:            Ядро/фронт
        :description:       Проверка контроля обязательного значения в ДБО если отсутствует несколько, отправка сообщения пользователям с ролью admins
        :precondition:      Клиент авторизирован в ДБО
        :precondition:      У клиента в ерк не заполнен тег PersonalNumberBy
        :precondition:      У клиента в ерк не заполнен тег LastName
        :precondition:      У клиента в ерк не заполнен тег FirstName
        :precondition:      У клиента в ерк не заполнен тег CitizenshipCode
        :precondition:      У клиента в ерк не заполнен тег ResidentCode
        :precondition:      У клиента в ерк не заполнен тег BirthDate
        :precondition:      в itwCredoFront-process.properties параметр IsCheckClientData="true"
        :precondition:      В справочнике "info_guide_for_ibank" для строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" заполнено поле "Информация"
        :source_point:      52512
        :comment:           
        :tc_type:           +
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 17.04.2020
        :client_env:        Google Chrome 85 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 80 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 85 [Windows 10]
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'CreditCardSales'

    VARIANT = 'salary_ib'


    # :newpage: #######################################################################################################

    # :step: Создаем заявку по ссылке "Онлайн-овердрафт для держателей зарплатных карт"

    # :newpage: #######################################################################################################

    # :assert: На форме отобразилось сообщение из поля "Информация" строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" справочника info_guide_for_ibank
    # :assert: Пользователям с ролью admins пришло сообщение с темой: «ДБО. Отсутствует обязательное значение:Личный номер (idn);Фамилия (lastname);Имя (firstname);Дата рождения (birth_date);Гражданство (nat_cntr);Страна резидентства (res_cntr)»
    # :assert: emailBody: ФИО клиента: ОБЯЗАТЕЛЬНЫЕ ЗНАЧЕНИЯ ДБО Код ЕРК ISPPM37426 Время оформления заявки: 01-04-2020 Оформляемая заявка: Онлайн-овердрафт для держателей зарплатных карт v.2

    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)

@pytest.mark.skip(reason="Template")
def test_52512_68(app, credo_db):
    """
    {#
        :id:                52512_68
        :priority:          Высокий
        :module:            Ядро/фронт
        :description:       Проверка контроля обязательного значения ДУЛ DocDateExpiry в ДБО если sprcode=VID_BY, отправка сообщения пользователям с ролью admins
        :precondition:      Клиент авторизирован в ДБО
        :precondition:      У клиента в ерк есть ДУЛ со статусом 1 и незаполненным DocDateExpiry
        :precondition:      ДУЛ у клиента вид на жительство
        :precondition:      в itwCredoFront-process.properties параметр IsCheckClientData="true"
        :precondition:      В справочнике "info_guide_for_ibank" для строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" заполнено поле "Информация"
        :source_point:      52512
        :comment:           
        :tc_type:           +
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 17.04.2020
        :client_env:        Google Chrome 85 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 80 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 85 [Windows 10]
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'CreditCardSales'

    VARIANT = 'salary_ib'


    # :newpage: #######################################################################################################

    # :step: Создаем заявку по ссылке "Онлайн-овердрафт для держателей зарплатных карт"

    # :newpage: #######################################################################################################

    # :assert: На форме отобразилось сообщение из поля "Информация" строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" справочника info_guide_for_ibank
    # :assert: Пользователям с ролью admins пришло сообщение с темой: «ДБО. Отсутствует обязательное значение:Дата окончания действия документа (DocDateExpiry)»
    # :assert: emailBody: ФИО клиента: ОБЯЗАТЕЛЬНЫЕ ЗНАЧЕНИЯ ДБО Код ЕРК ISPPM37426 Время оформления заявки: 01-04-2020 Оформляемая заявка: ON-кредит v.2

    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)

@pytest.mark.skip(reason="Template")
def test_52512_76(app, credo_db):
    """
    {#
        :id:                52512_76
        :priority:          Средний
        :module:            Ядро/фронт
        :description:       Проверка контроля обязательного значения в ДБО если отсутствует несколько, отправка сообщения пользователям с ролью admins
        :precondition:      Клиент авторизирован в ДБО
        :precondition:      У клиента в ерк не заполнен тег PersonalNumberBy
        :precondition:      У клиента в ерк не заполнен тег LastName
        :precondition:      У клиента в ерк не заполнен тег FirstName
        :precondition:      У клиента в ерк не заполнен тег BirthDate
        :precondition:      У клиента в ерк не заполнен тег CitizenshipCode
        :precondition:      У клиента в ерк не заполнен тег ResidentCode
        :precondition:      в itwCredoFront-process.properties параметр IsCheckClientData="true"
        :precondition:      В справочнике "info_guide_for_ibank" для строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" заполнено поле "Информация"
        :source_point:      52512
        :comment:           
        :tc_type:           +
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 17.04.2020
        :client_env:        Google Chrome 85 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 80 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 85 [Windows 10]
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'Information'

    VARIANT = 'CreditContractDebtReference'


    # :newpage: #######################################################################################################

    # :step: На форме вкладки "Заявки" нажимаем кнопку "Новая заявка"

    # :newpage: ######################################################################################################

    # :step: Создаем заявку по ссылке "Справка о задолженности по кредитному договору"

    # :newpage: #######################################################################################################

    # :assert: На форме отобразилось сообщение из поля "Информация" строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" справочника info_guide_for_ibank
    # :assert: Пользователям с ролью admins пришло сообщение с темой: «ДБО. Отсутствует обязательное значение:Личный номер (idn);Фамилия (lastname);Имя (firstname);Дата рождения (birth_date);Гражданство (nat_cntr);Страна резидентства (res_cntr)»
    # :assert: emailBody: ФИО клиента: ОБЯЗАТЕЛЬНЫЕ ЗНАЧЕНИЯ ДБО Код ЕРК ISPPM37426 Время оформления заявки: 01-04-2020 Оформляемая заявка: Справка о задолженности по кредитному договору

    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)

@pytest.mark.skip(reason="Template")
def test_52512_98(app, credo_db):
    """
    {#
        :id:                52512_98
        :priority:          Средний
        :module:            Ядро/фронт
        :description:       Проверка контроля обязательного значения ДУЛ DocDateIssue в ДБО, отправка сообщения пользователям с ролью admins
        :precondition:      Клиент авторизирован в ДБО
        :precondition:      У клиента в ерк есть ДУЛ со статусом 1 и незаполненный DocDateIssue
        :precondition:      в itwCredoFront-process.properties параметр IsCheckClientData="true"
        :precondition:      В справочнике "info_guide_for_ibank" для строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" заполнено поле "Информация"
        :source_point:      52512
        :comment:           
        :tc_type:           +
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 17.04.2020
        :client_env:        Google Chrome 85 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 80 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 85 [Windows 10]
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'CreditCardSales'

    VARIANT = 'OnCredit'


    # :newpage: #######################################################################################################

    # :step: На форме вкладки "Заявки" нажимаем кнопку "Новая заявка"

    # :newpage: ######################################################################################################

    # :step: Создаем заявку по ссылке "ON-кредит за 5 минут"

    # :newpage: #######################################################################################################

    # :assert: На форме отобразилось сообщение из поля "Информация" строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" справочника info_guide_for_ibank
    # :assert: Пользователям с ролью admins пришло сообщение с темой: «ДБО. Отсутствует обязательное значение:Дата выдачи документа (doc_dt)»
    # :assert: emailBody: ФИО клиента: ОБЯЗАТЕЛЬНЫЕ ЗНАЧЕНИЯ ДБО Код ЕРК ISPPM37426 Время оформления заявки: 01-04-2020 Оформляемая заявка: ON-кредит v.2

    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)

@pytest.mark.skip(reason="Template")
def test_52512_138(app, credo_db):
    """
    {#
        :id:                52512_138
        :priority:          Средний
        :module:            Ядро/фронт
        :description:       Проверка контроля валидности ДУЛ в ДБО, если дата выдачи ДУЛ больше текущей, отправка сообщения пользователям с ролью admins
        :precondition:      Клиент авторизирован в ДБО
        :precondition:      У клиента в ерк есть ДУЛ со статусом 1, Текущая дата < Дата выдачи ДУЛ
        :precondition:      в itwCredoFront-process.properties параметр IsCheckClientData="true"
        :precondition:      В справочнике "info_guide_for_ibank" для строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" заполнено поле "Информация"
        :source_point:      52512, 55271
        :comment:           
        :tc_type:           +
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 01.10.2019
        :client_env:        Google Chrome 73.0.3683.86 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 65.0.2 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE [Windows 10]
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = ''

    VARIANT = ''


    # :newpage: #######################################################################################################

    # :step: На форме вкладки "Заявки" нажимаем кнопку "Новая заявка"

    # :newpage: ######################################################################################################

    # :step: Создаем заявку по ссылке "Заявка на Online-страхование"

    # :newpage: #######################################################################################################

    # :assert: На форме отобразилось сообщение из поля "Информация" строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" справочника info_guide_for_ibank
    # :assert: Пользователям с ролью admins пришло сообщение с темой: «ДБО. Документ клиента невалиден: Дата выдачи документа (doc_dt).»
    # :assert: emailBody: ФИО клиента: ОБЯЗАТЕЛЬНЫЕ ЗНАЧЕНИЯ ДБО Код ЕРК ISPPM37426 Время оформления заявки: 01-04-2020 Оформляемая заявка: Онлайн-страхование

    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)

@pytest.mark.skip(reason="Template")
def test_52512_139(app, credo_db):
    """
    {#
        :id:                52512_139
        :priority:          Средний
        :module:            Ядро/фронт
        :description:       Проверка контроля валидности ДУЛ в ДБО, если дата окончания действия меньше текущей для sprcode=PASSPORT, отправка сообщения пользователям с ролью admins
        :precondition:      Клиент авторизирован в ДБО
        :precondition:      У клиента в ерк есть ДУЛ со статусом 1, Текущая дата > Дата окончания действия ДУЛ
        :precondition:      в itwCredoFront-process.properties параметр IsCheckClientData="true"
        :precondition:      В справочнике "info_guide_for_ibank" для строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" заполнено поле "Информация"
        :source_point:      52512, 55271
        :comment:           
        :tc_type:           +
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 01.10.2019
        :client_env:        Google Chrome 73.0.3683.86 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 65.0.2 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE [Windows 10]
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = ''

    VARIANT = ''


    # :newpage: #######################################################################################################

    # :step: На форме вкладки "Заявки" нажимаем кнопку "Новая заявка"

    # :newpage: ######################################################################################################

    # :step: Создаем заявку по ссылке "Заявка на Online-страхование"

    # :newpage: #######################################################################################################

    # :assert: На форме отобразилось сообщение из поля "Информация" строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" справочника info_guide_for_ibank
    # :assert: Пользователям с ролью admins пришло сообщение с темой: «ДБО. Документ клиента невалиден: Дата выдачи документа (doc_dt).»
    # :assert: emailBody: ФИО клиента: ОБЯЗАТЕЛЬНЫЕ ЗНАЧЕНИЯ ДБО Код ЕРК ISPPM37426 Время оформления заявки: 01-04-2020 Оформляемая заявка: Онлайн-страхование

    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)

@pytest.mark.skip(reason="Template")
def test_52512_161(app, credo_db):
    """
    {#
        :id:                52512_161
        :priority:          Средний
        :module:            Ядро/фронт
        :description:       Проверка контроля обязательного значения CitizenshipCode в ДБО, отправка сообщения пользователям с ролью admins
        :precondition:      Клиент авторизирован в МП
        :precondition:      У клиента в ерк не заполнен тег CitizenshipCode
        :precondition:      в itwCredoFront-process.properties параметр IsCheckClientData="true"
        :precondition:      В справочнике "info_guide_for_ibank" для строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" заполнено поле "Информация"
        :source_point:      52512
        :comment:           
        :tc_type:           +
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 17.04.2020
        :client_env:        Android 9.0, iOS 13.3
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'ClientNewCardInner'

    VARIANT = 'new_card_v2'


    # :newpage: #######################################################################################################

    # :step: На форме вкладки "Заявки" нажимаем кнопку "Новая заявка"

    # :newpage: ######################################################################################################

    # :step: Создаем заявку по ссылке "Заявка на выпуск платежной карточки"

    # :newpage: #######################################################################################################

    # :assert: На форме отобразилось сообщение из поля "Информация" строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" справочника info_guide_for_ibank
    # :assert: Пользователям с ролью admins пришло сообщение с темой: «ДБО. Отсутствует обязательное значение:Гражданство (nat_cntr)»
    # :assert: emailBody: ФИО клиента: ОБЯЗАТЕЛЬНЫЕ ЗНАЧЕНИЯ ДБО Код ЕРК ISPPM37426 Время оформления заявки: 01-04-2020 Оформляемая заявка: Заявка на выпуск платежной карточки v.6

    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)

@pytest.mark.skip(reason="Template")
def test_52512_251(app, credo_db):
    """
    {#
        :id:                52512_251
        :priority:          Средний
        :module:            Ядро/фронт
        :description:       Проверка контроля обязательного значения ДУЛ CountryCode в ДБО, отправка сообщения пользователям с ролью admins
        :precondition:      Клиент авторизирован в МП
        :precondition:      У клиента в ерк есть ДУЛ со статусом 1 и незаполненным CountryCode
        :precondition:      в itwCredoFront-process.properties параметр IsCheckClientData="true"
        :precondition:      В справочнике "info_guide_for_ibank" для строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" заполнено поле "Информация"
        :source_point:      52512
        :comment:           
        :tc_type:           +
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 17.04.2020
        :client_env:        Google Chrome 87 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Android 10.0, iOS 14.3
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'CreditCardSales'

    VARIANT = 'cart_pokup_ib'


    # :newpage: #######################################################################################################

    # :step: На форме вкладки "Заявки" нажимаем кнопку "Новая заявка"

    # :newpage: ######################################################################################################

    # :step: Создаем заявку по ссылке "Оформление Карты Покупок"

    # :newpage: #######################################################################################################

    # :assert: На форме отобразилось сообщение из поля "Информация" строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" справочника info_guide_for_ibank
    # :assert: Пользователям с ролью admins пришло сообщение с темой: «ДБО. Отсутствует обязательное значение:Страна выдачи документа (doc_cntr)»
    # :assert: emailBody: ФИО клиента: ОБЯЗАТЕЛЬНЫЕ ЗНАЧЕНИЯ ДБО Код ЕРК ISPPM37426 Время оформления заявки: 01-04-2020 Оформляемая заявка: Оформление Карты Покупок v.1

    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)

@pytest.mark.skip(reason="Template")
def test_52512_282(app, credo_db):
    """
    {#
        :id:                52512_282
        :priority:          Средний
        :module:            Ядро/фронт
        :description:       Проверка отсутствия контроля обязательного значения ДУЛ DocDateExpiry в ДБО если sprcode=PAS_INOS
        :precondition:      Клиент авторизирован в ДБО
        :precondition:      У клиента в ерк есть ДУЛ со статусом 1 и незаполненным DocDateExpiry
        :precondition:      ДУЛ у клиента иностранный паспорт
        :precondition:      в itwCredoFront-process.properties параметр IsCheckClientData="true"
        :source_point:      52512
        :comment:           
        :tc_type:           +
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 17.04.2020
        :client_env:        Google Chrome 85 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 80 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 85 [Windows 10]
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'CreditCardSales'

    VARIANT = 'salary_ib'


    # :newpage: #######################################################################################################

    # :step: Создаем заявку по ссылке "Онлайн-овердрафт для держателей зарплатных карт"

    # :newpage: #######################################################################################################

    # :assert: Исключина проверка для sprCode="PAS_INOS", при которой если дата окончания ДУЛ не заполнена, то документ считается истекшим
    # :assert: Оформление заявки продолжается

    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)

@pytest.mark.skip(reason="Template")
def test_52512_287(app, credo_db):
    """
    {#
        :id:                52512_287
        :priority:          Средний
        :module:            Ядро/фронт
        :description:       Проверка того, что обязательно должны быть значения sprcode для Address
        :precondition:      У клиента в ерк есть блок Adress без sprcode
        :precondition:      в itwCredoFront-process.properties параметр IsCheckClientData="true"
        :precondition:      В справочнике "info_guide_for_ibank" для строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" заполнено поле "Информация"
        :source_point:      52512
        :comment:           
        :tc_type:           +
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 17.04.2020
        :client_env:        Google Chrome 85 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 80 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 85 [Windows 10]
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'CreditCardSales'

    VARIANT = 'OnCredit'


    # :newpage: #######################################################################################################

    # :step: На форме вкладки "Заявки" нажимаем кнопку "Новая заявка"

    # :newpage: ######################################################################################################

    # :step: Создаем заявку по ссылке "ON-кредит за 5 минут"

    # :newpage: #######################################################################################################

    # :assert: На форме отобразилось сообщение из поля "Информация" строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" справочника info_guide_for_ibank
    # :assert: Пользователям с ролью admins пришло сообщение об отсутствии обязательного значения

    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)

@pytest.mark.skip(reason="Template")
def test_52512_288(app, credo_db):
    """
    {#
        :id:                52512_288
        :priority:          Высокий
        :module:            Ядро/фронт
        :description:       Проверка того, что обязательно должны быть значения sprcode для Locality
        :precondition:      У клиента в ерк есть блок Locality без sprcode
        :precondition:      в itwCredoFront-process.properties параметр IsCheckClientData="true"
        :precondition:      В справочнике "info_guide_for_ibank" для строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" заполнено поле "Информация"
        :source_point:      52512
        :comment:           
        :tc_type:           +
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 17.04.2020
        :client_env:        Google Chrome 85 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 80 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 85 [Windows 10]
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'CreditCardSales'

    VARIANT = 'OnCredit'


    # :newpage: #######################################################################################################

    # :step: На форме вкладки "Заявки" нажимаем кнопку "Новая заявка"

    # :newpage: ######################################################################################################

    # :step: Создаем заявку по ссылке "ON-кредит за 5 минут"

    # :newpage: #######################################################################################################

    # :assert: На форме отобразилось сообщение из поля "Информация" строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" справочника info_guide_for_ibank 
    # :assert: Пользователям с ролью admins пришло сообщение об отсутствии обязательного значения

    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)

@pytest.mark.skip(reason="Template")
def test_52512_289(app, credo_db):
    """
    {#
        :id:                52512_289
        :priority:          Средний
        :module:            Ядро/фронт
        :description:       Проверка того, что обязательно должны быть значения sprcode для Contact
        :precondition:      У клиента в ерк есть блок Contact без sprcode
        :precondition:      в itwCredoFront-process.properties параметр IsCheckClientData="true"
        :precondition:      В справочнике "info_guide_for_ibank" для строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" заполнено поле "Информация"
        :source_point:      52512
        :comment:           
        :tc_type:           +
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 17.04.2020
        :client_env:        Google Chrome 85 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 80 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 85 [Windows 10]
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'CreditCardSales'

    VARIANT = 'OnCredit'


    # :newpage: #######################################################################################################

    # :step: На главной форме нажимаем кн. "Новая заявка"

    # :newpage: ######################################################################################################

    # :step: Создаем заявку по ссылке "ON-кредит за 5 минут"

    # :newpage: #######################################################################################################

    # :assert: На форме отобразилось сообщение из поля "Информация" строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" справочника info_guide_for_ibank
    # :assert: Пользователям с ролью admins пришло сообщение об отсутствии обязательного значения

    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)

@pytest.mark.skip(reason="Template")
def test_52512_308(app, credo_db):
    """
    {#
        :id:                52512_308
        :priority:          Средний
        :module:            Ядро/фронт
        :description:       Проверка контроля обязательного значения PersonalNumberOther в ДБО, отправка сообщения пользователям с ролью admins
        :precondition:      Клиент авторизирован в ДБО
        :precondition:      Клиент нерезидент
        :precondition:      У клиента в ерк не заполнен тег PersonalNumberOther
        :precondition:      в itwCredoFront-process.properties параметр IsCheckClientData="true"
        :precondition:      В справочнике "info_guide_for_ibank" для строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" заполнено поле "Информация"
        :source_point:      52512
        :comment:           
        :tc_type:           +
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 17.04.2020
        :client_env:        Google Chrome 84 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 78 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 44 [Windows 10]
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'ClientNewCardInner6'

    VARIANT = 'ClientAdditionalCardInner'


    # :newpage: #######################################################################################################

    # :step: На форме вкладки "Заявки" нажимаем кнопку "Новая заявка"

    # :newpage: ######################################################################################################

    # :step: Создаем заявку по ссылке "Заявка на выпуск дополнительной карточки"

    # :newpage: #######################################################################################################

    # :assert: На форме отобразилось сообщение из поля "Информация" строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" справочника info_guide_for_ibank
    # :assert: Пользователям с ролью admins пришло сообщение с темой: «ДБО. Отсутствует обязательное значение:Личный номер (idn)»
    # :assert: emailBody: ФИО клиента: ОБЯЗАТЕЛЬНЫЕ ЗНАЧЕНИЯ ДБО Код ЕРК ISPPM37426 Время оформления заявки: 01-04-2020 Оформляемая заявка: Выпуск дополнительной карточки в ДБО v2

    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)

@pytest.mark.skip(reason="Template")
def test_52512_359(app, credo_db):
    """
    {#
        :id:                52512_359
        :priority:          Средний
        :module:            Ядро/фронт
        :description:       Проверка контроля обязательного значения PersonalNumberOther в ДБО, отправка сообщения пользователям с ролью admins
        :precondition:      Клиент авторизирован в ДБО
        :precondition:      Клиент нерезидент
        :precondition:      У клиента в ерк не заполнен тег PersonalNumberOther
        :precondition:      в itwCredoFront-process.properties параметр IsCheckClientData="false"
        :precondition:      В справочнике "info_guide_for_ibank" для строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" заполнено поле "Информация"
        :source_point:      52512
        :comment:           
        :tc_type:           +
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 17.04.2020
        :client_env:        Google Chrome 85 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 80 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 85 [Windows 10]
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'CreditCardSales'

    VARIANT = 'OnCredit'


    # :newpage: #######################################################################################################

    # :step: На форме вкладки "Заявки" нажимаем кнопку "Новая заявка"

    # :newpage: ######################################################################################################

    # :step: Создаем заявку по ссылке "ON-кредит за 5 минут"

    # :newpage: #######################################################################################################

    # :assert: Проверка не производится. Оформление заявки продолжается

    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)

@pytest.mark.skip(reason="Template")
def test_52512_408(app, credo_db):
    """
    {#
        :id:                52512_408
        :priority:          Средний
        :module:            Ядро/фронт
        :description:       Проверка контроля обязательного значения ДУЛ sprCode в ДБО, отправка сообщения пользователям с ролью admins
        :precondition:      Клиент авторизирован в ДБО
        :precondition:      У клиента в ерк есть ДУЛ со статусом 1 и незаполненным sprCode
        :precondition:      в itwCredoFront-process.properties параметр IsCheckClientData="true"
        :precondition:      В справочнике "info_guide_for_ibank" для строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" заполнено поле "Информация"
        :source_point:      52512
        :comment:           
        :tc_type:           +
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 09.12.2021
        :client_env:        Google Chrome 108 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 106 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 106 [Windows 10]
        :client_env:        Android 10, iOS 16.1
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'InBankTransfer'

    VARIANT = 'IntraBankTransfer_v1'


    # :newpage: #######################################################################################################

    # :step: На форме вкладки "Заявки" нажимаем кнопку "Новая заявка"

    # :newpage: ######################################################################################################

    # :step: Создаем заявку по ссылке "Переводы"

    # :newpage: #######################################################################################################

    # :assert: На форме отобразилось сообщение из поля "Информация" строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" справочника info_guide_for_ibank
    # :assert: Пользователям с ролью admins пришло сообщение с темой: «ДБО. Отсутствует обязательное значение:Тип документа (doc_type)»
    # :assert: emailBody: ФИО клиента: ОБЯЗАТЕЛЬНЫЕ ЗНАЧЕНИЯ ДБО Код ЕРК ISPPM1665498 Время оформления заявки: 16:42:14 Оформляемая заявка: InBankTransfer/by.itworks.credo.IntraBankTransfer_v1

    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)

@pytest.mark.skip(reason="Template")
def test_52512_411(app, credo_db):
    """
    {#
        :id:                52512_411
        :priority:          Средний
        :module:            Ядро/фронт
        :description:       Проверка контроля обязательного значения ДУЛ DocOrgan в ДБО, отправка сообщения пользователям с ролью admins
        :precondition:      Клиент авторизирован в ДБО
        :precondition:      У клиента в ерк есть ДУЛ со статусом 1 и незаполненным DocOrgan
        :precondition:      в itwCredoFront-process.properties параметр IsCheckClientData="true"
        :precondition:      В справочнике "info_guide_for_ibank" для строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" заполнено поле "Информация"
        :source_point:      52512
        :comment:           
        :tc_type:           +
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 09.12.2021
        :client_env:        Google Chrome 108 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 106 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 106 [Windows 10]
        :client_env:        Android 10, iOS 16.1
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'InBankTransfer'

    VARIANT = 'IntraBankTransfer_v1'


    # :newpage: #######################################################################################################

    # :step: На форме вкладки "Заявки" нажимаем кнопку "Новая заявка"

    # :newpage: ######################################################################################################

    # :step: Создаем заявку по ссылке "Переводы"

    # :newpage: #######################################################################################################

    # :assert: На форме отобразилось сообщение из поля "Информация" строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" справочника info_guide_for_ibank
    # :assert: Пользователям с ролью admins пришло сообщение с темой: «ДБО. Отсутствует обязательное значение:Кем выдан документ (doc_place)»
    # :assert: emailBody: ФИО клиента: ОБЯЗАТЕЛЬНЫЕ ЗНАЧЕНИЯ ДБО Код ЕРК ISPPM1665501 Время оформления заявки: 16:42:14 Оформляемая заявка: InBankTransfer/by.itworks.credo.IntraBankTransfer_v1

    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)

@pytest.mark.skip(reason="Template")
def test_52512_510(app, credo_db):
    """
    {#
        :id:                52512_510
        :priority:          Средний
        :module:            Ядро/фронт
        :description:       Проверка контроля обязательного значения ДУЛ DocNumber в ДБО, отправка сообщения пользователям с ролью admins
        :precondition:      Клиент авторизирован в ДБО
        :precondition:      У клиента в ерк есть ДУЛ со статусом 1 и незаполненным DocNumber
        :precondition:      в itwCredoFront-process.properties параметр IsCheckClientData="true"
        :precondition:      В справочнике "info_guide_for_ibank" для строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" заполнено поле "Информация"
        :source_point:      52512
        :comment:           
        :tc_type:           +
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 09.12.2021
        :client_env:        Google Chrome 108 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 106 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 106 [Windows 10]
        :client_env:        Android 10, iOS 16.1
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'OpenDepositDBO'

    VARIANT = 'OpenDepositDBO_v1'


    # :newpage: #######################################################################################################

    # :step: На форме вкладки "Заявки" нажимаем кнопку "Новая заявка"

    # :newpage: ######################################################################################################

    # :step: Создаем заявку по ссылке "Открытие онлайн депозита"

    # :newpage: #######################################################################################################

    # :assert: На форме отобразилось сообщение из поля "Информация" строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" справочника info_guide_for_ibank
    # :assert: Пользователям с ролью admins пришло сообщение с темой: «ДБО. Отсутствует обязательное значение:Номер документа (doc_nr)»
    # :assert: emailBody: ФИО клиента: ОБЯЗАТЕЛЬНЫЕ ЗНАЧЕНИЯ ДБО Код ЕРК ISPPM1665500 Время оформления заявки: 16:42:14 Оформляемая заявка: OpenDepositDBO/by.itworks.credo.OpenDepositDBO_v1

    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)

@pytest.mark.skip(reason="Template")
def test_52512_514(app, credo_db):
    """
    {#
        :id:                52512_514
        :priority:          Средний
        :module:            Ядро/фронт
        :description:       Проверка контроля валидности ДУЛ в ДБО, если дата выдачи меньше даты рождения, отправка сообщения пользователям с ролью admins
        :precondition:      Клиент авторизирован в ДБО
        :precondition:      У клиента в ерк есть ДУЛ со статусом 1, Дата выдачи ДУЛ < даты рождения
        :precondition:      в itwCredoFront-process.properties параметр IsCheckClientData="true"
        :precondition:      В справочнике "info_guide_for_ibank" для строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" заполнено поле "Информация"
        :source_point:      52512, 55271
        :comment:           
        :tc_type:           +
        :db_env:            База FORPOST: forp_d3; Тестовая дата: 09.12.2021
        :client_env:        Google Chrome 108 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Mozilla Firefox 106 [Windows 10; openSuSE Linux Leap 15.1]
        :client_env:        Microsoft EDGE 106 [Windows 10]
        :client_env:        Android 10, iOS 16.1
    }#
        :param: app: фикстура приложения
        :param: db_credo: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'OpenDepositDBO'

    VARIANT = 'OpenDepositDBO_v1'


    # :newpage: #######################################################################################################

    # :step: На форме вкладки "Заявки" нажимаем кнопку "Новая заявка"

    # :newpage: ######################################################################################################

    # :step: Создаем заявку по ссылке "Открытие онлайн депозита"

    # :newpage: #######################################################################################################

    # :assert: На форме отобразилось сообщение из поля "Информация" строки "(Сервер) Уведомление о необходимости явиться в банк для актуализации данных" справочника info_guide_for_ibank
    # :assert: Пользователям с ролью admins пришло сообщение с темой: «ДБО. Документ клиента невалиден: Дата выдачи документа (doc_dt).»
    # :assert: emailBody: ФИО клиента: ОБЯЗАТЕЛЬНЫЕ ЗНАЧЕНИЯ ДБО Код ЕРК ISPPM1665502 Время оформления заявки: 16:42:14 Оформляемая заявка: OpenDepositDBO/by.itworks.credo.OpenDepositDBO_v1

    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


