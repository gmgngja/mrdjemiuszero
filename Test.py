import requests
from bs4 import BeautifulSoup


def login (user_login, user_password, session):
    data = {
        'AUTH_FORM': 'Y',
        'TYPE': 'AUTH',
        'USER_LOGIN': user_login,
        'USER_PASSWORD': user_password,
        'backurl': '/?login=yes'}
    response_login = session.post('https://www.mrdjemiuszero.com/auth/?login=yes', data=data)
    #print(response_login.status_code)
    if response_login.status_code != 200:
        raise RuntimeError('{} {}'.format(response_login.reason, response_login.status_code))
    return response_login.text


def order(session):
    response_order = session.get('https://www.mrdjemiuszero.com/personal/orders/')
    #print(response_order.status_code)
    if response_order.status_code != 200:
        raise RuntimeError('{} {}'.format(response_order.reason, response_order.status_code))
    return response_order.text


def test_login():
    user_login = ''
    user_password = ''
    session = requests.Session()

    login_page_text = login(user_login, user_password, session)
    login_page = BeautifulSoup(login_page_text, 'lxml')

    assert login_page.title.text == 'Личный кабинет', 'Не удалось зайти в личный кабинет'
    #print("Ассерт пройден")


def test_order():
    user_login = ''
    user_password = ''
    session = requests.Session()

    login(user_login, user_password, session)
    order_page_text = order(session)
    order_page = BeautifulSoup(order_page_text, 'lxml')

    assert order_page.title.text == 'Мои заказы', 'Не удалось открыть страницу "Мои заказы"'



#test_login()
#test_order()
#print('tests passed')
