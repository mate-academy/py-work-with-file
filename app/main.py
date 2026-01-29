def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name) as file:
        data = file.readlines()
        for line in data:
            if line:
                key, value = line.split(",")
                if key == "supply":
                    supply += int(value)
                if key == "buy":
                    buy += int(value)
    with open(report_file_name, "w") as report_file_name:
        report_file_name.write("supply," + str(supply) + "\n")
        report_file_name.write("buy," + str(buy) + "\n")
        report_file_name.write("result," + str(supply - buy) + "\n")
