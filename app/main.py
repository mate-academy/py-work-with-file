def create_report(data_file_name: str, report_file_name: str) -> None:
    data = dict()

    with open(data_file_name, "r") as f:
        for line in f:
            name, value = line.split(",")

            if name not in data:
                data[name] = int(value)
            else:
                data[name] += int(value)

    result = data["supply"] - data["buy"]

    with open(report_file_name, "w") as f:
        f.write(f"supply,{data['supply']}\n"
                f"buy,{data['buy']}\n"
                f"result,{result}\n")
