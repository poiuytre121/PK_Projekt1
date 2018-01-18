from tkinter import *
from tkinter import messagebox
from config.config import *
from classes.student import *


class MainWindow(object):

    def __init__(self, tk):
        """
        Initializes new instance of Window class

        :param Tk tk:
        """
        # btnCountAverage
        self.btnCountAverage = Button()
        self.btnCountAverage['text'] = "Policz średnią"
        self.btnCountAverage['width'] = 20
        self.btnCountAverage['command'] = self.CountAverage
        self.btnCountAverage.grid(column=2, columnspan=2)

        # btnSaveReport
        self.btnSaveReport = Button()
        self.btnSaveReport['text'] = "Zapisz raport do pliku csv"
        self.btnSaveReport['width'] = 20
        self.btnSaveReport.grid(column=2, columnspan=2)

        # btnGenerateCertificate
        self.btnGenerateCertificate = Button()
        self.btnGenerateCertificate['text'] = "Wygeneruj świadectwo"
        self.btnGenerateCertificate['width'] = 20
        self.btnGenerateCertificate.grid(column=2, columnspan=2)

        # subject labels and grade input fields
        self.selectsStudentGrades = []
        row = 0
        for subject_name in get_subjects_names():
            label = Label()
            label['text'] = subject_name
            label.grid(column=0, row=row)
            selectedOption = StringVar()
            selectedOption.set(Student.possible_grades[4])
            a = OptionMenu(tk, selectedOption, *Student.possible_grades)
            a['height'] = 1
            a['width'] = 10
            a.grid(column=1, row=row)
            self.selectsStudentGrades.append(selectedOption)
            row += 1

        # label and input for behaviour (using row from previous generation)
        self.labelBehaviour = Label()
        self.labelBehaviour['text'] = "Zachowanie"
        self.labelBehaviour.grid(column=0, row=row)
        self.selected_behaviour_option = StringVar()
        self.selected_behaviour_option.set(Student.possible_behaviour_grades[3])
        self.selectBehavior = OptionMenu(tk, self.selected_behaviour_option, *Student.possible_behaviour_grades)
        self.selectBehavior['width'] = 10
        self.selectBehavior.grid(column=1, row=row)

        # labelAverage
        self.labelAverage = Label()
        self.labelAverage['text'] = "Średnia:"
        self.labelAverage.grid(row=0, column=2)

        # labelAverageDisplay
        self.labelAverageDisplay = Label(tk)
        self.labelAverageDisplay.grid(row=0, column=3)

    def CountAverage(self):
        student = Student("Jan", "Kowalski")
        grades = {}
        for i in range(0,len(self.selectsStudentGrades)):
            grade = int(self.selectsStudentGrades[i].get())
            subject = get_subjects_names()[i]
            grades[subject] = grade
        student.assign_grades(grades)
        average = student.get_student_average()
        self.labelAverageDisplay['text'] = average
        student.assign_behaviour_grade(self.selected_behaviour_option.get())
        if student.is_student_honored():
            info = "Uczeń otrzyma świadectwo z wyróżnieniem"
        else:
            info = "Uczeń nie otrzyma świadectwa z wyróżnieniem"
        messagebox.showinfo('Informacja', info)
