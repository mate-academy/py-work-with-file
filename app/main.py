import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open("./" + data_file_name, "r") as data, \
            open(report_file_name, "w") as report:
        supply = 0
        buy = 0
        reader = csv.reader(data)
        for line in reader:
            # data_mas = line.split(",")
            if line[0] == "supply":
                supply += int(line[1])
            if line[0] == "buy":
                buy += int(line[1])
        content = f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n"
        report.write(content)
