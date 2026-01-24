import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as file:
        read_file = csv.reader(file)
        for line in read_file:
            if line[0] == "supply":
                supply += int(line[1])
            else:
                buy += int(line[1])

    with open(report_file_name, "a") as file:
        file.write("supply," + str(supply) + "\n")
        file.write("buy," + str(buy) + "\n")
        file.write("result," + str(supply - buy) + "\n")
