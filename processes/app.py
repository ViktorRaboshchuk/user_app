import folium
from flask import Flask, render_template, request, redirect
from folium import Popup
from sqlalchemy import create_engine

db_name = 'users'
db_user = 'username'
db_pass = 'secret'
db_host = 'db'
db_port = '5432'

db_string = 'postgres://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
db = create_engine(db_string)

app = Flask(__name__)


@app.route('/')
def index():
    """
    Get data from DB to render on main page
    """
    users = []
    sql = ''' SELECT id, full_name, state FROM users_table'''
    data = db.execute(sql)

    for dt in data:
        each_user = {'id': dt[0],
                     'name': dt[1],
                     'state': dt[2]}
        users.append(each_user)

    return render_template('index.html', users=users)


@app.route('/user/<int:user_id>', methods=['POST', 'GET'])
def user_info(user_id=None):
    """
    Get information for specific user, delete user, mark location on the map
    """
    sql = ''' SELECT *  FROM users_table where id = %s'''
    conn = db.connect()
    res = conn.execute(sql, (user_id,))
    user = res.first()
    conn.close()

    center = [-0.023559, 37.9061928]
    user_map = folium.Map(location=center, zoom_start=2)
    location = [user['latitude'], user['longitude']]
    folium.Marker(location, popup=Popup('Random user location ', show=True)).add_to(user_map)

    if request.method == 'POST':
        sql = ''' Delete  FROM users_table where id = %s'''
        db.execute(sql, (user_id,))
        return redirect('/')
    return render_template('user.html', user=user, user_id=user_id, user_map=user_map._repr_html_())


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
