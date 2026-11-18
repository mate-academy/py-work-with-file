import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file:
        reader = csv.reader(file)

        for line in reader:
            if line:
                row1 = line[0]
                row2 = int(line[1])

                if row1 == "supply":
                    supply += row2
                elif row1 == "buy":
                    buy += row2

        result = supply - buy

    with open(report_file_name, "w") as file:
        writer = csv.writer(file)
        writer.writerow(["supply", supply])
        writer.writerow(["buy", buy])
        writer.writerow(["result", result])
