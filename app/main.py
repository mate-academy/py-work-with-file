def create_report(data_file_name: str, report_file_name: str) -> None:
    """Create a report from the data file and save it to the report file.

    Args:
        data_file_name (str): The name of the data file to read from.
        report_file_name (str): The name of the report file to write to.
    """

    data_file = open(data_file_name, "r")
    data: list[str] = data_file.readlines()
    data_file.close()

    report_lines: dict[str, int] = {
        "supply": 0,
        "buy": 0,
        "result": 0,
    }

    for line in data:
        if line.strip() == "":
            continue
        key_value = line.split(",")[0]
        report_lines[key_value] += int(line.split(",")[1])

    report_lines["result"] = (
        report_lines.get("supply", 0)
        - report_lines.get("buy", 0)
    )

    report_file = open(report_file_name, "w")
    for key, value in report_lines.items():
        report_file.write(f"{key},{value}\n")
    report_file.close()
