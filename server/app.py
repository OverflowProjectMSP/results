import uuid
import psycopg2
from psycopg2 import extras, Error
from flask import Flask, jsonify, request, session, make_response
from flask_cors import CORS, cross_origin
import smtplib
from email.mime.text import MIMEText
import random
from datetime import datetime


# instantiate the app
app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['PERMANENT_SESSION_LIFETIME'] = 3600
app.config["SESSION_COOKIE_SAMESITE"] = "None"
app.config["SESSION_COOKIE_SECURE"] =  True

# enable CORS
CORS(app, resources={r"*": {"origins": "http://localhost:5173", 'supports_credentials': True}})



# Обновление доп данных о 
def refresh_data(name = '', surname='', interestings='', about='', contacts='', country='', region='', city='', id=''):
    try:
        pg = psycopg2.connect("""
            host=localhost
            dbname=postgres
            user=postgres
            password=kos120675
            port=5432
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
        pg = psycopg2.connect("""
            host=localhost
            dbname=postgres
            user=postgres
            password=kos120675
            port=5432
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(f"SELECT COUNT(*) FROM users WHERE email=$${email}$$")
        # Проверка есть ли такой пользователь 
        if cursor.fetchone()[0] == 1:
            print(1)
            cursor.execute(f"SELECT * FROM users WHERE email=$${email}$$")
            user = cursor.fetchone()
            # Проверка пороля
            if user[3] == pas: 
                # res.set_cookie(f'{user[0]}', f'{user[1]}', max_age = 3600)
                session['id'] = user[0] # инициализация сессии
                session.modified = True
                return_data = f"Вход выполнен! Здравствуйте, {session['id']}"


            else: return_data = "Неверный пароль!"
        else: return_data = "Аккаунта с такой почтой не существует!"

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
        pg = psycopg2.connect("""
            host=localhost
            dbname=postgres
            user=postgres
            password=kos120675
            port=5432
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
        pg = psycopg2.connect("""
            host=localhost
            dbname=postgres
            user=postgres
            password=kos120675
            port=5432
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
        pg = psycopg2.connect("""
            host=localhost
            dbname=postgres
            user=postgres
            password=kos120675
            port=5432
        """)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        print(id)
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
        pg = psycopg2.connect("""
            host=localhost
            dbname=postgres
            user=postgres
            password=8533
            port=5432
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"SELECT * from questions")
        all_questions = cursor.fetchall()  

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

# Изменения пороля, если user знает страый
def change_password(password, old_password, email):
    try: 
        if check_old_password(old_password, email): # Вернет True если пороли стовпадает со старым 
            pg = psycopg2.connect("""
                host=localhost
                dbname=postgres
                user=postgres
                password=kos120675
                port=5432
            """)
            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cursor.execute(f'''UPDATE users
                            SET password=$${password}$$
                            WHERE email=$${email}$$;
                            ''')
            pg.commit()

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


# Проверка совпадениеия старого пороля с ныненшним
def check_old_password(email, password):
    
    try:
        pg = psycopg2.connect("""
            host=localhost
            dbname=postgres
            user=postgres
            password=kos120675
            port=5432
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        password_to_check = cursor.execute(f'SELECT password FROM users WHERE email=$${email}$$')

        if password_to_check == password:
            return_data = True
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


# Измения пороля с праолем на email
def change_password_send(password, email):
    try: 
        pg = psycopg2.connect("""
                    host=localhost
                    dbname=postgres
                    user=postgres
                    password=kos120675
                    port=5432
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

    for i in range(4):
        a = random.randint(0, 9)
        code_pas += str(a)

    msg = MIMEText(f"Ваш код для изменения пароля: {code_pas}. Не сообщайте его никому!")
    msg["Subject"] = "Ваш код"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login(sender, send_password)

    server.sendmail(sender, email, msg.as_string())

    # держим пороль в сессии
    session['code'] = code_pas
    session.modified = True


# Проверка совпадения кода с Frontend и реального кода
def check_password(password, true_password):
    if password == true_password:
        return_data = True
    else: return_data = True
    session.pop('sent-password', None)
    return return_data

# Добавление сообщения в бд (чат форума)
def chat(id, time, msg):
    try: 
        pg = psycopg2.connect("""
            host=localhost
            dbname=postgres
            user=postgres
            password=kos120675
            port=5432
        """)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        message_id = uuid.uuid4().hex # Записываем id сообщения в отдельную переменную для отпраки на клиент

        message_to_write = (message_id, id, time, msg)
        cursor.execute(f"INSERT INTO messages(message_id, user_id, time, msg) VALUES {message_to_write}")
        pg.commit()

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
        print(add_user_todb(post_data.get('name'), post_data.get('email'), post_data.get('password'))) #Вызов фунции добавления пользователя в бд и ее debug

    return jsonify(response_object)

#Изменение информации пользователя
@app.route('/user-info', methods=['GET', 'PUT'])
def user_info():
    response_object = {'status': 'success'} #БаZа

    if request.method == 'PUT':

        #------------ я хз че это ---------------------------------------------------------------------
        s = session.get('id')
        print(s)
        #----------------------------------------------------------------------------------------------
        
        #Вызов функции обновления бд
        post_data = request.get_json()
        refresh_data(post_data.get('Name'), 
                     post_data.get('Surname'), 
                     post_data.get('inrestings'), 
                     post_data.get('about'), 
                     post_data.get('contacts'), 
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
    print(session.get('id'))
    response_object = {'status': 'success'} #БаZа
    resp = make_response('Cookie set!')
    if request.method == 'POST':
        print(1) # Debug Константина
        post_data = request.get_json()
        resp.set_cookie('my_persistent_cookie', value='some_value', max_age=60*60*24)
        print(login_user(post_data.get('user'), post_data.get('password'))) #Вызов и debug функции проверки пароля пользователя (вход в аккаунт)
        return resp
        
    else:
        response_object['message'] = db_get()
        return jsonify(response_object)

#Новый вопрос
@app.route('/new-question', methods=['POST'])
def new_question():
    print(session.get('id')) #Debug
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
    return responce_object

if __name__ == '__main__':
    app.run()