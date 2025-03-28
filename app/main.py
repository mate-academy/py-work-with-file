def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file, \
         open(report_file_name, "w") as reports:
        supply_sum, buy_sum = 0, 0
        while True:
            line = file.readline().split(",")
            if line[0] == "supply":
                supply_sum += int(line[1])
            elif line[0] == "buy":
                buy_sum += int(line[1])
            else:
                break
        reports.write(f"supply,{supply_sum}\n"
                      f"buy,{buy_sum}\n"
                      f"result,{supply_sum - buy_sum}\n"
                      )
