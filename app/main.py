def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as data_file,
        open(report_file_name, "w") as report_file
    ):
        report_dict = {}
        for line in data_file:
            line = line.strip()
            if not line:
                continue
            key, value = line.split(",")
            if key not in report_dict:
                report_dict[key] = int(value)
            else:
                report_dict[key] += int(value)
        report_dict["result"] = (
            report_dict.get("supply") - report_dict.get("buy")
        )

        report_file.write(f'supply,{report_dict["supply"]}\n')
        report_file.write(f'buy,{report_dict["buy"]}\n')
        report_file.write(f'result,{report_dict["result"]}\n')
