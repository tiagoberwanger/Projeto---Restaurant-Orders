import csv


def reading_csv(path_to_file):
    with open(path_to_file, "r") as file:
        return list(csv.reader(file))
# não funciona o import no src/analize_log.py
