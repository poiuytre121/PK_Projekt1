from tkinter import *
from tkinter import messagebox
from config.config import *
from classes.student import *
from classes.dataexport import *


class MainWindow(object):

    current_student = None

    def __init__(self, tk):
        """
        Initializes new instance of Window class

        :param Tk tk:
        """
        # btnCountAverage
        self.btnCountAverage = Button()
        self.btnCountAverage['text'] = "Policz średnią"
        self.btnCountAverage['width'] = 20
        self.btnCountAverage['command'] = self.count_average
        self.btnCountAverage.grid(column=2, columnspan=2, row=3)

        # btnSaveReport
        self.btnSaveReport = Button()
        self.btnSaveReport['text'] = "Zapisz ucznia do pliku csv"
        self.btnSaveReport['width'] = 20
        self.btnSaveReport['command'] = self.save_report
        self.btnSaveReport.grid(column=2, columnspan=2, row=4)

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

        # first name input
        self.labelFirstName = Label()
        self.labelFirstName['text'] = "Imię"
        self.labelFirstName.grid(column=2, row=0)
        self.inputFirstName = Text()
        self.inputFirstName['height'] = 1
        self.inputFirstName['width'] = 20
        self.inputFirstName.grid(column=3, row=0)

        # last name input
        self.labelLastName = Label()
        self.labelLastName['text'] = "Nazwisko"
        self.labelLastName.grid(column=2, row=1)
        self.inputLastName = Text()
        self.inputLastName['height'] = 1
        self.inputLastName['width'] = 20
        self.inputLastName.grid(column=3, row=1)

        # labelAverage
        self.labelAverage = Label()
        self.labelAverage['text'] = "Średnia:"
        self.labelAverage.grid(row=2, column=2)

        # labelAverageDisplay
        self.labelAverageDisplay = Label(tk)
        self.labelAverageDisplay.grid(row=2, column=3)

    def count_average(self):
        student = Student(self.inputFirstName.get("1.0",END), self.inputLastName.get("1.0",END))
        grades = {}
        for i in range(0,len(self.selectsStudentGrades)):
            grade = int(self.selectsStudentGrades[i].get())
            subject = get_subjects_names()[i]
            grades[subject] = grade
        student.assign_grades(grades)
        average = student.get_student_average()
        self.labelAverageDisplay['text'] = average
        student.assign_behaviour_grade(self.selected_behaviour_option.get())
        self.current_student = student
        if student.is_student_honored():
            info = "Uczeń otrzyma świadectwo z wyróżnieniem"
        else:
            info = "Uczeń nie otrzyma świadectwa z wyróżnieniem"
        messagebox.showinfo('Informacja', info)

    def save_report(self):
        if self.current_student is None:
            messagebox.showinfo('Błąd', 'Średnia dla ucznia nie została policzona. Kliknij "Policz Średnią".')
        else:
            DataExport.export_student_to_csv('uczniowie.csv', self.current_student)
            messagebox.showinfo('OK', 'Zapisano do pliku uczniowie.csv')

