
def create_report(data_file_name: str ,report_file_name: str) -> None:
    with open(data_file_name, "r") as file:
        lines = file.readlines()
        supply_total = 0
        buy_total = 0
        for line in lines:
            line = line.strip().split(",")
            print(line[0])
            if line[0] == "supply":
                supply_total += int(line[1])
            elif line[0] == "buy":
                buy_total += int(line[1])
        result = supply_total - buy_total

    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply_total}\n")
        report.write(f"buy,{buy_total}\n")
        report.write(f"result,{result}\n")
