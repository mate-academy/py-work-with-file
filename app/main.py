def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_sum = 0
    buy_sum = 0
    with open(data_file_name, "r") as file:
        for line in file.readlines():
            parts = line.split(",")
            if parts[0]:
                if parts[0] == "buy":
                    buy_sum += int(parts[1].strip())
                else:
                    supply_sum += int(parts[1].strip())
    with open(report_file_name, "w") as rep_file:
        rep_file.write(f"supply,{supply_sum}\n")
        rep_file.write(f"buy,{buy_sum}\n")
        rep_file.write(f"result,{supply_sum - buy_sum}\n")
