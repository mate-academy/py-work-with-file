def create_report(data_file_name: str, report_file_name: str) -> None:
    data = {}

    with (
        open(data_file_name, "r") as data_file,
        open(report_file_name, "w") as report_file
    ):
        content = data_file.readlines()

        for line in content:
            if line.strip():
                operation, amount = line.strip().split(",")
                if operation in data:
                    data[operation] += int(amount)
                else:
                    data[operation] = int(amount)

        supply_total = data.get("supply", 0)
        buy_total = data.get("buy", 0)
        result = supply_total - buy_total
        report_file.write(f"supply,{supply_total}\n")
        report_file.write(f"buy,{buy_total}\n")
        report_file.write(f"result,{result}\n")
