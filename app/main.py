def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data:
        text = data.readlines()
        sum_buy = 0
        sum_supply = 0
        for line in text:
            ls = line.split("\n")[0].split(",")
            if not ls[0]:
                continue
            if (ls[0] == "buy"):
                sum_buy += int(ls[1])
            if (ls[0] == "supply"):
                sum_supply += int(ls[1])
        with open(report_file_name, "w") as report:
            report.write(f"supply,{sum_supply}\n")
            report.write(f"buy,{sum_buy}\n")
            report.write(f"result,{sum_supply - sum_buy}\n")
