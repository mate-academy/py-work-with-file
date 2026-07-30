import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name) as data_file:
        reader = csv.reader(data_file)

        for row in reader:
            if row[0] == "supply":
                supply += int(row[1])

            elif row[0] == "buy":
                buy += int(row[1])

    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}"
                f"\nbuy,{buy}"
                f"\nresult,{supply - buy}\n")
