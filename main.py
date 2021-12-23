from flask import Flask, request, render_template
from employee import Employee as imported_employee
import pandas as pd
import DBConnection
import pymssql
import Predictor

app = Flask(__name__)


users = [
    {
        'id': "1",
        'name': "Sanat Mondal",
        'emp_id': "20170546",
        'dept': "IT",
        'des': "Asst Manager",
        'salary': "20000"
    }, {
        'id': "2",
        'name': "Badal Biswas",
        'emp_id': "20181010",
        'dept': "IT",
        'des': "Asst Manager",
        'salary': "30000"
    }, {
        'id': "3",
        'name': "Sonjoy Day",
        'ID': "20170546",
        'Dept': "IT",
        'salary': "25000"
    }, {
        'id': "4",
        'name': "AlimUddin",
        'emp_id': "20150551",
        'dept': "IT",
        'des': "Manager",
        'salary': "22000"
    }
]


@app.route('/')
def home_page():
    return render_template('login.html')


@app.route('/home',  methods=['POST', 'GET'])
def home():

    # How to access Class and object
    # obj_imp_emp = imported_employee("4", "AlimUddin", "20150551", "IT", "Manager", "22000")
    # obj_imp_emp.name

    x = dict()
    emp_id = request.form["emp_id"]
    if request.form['action'] == 'Login':
        return "Login"
    if request.form['action'] == 'Show Emp':
        for objEmp in users:
            if emp_id == objEmp['emp_id']:
                x = objEmp
                break
        return render_template('home.html', objEmployee=x)
    else:
        return "None"


@app.route('/show_emp',  methods=['POST'])
def show_emp():
    return "show emp"


@app.route('/db_conn', methods=['get'])
def db_conn():
    # connc = DBConnection.Connection('SQL Server', 'ITDEV22', 'NMLCustomerInfo', 'sa', '123', 'yes')
    connc = DBConnection.Connection('SQL Server', '192.168.11.57', 'NMLSALES2122', 'adminsales', 'Ad@MSsql2014', 'yes')
    conn = connc.db_connect()
    return 'success'


@app.route('/get_user_from_db', methods=['get'])
def get_user_from_db():
    conn = db_conn()
    cursor = conn.cursor()
    cursor.execute('select top(10)* from tblUsers')
    for row in cursor:
        print(row)
    return 'success'


@app.route('/get_user_using_sp', methods=['get'])
def get_user_using_sp():
    conn = dbconectwithpy()
    sp = 'EXEC getSalesPredictionData_yearly'.format()
    result = pd.read_sql_query(sp, conn)
    print(result)
    lin_prediction_data = Predictor.Predictor.linear_prediction(result, 2021)
    poly_prediction_data = Predictor.Predictor.polynomial_prediction(result, 2021)
    x = 'lin_prediction_data ==>> ', lin_prediction_data[0], '. poly_prediction_data ==>>', poly_prediction_data[0]
    print(x)
    return str(x)


@app.route('/dbconectwithpy', methods=['get'])
def dbconectwithpy():
    conn = DBConnection.Connection.db_connect_pymssql('192.168.11.57', 'adminsales', 'Ad@MSsql2014', 'NMLSALES2122')
    # cursor = conn.cursor(as_dict=True)
    return conn


if __name__ == "__main__":
    app.run(debug=True)
