@pytest.mark.skip(reason="Template")
def test_57101_1(app, credo_db, forpost_db):
    """
    {#
        :id:                57101_1
        :priority:          Средний
        :module:            Ценные бумаги
        :description:       Проверка установки котировок актуальных ЦБ
        :precondition:      Пользователь admin авторизован
        :precondition:      У пользователя admin присутствуют все роли и права доступа
        :precondition:      В справочнике ценных бумаг для ЦБ "ВГДО 153" и "ВГДО 171" установлена актуальность = 1
        :precondition:      После запроса в сервис ценных бумаг актуальна только ЦБ "ВГДО 171"
        :precondition:      Для ЦБ "ВГДО 153" присутствуют ранее установленные котировки
        :precondition:      Для ЦБ "ВГДО 171" присутствуют ранее установленные котировки
        :comment:           С помощью SoapUI создали имитацию сервиса получения курсов ценных бумаг из Diling - ответа на запрос GetBonds (возвращаем ответ из оригинальной системы, полученный запросом из ServMoney, т.к. доступ к Diling есть только оттуда). Пример файла ответа прикреплен к задаче по тестированию
        :source_point:      RM56476;
        :tc_type:           +
        :db_env:            БД: Node9_Rates;
        :client_env:        Google Chrome 96 [Windows 10; openSuSE Linux Leap 15.3]
        :client_env:        Mozilla Firefox 94 [Windows 10; openSuSE Linux Leap 15.3]
        :client_env:        Microsoft EDGE 96 [Windows 10]
        :time_of_test:      30
        :precondition_time: 10
        :count_of_check:    3
    }#
        :param: app: фикстура приложения
        :param: credo_db: фикстура базы данных
    """

    value = ''
    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)


    PRODUCT = 'RateAndPriceChange'
    VARIANT = 'BondChange'

    # :newpage: #######################################################################################################

    # :step: Переходим во вкладку "Список заявок"
    # :step: Нажимаем на кнопку "Новая заявка"
    # :step: В поле "Вариант" выбираем значение
    value = 'Установка котировок ЦБ'
    # :step: Нажимаем на кнопку "Создать заявку"

    # :newpage: #######################################################################################################

    # :step: В поле "Сотрудник ОНО для ввода котировок" выбираем значение
    value = 'Administrator User'
    # :step: В поле "Ценные бумаги" выбираем значение
    value = 'ВГДО 171 1000 USD'
    # :assert: В поле "Ценные бумаги" отсутствует ЦБ "ВГДО 153 1000 USD"
    # :step: Нажимаем на кнопку "Завершить"

    # :newpage: #######################################################################################################

    # :assert: В списке присутствует ЦБ "ВГДО 171 1000 USD"
    # :assert: В списке отсутствует ЦБ "ВГДО 153 1000 USD"

    # :newpage: #######################################################################################################

    # :step: Переходим во вкладку "Ценные бумаги"
    # :assert: У ЦБ "ВГДО 153" актуальность сменилась на 0


    logrecord = "{time} [{module}] -- [{method}]".format(time=datetime.now().strftime("%H:%M:%S,%f"), module=(os.path.basename(__file__)), method=(sys._getframe().f_code.co_name))
    print(logrecord)
