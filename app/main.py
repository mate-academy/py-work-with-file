def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as read,
        open(report_file_name, "w") as write
    ):
        dict_sum = {}
        for line in read:
            operation, amount = line.strip().split(",")
            amount = int(amount)
            if operation in dict_sum:
                dict_sum[operation] += amount
            else:
                dict_sum[operation] = amount

        result = dict_sum.get("supply", 0) - dict_sum.get("buy", 0)

        write.write(f"supply,{dict_sum.get('supply', 0)}\n")
        write.write(f"buy,{dict_sum.get("buy", 0)}\n")
        write.write(f"result,{result}\n")
