def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    report_data = {
        "supply": 0,
        "buy": 0
    }
    with open(
            data_file_name, "r"
    ) as file:
        with open(
                report_file_name, "w"
        ) as report_file:
            for line in file:
                if line:
                    if line.split(",")[0] in report_data:
                        report_data[line.split(",")[0]] \
                            += int(line.split(",")[1])
                    else:
                        report_data[line.split(",")[0]] \
                            = int(line.split(",")[1])
            for element in report_data:
                report_file.write(f"{element},{report_data[element]}\n")
            report_file.write(
                f"result,"
                f"{report_data.get('supply') - report_data.get('buy')}\n"
            )
