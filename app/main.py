def create_report(data_file_name: str, report_file_name: str) -> None:
    counted_data = {
        "result": 0,
    }

    with open(data_file_name, "r") as data_file:
        for line in data_file.readlines():
            if not line.strip():
                continue
            operation, amount = line.split(",")
            if operation not in counted_data:
                counted_data[operation] = int(amount)
            else:
                counted_data[operation] += int(amount)

    counted_data["result"] = counted_data["supply"] - counted_data["buy"]

    with open(report_file_name, "w") as new_report:
        sup = counted_data["supply"]
        buy = counted_data["buy"]
        result = counted_data["result"]
        new_report.write(
            f"supply,{sup}\nbuy,{buy}\nresult,{result}\n"
        )
