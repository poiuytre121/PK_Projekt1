def get_subjects_names():
    """
    returns an array with subject list names
    :return:
    """
    try:
        file_handler = open('config/subjects.csv', 'r')
        return [i for i in file_handler]
    except IOError:
        raise FileNotFoundError("Błąd odczytu pliku przedmiotów. Sprawdź czy w folderze config znajduje się plik subjects.csv")
