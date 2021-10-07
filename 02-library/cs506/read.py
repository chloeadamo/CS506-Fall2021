from csv import reader

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = reader(csv_file)
        rowlist = list(csv_reader)
        return rowlist 
