# Name: Tim Garlick
# Course: CS1400
# Title: payroll shuffle
# people who helped me: google, book, collegue from work
# original problem: create a gui that accepts a txt file and loads employee information into fields that you can navigate through.
# major steps: learned how to upload a file and loop through a file and making it into an object by the use of a class.
# bullet list of lessons I learned:
# * how to use a class and how they are truly benificial when getting deactivate
# * how to loop through and dynamically create objects.

from tkinter.filedialog import askopenfilename

from graphics import *


class Employee:
   def __init__(self, employeeNumber, name, address, wage, hoursWorked):
       """An Employee class creates employee Number, address, wage, hoursWorked and has a calc_salary method."""
       self.employeeNumber = employeeNumber
       self.name = name
       self.address = address
       self.wage = float(wage)
       self.hoursWorked = float(hoursWorked)

   def calc_salary(self):
       """calc_salary calculates all of salary and returns the netwage"""
       if self.hoursWorked > 40:
           grossWage = 40 * self.wage
           overtimeHours = self.hoursWorked - 40
           overtimeWage = self.wage * 1.5 * overtimeHours
           grossWage = grossWage + overtimeWage
       else:
           grossWage = self.wage * self.hoursWorked
       fedTax = grossWage * .20
       stateTax = grossWage * .075
       netWage = grossWage - fedTax - stateTax
       return netWage

class Button:
    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""
    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, ’Quit’) """
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill("lightgray")
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()
    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)
    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()
    def activate(self):
        "Sets this button to ’active’."
        self.label.setFill("black")
        self.rect.setWidth(2)
        self.active = True
    def deactivate(self):
        "Sets this button to ’inactive’."
        self.label.setFill("darkgrey")
        self.rect.setWidth(1)
        self.active = False



def drawApplication(employees):
    """drawApplication draws all of my fields for information to be placed"""

    win = GraphWin('FluffShuffle Electronics', 700, 600)
    win.setBackground(color_rgb(240, 240, 240))

    topField = Rectangle(Point(340, 150), Point(650, 180))
    topField.setFill('white')
    topField.draw(win)

    middleField = Rectangle(Point(340, 200), Point(650, 230))
    middleField.setFill('white')
    middleField.draw(win)

    bottomField = Rectangle(Point(420, 250), Point(650, 280))
    bottomField.setFill('white')
    bottomField.draw(win)

    nextButton = Button(win, Point(630, 560), 100, 35, 'Next')
    nextButton.activate()

    previousButton = Button(win, Point(70, 560), 100, 35, 'Prev')
    previousButton.activate()
    exitButton = Button(win, Point(85, 25), 65, 30, 'Exit')
    exitButton.activate()

    Text(Point(315, 165), 'Name:').draw(win)
    Text(Point(310, 215), 'Address:').draw(win)
    Text(Point(390, 265), 'Net Pay:').draw(win)
    Text(Point(25, 25), 'File').draw(win)

    nameField = Text(Point(395, 165),'').draw(win)
    addressField = Text(Point(410, 215), '').draw(win)
    netWageField = Text(Point(450, 265), '').draw(win)
    navigateEmployeeInfo(employees, win, nextButton, previousButton, exitButton, nameField, addressField, netWageField)


#gives
def navigateEmployeeInfo(employees, win, nextButton, previousButton, exitButton, nameField, addressField, netWageField):
    """navigateEmployeeInfo populates all the empty fields with customer data and also
    provides the logic for scrolling to the next employee. It accepts employees list, win object, nextButton object, previousButton
    object, exitButton object, nameField, addressField, netWageField."""

    for i in range(len(employees)):
        print(employees[i].name)

    nameField.setText(employees[i].name)
    addressField.setText(employees[i].address)
    netWageField.setText('${0:0.2f}'.format(employees[i].calc_salary()))

    while True:
        mouse = win.getMouse()

        if nextButton.clicked(mouse) and i != 0:
            i = i-1
            nameField.setText(employees[i].name)
            addressField.setText(employees[i].address)
            netWageField.setText('${0:0.2f}'.format(employees[i].calc_salary()))

        elif previousButton.clicked(mouse) and i < (len(employees) - 1):
            i = i+1
            nameField.setText(employees[i].name)
            addressField.setText(employees[i].address)
            netWageField.setText('${0:0.2f}'.format(employees[i].calc_salary()))

        elif exitButton.clicked(mouse):
            win.getMouse()
            win.close()
#creates employee with selectedFile as parameter
def createEmployee(selectedFile):
    """createEmployee creates the employee from the list accepting the file uploaded by user"""
    employees = []
    while True:
        employeeNumber = selectedFile.readline()[:-1]
        if employeeNumber == "":
            break
        name = selectedFile.readline()[:-1]
        address = selectedFile.readline()[:-1]
        wage, hoursWorked = selectedFile.readline().strip().split()
        employees.append(Employee(employeeNumber, name, address, wage, hoursWorked))
    selectedFile.close()
    drawApplication(employees)
#opens file
def main():
    try:
        file = askopenfilename()
        selectedFile = open(file)
    except FileNotFoundError:
        print(file + " does not exist.")
        file = askopenfilename()
        selectedFile = open(file)
    except TypeError:
        print(file + " type is not supported.")
        file = askopenfilename()
        selectedFile = open(file)
    except ValueError:
        print(file + " not supported.")
        file = askopenfilename()
        selectedFile = open(file)
    #call createEmployee function
    createEmployee(selectedFile)
main()
