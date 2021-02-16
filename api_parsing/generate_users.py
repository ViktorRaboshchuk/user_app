import requests
import psycopg2
from sqlalchemy import create_engine


db_name = 'users'
db_user = 'username'
db_pass = 'secret'
db_host = 'db'
db_port = '5432'

db_string = 'postgres://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
db = create_engine(db_string)


def create_table():
    """
    Create table for user information
    """
    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users_table (
                                            id SERIAL,
                                            full_name text NOT NULL,
                                            street text NOT NULL,
                                            city text NOT NULL,
                                            state text NOT NULL,
                                            country text NOT NULL,
                                            latitude real not null,
                                            longitude real not null,
                                            dob text NOT NULL,
                                            age int not null,
                                            phone text not null
                                        ); """
    try:
        db.execute(sql_create_users_table)
        print('Table created')
    except Exception as e:
        print(e)
        print('Creation failed')


def add_data(data):
    """
    Insert data from API
    """
    sql = ''' INSERT INTO users_table(full_name,street,city,state,country,latitude,longitude,dob,age, phone)
                  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) '''
    db.execute(sql, data)


def parse_api(num):
    """
    Calling Random user API, and fetching data from response, and storing it too created table
    """
    request_url = 'https://randomuser.me/api/?gender=female&nat=us&results={}'
    response = requests.get(request_url.format(num))
    resp_result = response.json()
    print('API response', response)
    for user in resp_result['results']:
        user_data = []
        name = ' '.join([user['name']['title'], user['name']['first'], user['name']['last']])
        street = ''.join([str(user['location']['street']['number']), user['location']['street']['name']])
        city = user['location']['city']
        state = user['location']['state']
        country = user['location']['country']
        latitude = user['location']['coordinates']['latitude']
        longitude = user['location']['coordinates']['longitude']
        dob = user['dob']['date'].split('T')[0]
        age = user['dob']['age']
        phone = user['phone']
        user_data.append(name)
        user_data.append(street)
        user_data.append(city)
        user_data.append(state)
        user_data.append(country)
        user_data.append(latitude)
        user_data.append(longitude)
        user_data.append(dob)
        user_data.append(age)
        user_data.append(phone)
        add_data(user_data)


# Calling functions to fill users table
create_table()
parse_api(100)
