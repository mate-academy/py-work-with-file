def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file:
        total_supply = 0
        total_buy = 0

        for line in file:
            line = line.strip()
            if not line:  # pula linha vazia
                continue
            if line.split(",")[0] == "supply":
                total_supply += int(line.split(",")[1])
            if line.split(",")[0] == "buy":
                total_buy += int(line.split(",")[1])

    with open(report_file_name, "w") as report:
        report.write(f"supply,{total_supply}\n")
        report.write(f"buy,{total_buy}\n")
        report.write(f"result,{total_supply - total_buy}\n")
