def create_report(data_file_name: str, report_file_name: str) -> None:
    total = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as file:
        for line in file:
            clean_line = line.strip()
            if not clean_line:
                continue

            operation_type, amount = clean_line.split(",")
            total[operation_type] += int(amount)

    with open(report_file_name, "w") as file_w:
        file_w.write(f"supply,{total['supply']}\n")
        file_w.write(f"buy,{total['buy']}\n")
        result  = total["supply"] - total["buy"]
        file_w.write(f"result,{result}\n")
