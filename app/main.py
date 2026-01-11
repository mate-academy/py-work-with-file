def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
            open(data_file_name) as data_file,
            open(report_file_name, "w") as report_file
    ):
        data = dict()
        for line in data_file.readlines():
            key, value = line.replace("\n", "").split(",")
            if data.get(key) is not None:
                data[key] = data.get(key) + int(value)
            else:
                data[key] = int(value)

        report_file.write(f'supply,{data.get("supply")}\n')
        report_file.write(f'buy,{data.get("buy")}\n')
        result_line = data.get("supply") - data.get("buy")
        report_file.write(f"result,{result_line}\n")
