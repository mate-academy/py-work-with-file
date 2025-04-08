def create_report(data_file_name: str, report_file_name: str) -> None:
    new_dict = {}
    with open(data_file_name) as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            key, value = line.split(",")
            key = key.strip()
            value = int(value.strip())
            new_dict[key] = new_dict.get(key, 0) + value

    supply = new_dict.get("supply", 0)
    buy = new_dict.get("buy", 0)
    result = supply - buy

    report_lines = []
    if "supply" in new_dict:
        report_lines.append(f"supply,{new_dict['supply']}")

    if "buy" in new_dict:
        report_lines.append(f"buy,{new_dict['buy']}")

    report_lines.append(f"result,{result}")

    with open(report_file_name, "w") as report_file:
        report_file.write("\n".join(report_lines) + "\n")
