# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


class Person:

    def __init__(self, name, age=22):
        self.name = name
        self.age = age

    def getName(self):
        return self.name
    def getAge(self):
        return self.age



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    p1 = Person("jay", 33)

    print(p1.getAge())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
