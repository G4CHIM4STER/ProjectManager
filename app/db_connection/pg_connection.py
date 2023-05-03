"""
Модуль, при поиощи которого осуществляется  соединение с БД
"""
import psycopg2
from configparser import ConfigParser

def connect():
    """
    connect Функция создающая соединение с БД. При помощи данных из конфига, в котором находятся креды.
    Таже, внутри функции создается переменная conn, при помощи которой будет создаваться курсор, а так же 
    закрываться соединение с БД.
    """
    global conn
    try:
        # Считываем параметры соединения из конфига
        params = config()

        # Соединение с БД
        print('Подключение к PostgreSQL...')
        conn = psycopg2.connect(**params)
        print('Подключение успешно')

        # Прокидываем исключения
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)



# Функция создания конфигурации. В случае изменения конфига, необходимо переписать название используемого конфига в следующей строке
def config(filepath = r'/run/media/g4chi/5260B70160B6EABD/g4chi_storage/code/Projects/ProjectManager/app/db_connection/settings.ini', section = 'postgresql'):
    """
    config Функция, парсящая конфиг с раширение .ini, в котоом находятся креды для соединия с БД.

    Args:
        filepath (str): Строка в которой прописан путь к .ini файлу. 
        section (str): Название секции внутри .ini файла, из которой будут браться данные для покдлючения к БД. 

    Raises:
        Exception: Исключение, возвращающее название секции и файла, в котором скрипт пытался найти данную функцию.

    Returns:
        db (dict): Словарь, в котором запсаны основные креды для покдлючения к БД
    """
    parser = ConfigParser()
    parser.read(filepath)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception ('Секция {0} не найдена в файле {1} '.format(section, filepath))
    return db
