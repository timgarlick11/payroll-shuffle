# button.py
#    A simple Button widget.
from tkinter.filedialog import askopenfilename

from graphics import *

selectedFile = askopenfilename()
file = open(selectedFile)

class Employee:
    def __init__(self, employeeNumber, name, address, wage, hoursWorked):
        self.employeeNumber = employeeNumber
        self.name = name
        self.address = address
        self.wage = wage
        self.hoursWorked = hoursWorked

    def calc_salary(self):
        grossWage = wage * hoursWorked
        if hoursWorked > 40:
            overtimeHours = hoursWorked - 40
            overtimeWage = (wage + (wage/2)) * overtimeHours
            grossWage = grossWage + overtimeWage
        fedTax = grossWage * .80
        stateTax = grossWage * .925
        self.netWage = float(grossWage) - (fedTax + stateTax)




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







person = []
with file as f:
    linesOne = (line.rstrip() for line in f)
    lines = (line for line in linesOne if line)
    for line in lines:
        person.append(line)

employeeOne = Employee(person[0], person[1], person[2], person[3], person[4])
employeeTwo = Employee(person[5], person[6], person[7], person[8], person[9])
employeeThree = Employee(person[10], person[11], person[12], person[13], person[14])
employeeFour = Employee(person[15], person[16], person[17], person[18], person[19])
employeeFive = Employee(person[20], person[21], person[22], person[23], person[24])
employeeSix = Employee(person[25], person[26], person[27], person[28], person[29])
print(employeeSix.name)
