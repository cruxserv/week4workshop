class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password
        pass

    def change_name(self, name):
        new_name = name
        self.name = new_name

    def change_pin(self, pin):
        new_pin = pin
        self.pin = new_pin

    def change_password(self, password):
        new_password = password
        self.password = new_password


Driver Code for Task 1
bankuser1 = User("Bob", "1234", "password")
print(bankuser1.name, bankuser1.pin, bankuser1.password)

Driver Code for Task 2
bankuser1.change_name("Bobby")
bankuser1.change_password("newpassword")
print(bankuser1.name, bankuser1.pin, bankuser1.password)
