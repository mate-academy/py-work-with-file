def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file_out:
        buy = 0
        supply = 0
        for line in file_out:
            action, amount = line.split(",")
            if action == "buy":
                buy += int(amount)
            if action == "supply":
                supply += int(amount)
        result = supply - buy
    with open(report_file_name, "w") as file_in:
        file_in.write(f"supply, {supply}\n")
        file_in.write(f"buy, {buy}\n")
        file_in.write(f"result, {result}\n")
