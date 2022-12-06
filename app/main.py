def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(f"{data_file_name}", "r") as file:
        supply_sum = 0
        buy_sum = 0

        for line in file:
            line = line.split(",")
            print(line)
            if line[0] == "supply":
                supply_sum += int(line[1])
            if line[0] == "buy":
                buy_sum += int(line[1])

        result_sum = supply_sum - buy_sum

    with open(f"{report_file_name}", "a") as report:
        report.write(f"supply,{supply_sum}\n")
        report.write(f"buy,{buy_sum}\n")
        report.write(f"result,{result_sum}\n")

