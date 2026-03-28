import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    # Reading info from CSV file and calculating result
    with open(data_file_name, "r") as file:
        csv_file = csv.reader(file)
        supply = 0
        buy = 0

        for line in csv_file:
            if line[0] == "supply":
                supply += int(line[1])
            else:
                buy += int(line[1])

        result = supply - buy

    # Write calculated data to new file
    with open(report_file_name, "w", newline="") as out_file:
        writer = csv.writer(out_file)
        writer.writerow(["supply", supply])
        writer.writerow(["buy", buy])
        writer.writerow(["result", result])
