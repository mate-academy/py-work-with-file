def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file:
        content = file.readlines()

    report_content = {"supply": 0, "buy": 0}

    for line in content:
        if not line.strip():
            continue

        action, price = line.strip().split(",")

        if action in report_content:
            report_content[action] += int(price)

    result = report_content["supply"] - report_content["buy"]
    report_template = (
        f"supply,{report_content['supply']}\n"
        f"buy,{report_content['buy']}\n"
        f"result,{result}\n"
    )

    with open(report_file_name, "w") as file:
        file.write(report_template)
