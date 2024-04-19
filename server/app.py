import os
import uuid
import psycopg2
from psycopg2 import extras, Error
from flask import Flask, jsonify, request, session, make_response
from flask_cors import CORS, cross_origin
import smtplib
from email.mime.text import MIMEText
import random
from datetime import datetime
from dotenv import load_dotenv
import base64


load_dotenv()
# instantiate the app
app = Flask(__name__)

app.secret_key = b'eewj'
app.config['PERMANENT_SESSION_LIFETIME'] = 3600
app.config["SESSION_COOKIE_SAMESITE"] = "None"
app.config["SESSION_COOKIE_SECURE"] =  'None'

# enable CORS
CORS(app, resources={r"*": {"origins": "http://localhost:5173", 'supports_credentials': True}})


# Добавление в картинки в БД
def push_image(image, user_id):
    try: 
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)


        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(f"""
            UPDATE users
            SET avatar = decode('{image}', 'base64')
            WHERE id = $$user_id$$
                """)
        pg.commit()
        print('Изобрадение было добавлено')
    except (Exception, Error) as error:
        print(f'DB ERROR: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            print("Соединение с PostgreSQL закрыто")
            return return_data


# Получение картинки из БД
def get_image(user_id):
    try: 
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(f"SELECT avatar from users WHERE id=$${user_id}$$")
        to_encode = bytes(cursor.fetchone()[0])
        print('base64 успешно отправлен')
        return base64.b64encode(to_encode)
    except (Exception, Error) as error:
        print(f'DB ERROR: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            print("Соединение с PostgreSQL закрыто")
            return return_data


# Обновление доп данных о 
def refresh_data(name = '', surname='', interestings='', about='', contacts='', country='', region='', city='', id=''):
    try:
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        # UPDATE user-info
        cursor.execute(f"""UPDATE users 
                    SET name = $${name}$$,
                        surname = $${surname}$$,
                        interestings = $${interestings}$$,
                        about = $${about}$$,
                        contacts = $${contacts}$$,
                        country = $${country}$$,
                        region=$${region}$$,
                        city=$${city}$$
                    WHERE id=$${id}$$;""")
        pg.commit()

        return_data = "Данные изменены"

    except (Exception, Error) as error:
        print(f'DB ERROR: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            print("Соединение с PostgreSQL закрыто")
            return return_data


# LogIn
def login_user(email, pas):
    try:
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(f"SELECT COUNT(*) FROM users WHERE email=$${email}$$")

        # Проверка есть ли такой пользователь 
        if cursor.fetchall()[0][0]==1:

            cursor.execute(f"SELECT * FROM users WHERE email=$${email}$$")
            user = cursor.fetchone()

            # Проверка пароля
            if user[3] == pas: 
                return_data = user[2]

                print(f"Вход выполнен! Здравствуйте, {user[2]}")
                return_data=['ok', user[1]]

            else: 
                print("Неверный пароль!")
                return_data = 'Неверный пароль!'
        else: 
            print("Аккаунта с такой почтой не существует!")
            return_data = "Аккаунта с такой почтой не существует!"

    except (Exception, Error) as error:
        print(f'DB ERROR: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            print("Соединение с PostgreSQL закрыто")
            return return_data


# Get шифы с бд
def db_get():
    try:
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        
        pg.commit()

        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()

        return_data = []
        for row in result:
            return_data.append(dict(row))

    except (Exception, Error) as error:
        return_data = f"Ошибка получения данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            print("Соединение с PostgreSQL закрыто")
            return return_data


# Регистрация пользователя
def add_user_todb(name, email, pas):
    try:
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        send_user = []
        cursor.execute(f"SELECT COUNT(*) FROM users WHERE nickname=$${name}$$")  
        send_user.append(cursor.fetchone())

        cursor.execute(f"SELECT COUNT(*) FROM users WHERE email=$${email}$$")
        send_user.append(cursor.fetchone())
        # Проверка существует ли такой пользователь
        if send_user[0][0] == 0 and send_user[1][0] == 0:
            user_to_write = (uuid.uuid4().hex, name, email, pas, False)
            
            cursor.execute(f"INSERT INTO users(id, nickname, email, password, admin) VALUES {user_to_write}")      
            
            pg.commit()
            
            return_data = "Пользователь зарегестрирован!"

        else:
            return_data = "Пользователь с таким именем или почтой уже существует!"

    except (Exception, Error) as error:
        print(f'DB ERROR: ', error)
        return_data = f"Ошибка добавления в базу данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            print("Соединение с PostgreSQL закрыто")
            return return_data


# Новый вопрос
def add_question(discriptions='', details='', dificulty='', tag='', id=''):
    try: 
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        send_question = []

        cursor.execute(f"SELECT COUNT(*) FROM questions WHERE discriptions=$${discriptions}$$")  
        
        send_question.append(cursor.fetchone())
        # Существует ли такой же вопрос
        if send_question[0][0]==0:
            print(details, 1)
            question_to_write = (uuid.uuid4().hex, discriptions, details, dificulty, tag, id)
            cursor.execute(f"INSERT INTO questions(id, discriptions, details, dificulty, tag, user_id) VALUES {question_to_write}")      
            pg.commit()
            
            
        return_data = "Вопрос добавлен"
    except (Exception, Error) as error:
        print(f'DB ERROR: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            print("Соединение с PostgreSQL закрыто")
            return return_data


# Отображение всех вапросов на frontend
def render_questions():
    try: 
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"SELECT * from questions")

        all_questions = cursor.fetchall()  

        print('Вопросы отображены')

        return_data = all_questions

    except (Exception, Error) as error:
        print(f'DB ERROR: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            print("Соединение с PostgreSQL закрыто")
            return return_data


# Изменения пароля, если user знает страый
def change_password(password, old_password, email):
    try: 
        if check_old_password(old_password, email): # Вернет True если пароли стовпадает со старым 
            pg = psycopg2.connect(f"""
                host=localhost
                dbname=postgres
                user=postgres
                password={os.getenv('PASSWORD_PG')}
                port={os.getenv('PORT_PG')}
            """)
            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cursor.execute(f'''UPDATE users
                            SET password=$${password}$$
                            WHERE email=$${email}$$;
                            ''')
            pg.commit()

            print('Пароль изменен')

            return_data = True

        else: return_data = False

    except (Exception, Error) as error:
        return_data = f"Ошибка получения данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            print("Соединение с PostgreSQL закрыто")
            return return_data


# Проверка совпадениеия старого пароля с ныненшним
def check_old_password(email, password):
    try:
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        password_to_check = cursor.execute(f'SELECT password FROM users WHERE email=$${email}$$')

        if password_to_check == password:
            return_data = True
            print('Пароли не совпадают')
        else: return_data = False

    except (Exception, Error) as error:
        print(f'DB ERROR: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            print("Соединение с PostgreSQL закрыто")
            return return_data


# Измения пароля с праолем на email
def change_password_send(password, email):
    try: 
        pg = psycopg2.connect(f"""
                    host=localhost
                    dbname=postgres
                    user=postgres
                    password{os.getenv('PASSWORD_PG')}*
                    port={os.getenv('PORT_PG')}
                """)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f'''UPDATE users
                        SET password=$${password}$$
                        WHERE email=$${email}$$;
                        ''')
        pg.commit()
    except (Exception, Error) as error:
        return_data = f"Ошибка получения данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            print("Соединение с PostgreSQL закрыто")
            return return_data


# Отпрака кода на почту
def send_code(email):
    sender = "upfollow835@gmail.com"
    send_password = "zwrx qgne arwj jblp"

    code_pas = ""

# ------------------------Улучшить бы----------------------------------------------------
    for i in range(4):
        a = random.randint(0, 9)
        code_pas += str(a)
#-----------------------------------------------------------------------------------------
    
    msg = MIMEText(f"Ваш код для изменения пароля: {code_pas}. Не сообщайте его никому!")
    msg["Subject"] = "Ваш код"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login(sender, send_password)

    server.sendmail(sender, email, msg.as_string())

    # держим пароль в сессии
    session['code'] = code_pas
    session.modified = True

    print('Пароль отправлен на почту')

    return 0


# Проверка совпадения кода с Frontend и реального кода
def check_password(password, true_password):
    if password == true_password:
        return_data = True
        print('Пароли совпали')
    else: 
        print('Пароли не совпали')
        return_data = False
    session.pop('sent-password', None)
    return return_data


# Добавление сообщения в бд (чат форума)
def chat(id, time, msg):
    try: 
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        message_id = uuid.uuid4().hex # Записываем id сообщения в отдельную переменную для отпраки на клиент

        message_to_write = (message_id, id, time, msg)
        cursor.execute(f"INSERT INTO messages(message_id, user_id, time, msg) VALUES {message_to_write}")
        pg.commit()

        print('Сообщение добавлено')

        return_data = message_id

    except (Exception, Error) as error:
        print(f'DB ERROR: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            print("Соединение с PostgreSQL закрыто")
            return return_data


# Добоволение статьи
def add_states(discriptions='', details='', id=''):
    try: 
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        print(id)

        send_question = []

        cursor.execute(f"SELECT COUNT(*) FROM states WHERE discriptions=$${discriptions}$$")  
        send_question.append(cursor.fetchone())

        # Существует ли таккая же
        if send_question[0][0]==0:
            print(details, 1)
            question_to_write = (uuid.uuid4().hex, discriptions, details, id)
            cursor.execute(f"INSERT INTO states(id, discriptions, details, dificulty, tag, user_id) VALUES {question_to_write}")      
            pg.commit()
            
        print('Статья добавлена')

        return_data = "Вопрос добавлен"
    except (Exception, Error) as error:
        print(f'DB ERROR: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            print("Соединение с PostgreSQL закрыто")
            return return_data


# Все вопросы/статьи от одного юзера
def show_all_by_user(id):
    try: 
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        questions = cursor.execute(f'''SELECT * FROM questions
                                WHERE id=$${id}$$''')
        
        states = cursor.execute(f'''SELEСT * FROM states
                                WHERE id=$${id}$$''')
        
        print('Информация отпраленна')

        return_data = {
            'questions': questions,
            'states': states
        }
    except (Exception, Error) as error:
        print(f'DB ERROR: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            print("Соединение с PostgreSQL закрыто")
            return return_data


# Фильтр 
def filtre(filtres, category):
    pass


# удалить что-то
def delete(id, isQ):
    if isQ:
        try: 
            pg = psycopg2.connect(f"""
                host=localhost
                dbname=postgres
                user=postgres
                password={os.getenv('PASSWORD_PG')}
                port={os.getenv('PORT_PG')}
            """)
            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cursor.excute(f'''DELETE FROM questions 
                          WHEREE id=$${id}$$''')

            pg.commit()
            return_data = 'ok'
            
        except (Exception, Error) as error:
            print(f'DB ERROR: ', error)
            return_data = f"Ошибка обращения к базе данных: {error}" 

        finally:
            if pg:
                cursor.close
                pg.close
                print("Соединение с PostgreSQL закрыто")
                return return_data
    else:
        try: 
            pg = psycopg2.connect(f"""
                host=localhost
                dbname=postgres
                user=postgres
                password={os.getenv('PASSWORD_PG')}
                port={os.getenv('PORT_PG')}
            """)
            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cursor.excute(f'''DELETE FROM states
                          WHEREE id=$${id}$$''')
            pg.commit()
            return_data = 'ok'
        except (Exception, Error) as error:
            print(f'DB ERROR: ', error)
            return_data = f"Ошибка обращения к базе данных: {error}" 

        finally:
            if pg:
                cursor.close
                pg.close
                print("Соединение с PostgreSQL закрыто")
                return return_data


# обновить что-то
def change(id, info, isQ):
    infor = info # без for
    if isQ:
        try: 
            pg = psycopg2.connect(f"""
                host=localhost
                dbname=postgres
                user=postgres
                password={os.getenv('PASSWORD_PG')}
                port={os.getenv('PORT_PG')}
            """)
        
            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cursor.excute(f'''UPDATE questions
                        SET (information)
                          WHEREE id=$${id}$$''')

            pg.commit()
            return_data = 'ok'
            
        except (Exception, Error) as error:
            print(f'DB ERROR: ', error)
            return_data = f"Ошибка обращения к базе данных: {error}" 

        finally:
            if pg:
                cursor.close
                pg.close
                print("Соединение с PostgreSQL закрыто")
                return return_data
    else:
        try: 
            pg = psycopg2.connect(f"""
                host=localhost
                dbname=postgres
                user=postgres
                password={os.getenv('PASSWORD_PG')}
                port={os.getenv('PORT_PG')}
            """)
            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cursor.excute(f'''UPDATE states
                        SET (information)
                          WHEREE id=$${id}$$''')
            pg.commit()
            return_data = 'ok'
        except (Exception, Error) as error:
            print(f'DB ERROR: ', error)
            return_data = f"Ошибка обращения к базе данных: {error}" 

        finally:
            if pg:
                cursor.close
                pg.close
                print("Соединение с PostgreSQL закрыто")
                return return_data


# Вопросы форума    
def show_forum(filtre):
    try:
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        states = cursor.excute(f'''SELECT * FROM states WHERE tag=$${filtre}$$''')
        questions = cursor.excute(f'''SELECT * FROM questions WHERE tag=$${filtre}$$''')
        
        return_data = {
            "states": states,
            "questions": questions
        }

        print(f'Вся информация о форуме {filtre} была отправлена')
        pg.commit()
    except (Exception, Error) as error:
        print(f'DB ERROR: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            print("Соединение с PostgreSQL закрыто")
            return return_data


# Отображение всех статей на frontend
def render_states():
    try: 
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"SELECT * from states")
        
        all_states = cursor.fetchall()  
        print('все статьи отображены')

        return_data = all_states

    except (Exception, Error) as error:
        print(f'DB ERROR: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            print("Соединение с PostgreSQL закрыто")
            return return_data
        

# Показываем что-то определенное
def show_one(id, isQ):
    if isQ:
        try: 
            pg = psycopg2.connect(f"""
                host=localhost
                dbname=postgres
                user=postgres
                password={os.getenv('PASSWORD_PG')}
                port={os.getenv('PORT_PG')}
            """)

            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cursor.execute(f"SELECT * from states WHERE id = $${id}$$")
            
            all_states = cursor.fetchall()  


            return_data = all_states

        except (Exception, Error) as error:
            print(f'DB ERROR: ', error)
            return_data = f"Ошибка обращения к базе данных: {error}" 

        finally:
            if pg:
                cursor.close
                pg.close
                print("Соединение с PostgreSQL закрыто")
                return return_data
    try: 
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"SELECT * from states WHERE id = $${id}$$")
        
        all_states = cursor.fetchall()  

        return_data = all_states

    except (Exception, Error) as error:
        print(f'DB ERROR: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            print("Соединение с PostgreSQL закрыто")
            return return_data
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Главная страница
@app.route('/', methods=['GET'])
def home():

    response_object = {'status': 'success'} #БаZа
    response_object['message'] = session.get('username')

    print(session.get('username')) #debug

    return jsonify(response_object)

#Регистрация
@app.route('/registration', methods=['GET', 'POST'])
def user_registration():
    response_object = {'status': 'success'} #БаZа

    if request.method == 'POST':
        post_data = request.get_json()
        # print(add_user_todb(post_data.get('name'), post_data.get('email'), post_data.get('password'))) #Вызов фунции добавления пользователя в бд и ее debug
        print(request.cookies.get('all'))
    return jsonify(response_object)

#Изменение информации пользователя
@app.route('/user-info', methods=['GET', 'PUT'])
def user_info():
    response_object = {'status': 'success'} #БаZа

    if request.method == 'PUT':
        #Вызов функции обновления бд
        post_data = request.get_json()
        refresh_data(post_data.get('Name'), 
                     post_data.get('Surname'), 
                     post_data.get('interestings'), 
                     post_data.get('about'), 
                     post_data.get('contacts'), # contactsType 
                     post_data.get('Country'), 
                     post_data.get('Region'), 
                     post_data.get('City'),
                     session.get('id'))
        
    else:
        response_object['message'] = db_get()

    return jsonify(response_object)

#Вход
@app.route('/login', methods=['GET', 'POST'])
def login():
    response_object = {'status': 'success'} #БаZа
    resp = make_response(jsonify(response_object)) #куки-заготовка
    resp.headers['Content-Type'] = 'text/plain'
    if request.method == 'POST':
        post_data = request.get_json()
        a = login_user(post_data.get('email'), post_data.get('password'))

        if a[0] == 'ok': #Вызов и debug функции проверки пароля пользователя (вход в аккаунт)
            resp.set_cookie('all', a[1])
            session['all'] = a[1]
            session.modified = True
            resp.set_data('ok')

        else: resp.set_data(a[0])

    else:
        response_object['message'] = db_get()
        
    return resp

#Новый вопрос
@app.route('/new-question', methods=['POST'])
def new_question(): 
    response_object = {'status': 'success'} #БаZа

    post_data = request.get_json()

    print(add_question(post_data.get('discriptions'), post_data.get('details'), post_data.get('dificulty'), post_data.get('tag'), session.get('id'))) #Вызов и debug функции добавления вопроса в бд
    
    return jsonify(response_object)

#Страница со всеми вопросами
@app.route('/show-questions', methods=['GET'])
def show_questions():
    response_object = {'status': 'success'} #БаZа
    response_object['message'] = render_questions() #Вызов и возврат ответа на клиент функции для получения всех вопросов
    
    return jsonify(response_object)

#Обновление пароля
@app.route('/new-password-old', methods=['PUT'])
def new_password_with_old():

    response_object = {'status': 'success'} #БаZа
    post_data = request.get_json()

    #Вызов, debug и возврат ответа на клиент функции обновления пароля
    if request.method=='PUT':
        response_object['changeable'] = change_password(post_data.get('new-password'),post_data.get('old_passord') ,post_data.get('email'))
        print(response_object['changeable'])
    
    return jsonify(response_object)

#Восстановление пароля
@app.route('/new-password-email', methods=['POST', 'PUT'])
def new_password_with_email():
    response_object = {'status': 'success'} #БаZа
    post_data = request.get_json()

    if request.method=='PUT':
        #Восстановление пароля если мы в аккаунте
        change_password_send(post_data('new-password'), session.get('email'))
    
    elif request.method == 'POST' and post_data.get('email'):
        #Восстановление пароля если мы НЕ в аккаунте
        print(send_code(post_data.get('email')))
    
    else:
        # ХЗ, вроде проверка кода подтверждения
        response_object['status'] = check_password(post_data.get('password'), session.get('code'))
    
    return jsonify(response_object)

# Чат форума
@app.route('/chat', methods=['POST', 'PUT'])
def chat_forum():
    responce_object = {'status' : 'success'} #БаZа
    post_data = request.get_json()

    if request.method == 'PUT': # Обновка вопроса
        pass
    else: 
        responce_object['id_question'] = chat(session.get('id'), datetime.now(), post_data.get('msg')) #   Возвращает id сообщения и добовляет его в бд (сообщение)       
    
    return jsonify(responce_object)

# Новая статья
app.route('/new-state', methods = ['POST'])
def create_state(): 
    responce_object = {'status' : 'success'} #БаZа

    post_data = request.get_json()

    print(add_states(post_data.get('discriptions'), post_data.get('details'), session.get('id'))) #Вызов и debug функции добавления вопроса в бд
    
    return jsonify(responce_object)

# Фильтр статей
app.route("/filtre-states", methods=['GET'])
def filtre_states():
    responce_object = {'status' : 'success'} #БаZа

    post_data = request.get_json()

    responce_object['all'] = filtre(post_data.get('filters'), 'Стать')

    return jsonify(responce_object)

# Фильтр вопросов
app.route("/filtre-questions", methods=['GET'])
def filtre_questions():
    responce_object = {'status' : 'success'} #БаZа

    post_data = request.get_json()

    responce_object['all'] = filtre(post_data.get('filters'), 'Вопрос')

    return jsonify(responce_object)

# Вопросы форума
app.route('/show-forum', methods=['GET'])
def show_f():
    responce_object = {'status' : 'success'} #БаZа

    post_data = request.get_json()

    responce_object['all'] = show_forum(post_data.get('filters'))

    return jsonify(responce_object)

# Одино что-то
app.route('/question', methods=['GET'])
def one_something():
    responce_object = {'status': 'success'}

    post_data = request.get_json()

    if post_data.get('question'):
        responce_object['all'] = show_one(post_data.get('id'), True)
    else:
        responce_object['all'] = show_one(post_data.get('id'), True)


    return jsonify(responce_object)

# может ли юзер удалять/менять или нет
app.route('/check-user',methods=['POST'])
def check_user():
    responce_object = {'status' : 'success'} #БаZа

    post_data = request.get_json()

    if  post_data.get('id')==session.get('id'):
        responce_object['user'] = True
    else: 
        responce_object['user']=False

    return jsonify(responce_object)

# Удаление чего-то
app.route('/delete',methods=['DELETE'])
def delete_():
    responce_object = {'status' : 'success'} #БаZа

    post_data = request.get_json()
    if post_data.get('question'):
        responce_object['all'] = delete(post_data.get('id'), True) # а что - решим потом (название поменять надо)
    else:
        responce_object['all'] = delete(post_data.get('id'), False) # а что - решим потом (название поменять надо)
    
    print(responce_object['all'])

    return jsonify(responce_object)

# Изменение чего-то
app.route('/change',methods=['PUT'])
def change_():
    responce_object = {'status' : 'success'} #БаZа

    post_data = request.get_json()

    if post_data.get('question'):
        responce_object['all'] = change(post_data.get('id'), post_data.get('all'), True) # а что - решим потом (название поменять надо)
    else: 
        responce_object['all'] = change(post_data.get('id'), post_data.get('all'), False) # а что - решим потом (название поменять надо)

    print(responce_object['all'])

    return jsonify(responce_object)

#Страница со всеми статьями
@app.route('/show-states', methods=['GET'])
def show_sates():
    response_object = {'status': 'success'} #БаZа

    response_object['message'] = render_states() #Вызов и возврат ответа на клиент функции для получения всех вопросов
    
    return jsonify(response_object)

# проверка может ли юзер исправлять что-то
@app.route('/check-user', methods=['GET'])
def check():
    response_object = {'status': 'success'} #БаZа

    post_data = request.get_json()

    if post_data.get('id') == request.cookies.get('all'):
        response_object['isEdit'] = True

    else:
        response_object['isEdit'] = False

    return  jsonify(response_object)

# проверка может ли юзер исправлять что-то
@app.route('/show-all-by-user', methods=['GET'])
def check_():
    response_object = {'status': 'success'} #БаZа

    post_data = request.get_json()

    response_object['all'] = show_all_by_user(post_data.get('id'))

    print('Отправлено')
    return  jsonify(response_object)

if __name__ == '__main__':
    app.run()

'''
from flask import jsonify, make_response

@app.route('/your-endpoint')
def your_function():
    response = make_response(jsonify(my_dictionary))
    # Добавляем заголовок Content-Type
    response.headers['Content-Type'] = 'application/json'
    return response
'''