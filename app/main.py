def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as first_f:
        first_all_file = first_f.readlines()

        for line in first_all_file:
            sup_or_buy, amount = line.split(",")
            if sup_or_buy == "supply":
                supply += int(amount)
            if sup_or_buy == "buy":
                buy += int(amount)
        result = supply - buy

    with open(report_file_name, "w") as second_f:
        second_f.write(f"supply, {supply}\n")
        second_f.write(f"buy, {buy}\n")
        second_f.write(f"result, {result}\n")
