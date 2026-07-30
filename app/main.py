def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file:
        reader = file.readlines()
        result = {}
        for row in reader:
            if not row.strip():
                continue
            operation, amount = row.strip().split(",")
            if operation not in result:
                result[operation] = int(amount)
            else:
                result[operation] += int(amount)
        result["result"] = result["supply"] - result["buy"]

    with open(report_file_name, "w") as f:
        f.write(f'supply,{result["supply"]}\n')
        f.write(f'buy,{result["buy"]}\n')
        f.write(f'result,{result["result"]}\n')
