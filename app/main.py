def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    sum_supply = 0
    sum_buy = 0
    for line in data_file:
        if line.strip() != "":
            row = line.strip().split(",")
            if row[0] == "supply":
                sum_supply += int(row[1])
            elif row[0] == "buy":
                sum_buy += int(row[1])
    data_file.close()
    report_file = open(report_file_name, "w")
    report_file.write(f"supply,{sum_supply}\n")
    report_file.write(f"buy,{sum_buy}\n")
    report_file.write(f"result,{sum_supply - sum_buy}\n")
    report_file.close()
