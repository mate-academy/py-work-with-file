def create_report(data_file_name: str, report_file_name: str) -> None:
    vul_supply = 0
    vul_buy = 0
    with open(data_file_name, "r") as file:
        for line in file:
            amount = line.split(",")[1].replace("\n", "")
            if "supply" in line:
                vul_supply += int(amount)
            if "buy" in line:
                vul_buy += int(amount)
    with open(report_file_name, "w") as file_report:
        file_report.write(f"supply,{vul_supply}\n"
                          f"buy,{vul_buy}\n"
                          f"result,{vul_supply - vul_buy}\n")
