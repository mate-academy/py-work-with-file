import csv


def process_data(data_file_name: str, report_file_name: str) -> None:
    supply_count = 0
    buy_count = 0

    with open(data_file_name, newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 2:
                if row[0] == "supply":
                    supply_count += int(row[1])
                elif row[0] == "buy":
                    buy_count += int(row[1])

    result = supply_count - buy_count
    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply_count}\nbuy,{buy_count}\nresult,{result}")


process_data("input.csv", "report.txt")
