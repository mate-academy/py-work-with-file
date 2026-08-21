def create_report(data_file_name: str, report_file_name: str) -> None:
    report_data: dict[str, int] = {}

    with open(data_file_name) as data_file:
        for line in data_file:
            key, value = line.split(",")
            try:
                curr_value = report_data.get(key, 0)
                report_data[key] = int(value) + curr_value
            except ValueError:
                print(f"Could not convert {value} to int")

    supply = report_data.get("supply", 0)
    buy = report_data.get("buy", 0)
    result = supply - buy

    with open(report_file_name, "w") as report_file:
        report_file.writelines(
            [
                f"supply,{supply}\n",
                f"buy,{buy}\n",
                f"result,{result}\n",
            ]
        )
