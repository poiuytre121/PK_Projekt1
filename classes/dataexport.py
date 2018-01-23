from classes.student import *
import os


class DataExport(object):

    @staticmethod
    def export_student_to_csv(path: str, student: Student):
        """
        Exports student grades to CSV
        :param path:str
        :param student:Student
        """
        file_exists = os.path.isfile(path)
        if file_exists:
            file = open(path, 'a')
            file_string = ''
            file_string += student.firstname.replace("\r", "").replace("\n", "") + ',' + student.lastname.replace("\r", "").replace("\n", "") + ','
            for grade in student.grades.values():
                file_string += str(grade) + ','
            file_string += student.behaviour_grade
            file_string += "\r\n"
            file.write(file_string)
            file.close()
        else:
            file_string = 'Imie,Nazwisko,'
            for subject in student.grades.keys():
                file_string += subject.replace("\r", "").replace("\n", "") + ','
            file_string += 'Zachowanie' + "\r\n"
            file_string += student.firstname.replace("\r", "").replace("\n", "") + ',' + student.lastname.replace("\r", "").replace("\n", "") + ','
            for grade in student.grades.values():
                file_string += str(grade) + ','
            file_string += student.behaviour_grade
            file_string += "\r\n"
            file = open(path, 'w')
            file.write(file_string)
            file.close()

