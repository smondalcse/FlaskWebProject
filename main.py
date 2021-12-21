from flask import Flask, request, render_template
from employee import Employee as imported_employee

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


if __name__ == "__main__":
    app.run(debug=True)
