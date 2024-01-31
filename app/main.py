import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        csv_reader = csv.reader(data_file)

        supply = 0
        buy = 0

        for line in csv_reader:
            if line[0] == "supply":
                supply += int(line[1])
            if line[0] == "buy":
                buy += int(line[1])

        result = supply - buy

        with open(report_file_name, "w") as report_file:
            report_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
