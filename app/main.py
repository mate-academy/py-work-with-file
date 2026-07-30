def create_report(data_file_name: str, report_file_name: str) -> None:
    amount_of_supplies = 0
    amount_to_buy = 0
    with (open(data_file_name, "r") as file,
          open(report_file_name, "w") as report):
        for line in file:
            amount = line.split(",")[1].replace("\n", "")
            if "supply" in line:
                amount_of_supplies += int(amount)
            if "buy" in line:
                amount_to_buy += int(amount)
        report.write(f"supply,{amount_of_supplies}\n"
                     f"buy,{amount_to_buy}\n"
                     f"result,{amount_of_supplies - amount_to_buy}\n")
