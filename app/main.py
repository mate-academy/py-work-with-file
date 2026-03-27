import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0] == "supply":
                supply += int(row[1])
            else:
                buy += int(row[1])

    with open(report_file_name, "a") as file:
        file.write("supply," + str(supply) + "\n")
        file.write("buy," + str(buy) + "\n")
        file.write("result," + str(supply - buy) + "\n")
