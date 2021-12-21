class Employee:
  def __init__(self, id, name, emp_id, dept, des, salary):
    self.id = id
    self.name = name
    self.emp_id = emp_id
    self.dept = dept
    self.des = des
    self.salary = salary

  def get_employee_name(self):
    print("Employee name is " + self.name)

