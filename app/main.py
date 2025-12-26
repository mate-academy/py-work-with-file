def create_report(data_file_name: str, report_file_name: str) -> None:
    sum_supply = 0
    sum_buy = 0

    file_read = open(data_file_name, "r")
    lines = file_read.readlines()

    for line in lines:

        operation, amount = line.split(",")
        amount = int(amount)

        if operation == "supply":
            sum_supply += amount
        else:
            sum_buy += amount

    result = sum_supply - sum_buy

    result_lines = [
        f"supply,{sum_supply}\n",
        f"buy,{sum_buy}\n",
        f"result,{result}\n"
    ]
    file_write = open(report_file_name, "w")
    file_write.writelines(result_lines)
