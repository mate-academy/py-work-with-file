def create_report(data_file_name: str, report_file_name: str) -> None:
    total = {"supply": 0, "buy": 0}

    with open(data_file_name, mode="r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            operation, amount = line.split(",")
            amount = int(amount)
            if operation in total:
                total[operation] += amount

    result = total["supply"] - total["buy"]

    with open(report_file_name, mode="w") as file:
        for key, value in total.items():
            file.write(f"{key},{value}\n")
        file.write(f"result,{result}\n")
