class QErr:
    NOT_ACTIVE = 'Ивент не активен в данный момент'
    SALE_NOT_STARTED = 'Продажа билетов еще не началась'
    P_ID_NOT_FOUND = 'Не найден идентификатор оплаты'
    LEGAL = 'Неверные данные для заказа: ИНН и/или наименование организации не указаны либо не верны.'
    TICKETS_EMAIL_NON_UNIQ = 'Адреса электронной почты участников должны быть уникальны.' \
                             ' На каждый будет отправлен индивидуальный билет.'
    TICKETS_TYPE_ID_NONEXISTS = 'Неверный type_id в заказе, {type_id} не существует'
    TICKETS_TYPE_ID_DISABLED = 'Продажа билетов этого типа в данный момент невозможна.'
    MEST_NEMA = 'Для типа {type_id} недостаточно свободных мест'
