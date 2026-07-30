from csv import reader


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_count = 0
    buy_count = 0
    with open(data_file_name, "r") as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if row[0] == "supply":
                supply_count += int(row[1])
            if row[0] == "buy":
                buy_count += int(row[1])

    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply_count}\nbuy,"
                   f"{buy_count}\nresult,{supply_count - buy_count}\n")
