from config.config import *


class Student(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.grades = {subject: 0 for subject in get_subjects_names()}
        self.behaviour_grade = self.possible_behaviour_grades[0]

    possible_grades = (1, 2, 3, 4, 5, 6)
    possible_behaviour_grades = ("naganne", "dopuszczające", "dostateczne", "dobre", "bardzo dobre", "wzorowe")

    def assign_grades(self, grade_dictionary):
        for key in grade_dictionary.keys():
            self.grades[key] = grade_dictionary[key]

    def assign_behaviour_grade(self, behaviour_grade):
        self.behaviour_grade = behaviour_grade

    def get_student_average(self):
        grade_sum = 0
        for grade in self.grades.values():
            grade_sum += grade
        return grade_sum / len(self.grades)

    def is_student_honored(self):
        average = self.get_student_average()
        behaviour_check = self.behaviour_grade == self.possible_behaviour_grades[4] or self.behaviour_grade == self.possible_behaviour_grades[5]
        return average >= 4.75 and behaviour_check
