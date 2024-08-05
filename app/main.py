def create_report(data_file_name: str, report_file_name: str) -> None:
    file_opener = open(data_file_name, "r")
    sum_supply = 0
    sum_buy = 0
    for line in file_opener:
        parts = line.strip().split(",")
        category, amount_str = parts
        amount = int(amount_str)

        if category == "supply":
            sum_supply += amount
        elif category == "buy":
            sum_buy += amount

    file_opener.close()
    result_num = sum_supply - sum_buy
    result = f"supply, {sum_supply}\nbuy, {sum_buy}\nresult, {result_num}\n"

    report_file = open(report_file_name, "w")
    report_file.write(result)
    report_file.close()
