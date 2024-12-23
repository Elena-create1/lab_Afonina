#задание 1
class UserAccout():
    def __init__(self,username,email,password):
        self.username = username
        self.password = password
        self.email = email
    def set_password(self):
        print('введите старый пароль')
        a=input()
        if a==self.password:
            print('введите новый пароль')
            b=input()
            self.password=str(b)
        else:
            print('неверный пароль')
    def check_password(self,password):
        if password==self.password:
            return True
        else:
            print('введен старый пароль, измените его')
            return False

userr=UserAccout('абвгд','1111@gmail.com','01234567')
userr.set_password()
print(userr.check_password('12345678'))


#задание 2
class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def get_info(self):
        return f'название марки: {self.make}\nмодель: {self.model}'
class Car(Vehicle):
    def __init__(self,make,model,fuel_type):
        super().__init__(make,model)
        self.ft=fuel_type
    def get_info(self):
        s=super().get_info()
        return s +f'\nтип топлива: {self.ft}'
auto=Vehicle('Koenigsegg ','Agera')
print(auto.get_info())
add=Car('Koenigsegg','Agera','Бензин')
print(add.get_info())
