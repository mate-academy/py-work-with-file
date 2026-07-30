import csv


def create_report(
        data_file_name: str,
        new_file: str
) -> None:
    with open(data_file_name, "r") as csv_file:
        data = csv.reader(csv_file)
        supply = 0
        buy = 0
        for line in data:
            if line[0] == "buy":
                buy += int(line[1])
            else:
                supply += int(line[1])
        with open(new_file, "w") as new_file:
            csv_writer = csv.writer(new_file, delimiter=",")
            csv_writer.writerow(["supply", str(supply)])
            csv_writer.writerow(["buy", str(buy)])
            csv_writer.writerow(["result", str(supply - buy)])


create_report("bananas.csv", "new_file.csv")
