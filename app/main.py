def create_report(data_file_name: str, report_file_name: str) -> str:
    report_dict: dict[str, int] = {}

    with open(data_file_name) as data_file:
        for line in data_file:
            if not line.strip():
                continue

            key, value = line.strip().split(",")
            report_dict[key] = report_dict.get(key, 0) + int(value)

    supply = report_dict.get("supply", 0)
    buy = report_dict.get("buy", 0)
    report_dict["result"] = supply - buy

    order = ["supply", "buy", "result"]

    with open(report_file_name, "w") as report_file:
        for key in order:
            report_file.write(f"{key},{report_dict.get(key, 0)}\n")

    return report_file_name
