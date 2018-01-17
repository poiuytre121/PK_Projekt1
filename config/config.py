def get_subjects_names():
    """
    returns an array with subject list names
    :return:
    """
    try:
        file_handler = open('config/subjects.csv', 'r')
        subjects = {}
        # removing duplicates
        for i in file_handler:
            subjects[i] = i
        return [i for i in subjects.values()]
    except IOError:
        raise FileNotFoundError("Błąd odczytu pliku przedmiotów. Sprawdź czy w folderze config znajduje się plik subjects.csv")
