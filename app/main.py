def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as read_file):
        result_dict = {}
        for line in read_file:
            operation, amount = line.strip().split(",")
            amount_as_int = int(amount)
            result_dict[operation] = (result_dict.get(operation, 0)
                                      + amount_as_int)

    with open(report_file_name, "w") as write_file:
        supply_sum = result_dict.get("supply", 0)
        buy_sum = result_dict.get("buy", 0)
        substraction = supply_sum - buy_sum

        write_file.write(f"supply,{str(supply_sum)}\n")
        write_file.write(f"buy,{str(buy_sum)}\n")
        write_file.write(f"result,{str(substraction)}\n")
