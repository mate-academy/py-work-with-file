import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as file:
        fil = csv.reader(file)
        for line in fil:
            str(line).split(",")
            result[line[0]] += int(line[1])
    res = str(result.get("supply") - result.get("buy"))

    with open(report_file_name, "a") as new_file:
        new_file.write("supply," + str(result.get("supply")) + "\n")
        new_file.write("buy," + str(result.get("buy")) + "\n")
        new_file.write("result," + res + "\n")
