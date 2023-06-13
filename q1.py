#file = open('password.txt', 'w')
#file.write('1903_matjan')
#file.write('\nfaizal13')
#file.write('\nhaha@faizal213HAHA')
#file.write('\njaja')
#file.write('\nioio')
#file.write('\nlalalalal')
#file.close()

class PasswordManager():
    def __init__(self,old_password,current_password):
        self.old_password = old_password
        self.current_password = current_password

    def get_password(self):
        current_pass = self.current_password
        return current_pass
    
    def set_password(self):
        #print(f'Please enter your password : {self.old_password}')
        if self.old_password not in self.old_password:
            print(f'Your password is different from the old password {self.old_password} so do you want to reset your password : ? ( Yes or No)')
            if ans == 'Yes':
                ans = self.current_password
                ans.write('password.txt','a')
                ans = '\n' + self.current_password
                ans.close()
            else:
                print('You still used the old password')
    
    def is_correct(self):
        if self.current_password == object.set_password():
          print('Your password is wrong')
        else:
            print("You changed your new password")
            object.set_password()

passwordd = input('Please enter your new password to reset: ')
list_of_password = PasswordManager(passwordd)
object.is_correct()
