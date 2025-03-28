def create_report(data_file_name: str, report_file_name: str) -> None:
    total_buy = 0
    total_supply = 0
    with open(data_file_name, "r") as f:

        for line in f.readlines():
            action, count = line.strip().split(",")
            if line:
                if action == "buy":
                    total_buy += int(count)
                elif action == "supply":
                    total_supply += int(count)

    result = total_supply - total_buy

    with open(report_file_name, mode="w") as report_file:
        report_file.write(f"supply,{total_supply}\n")
        report_file.write(f"buy,{total_buy}\n")
        report_file.write(f"result,{result}\n")
