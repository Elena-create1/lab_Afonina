class Employee():
  def __init__(self, name, id):
    self.name = name
    self.id = id
  def get_info(self):
    return f'имя работника: {self.name}, id: {self.id}'

class Manager(Employee):
  def __init__(self, name, id, department):
    Employee.__init__(self, name, id)
    self.department = department
  def get_info(self):
    return super().get_info() + f' , департамент: {self.department}'
  def manage_project(self):
    return f'{self.name} занимается управлением проектами в {self.department}'

class Technician(Employee):
  def __init__(self, name, id, specialization):
    Employee.__init__(self, name, id)
    self.specialization = specialization
  def get_info(self):
    return super().get_info()+f' , техническое обслуживание: {self.specialization}'
  def perform_maintenance(self):
    return f'{self.name} несет ответственность за проведение технического обслуживания в {self.specialization}'

class TechManager(Manager, Technician):
  def __init__(self, name, id, department, specialization):
    Manager.__init__(self, name, id, department)
    Technician.__init__(self, name, id, specialization)
    self.employees = []
  def skills(self):
    return f'{self.name} занимается управлением проектами в {self.department} и несет ответственность за проведение технического обслуживания в {self.specialization}'
  def add_employee(self, employee):
    self.employees.append(employee)
  def get_team_info(self):
    info = 'все сотрудники:\n'
    for sotru in self.employees:
      info += sotru.get_info() + '\n'
    return info


em1 = Employee('Софья','1')
print(em1.get_info())

maneg1 = Manager('Марк','2', 'продажи')
print(maneg1.get_info())
print(maneg1.manage_project())

tech1 = Technician('Влад', '3', 'cоздание сетей')
print(tech1.get_info())
print(tech1.perform_maintenance())

techmaneg1 = TechManager('Арина', '4', 'ИТ', 'системное администрирование')
print(techmaneg1.get_info())
print(techmaneg1.skills())

techmaneg1.add_employee(em1)
techmaneg1.add_employee(maneg1)
techmaneg1.add_employee(tech1)
techmaneg1.add_employee(techmaneg1)

print(techmaneg1.get_team_info())
