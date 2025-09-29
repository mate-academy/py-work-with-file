def create_report(data_file_name: str, report_file_name: str) -> None:
    new_dict = {}

    data_file = open(data_file_name, "r")
    lines = data_file.readlines()

    for line in lines:
        line = line.strip()
        if not line:
            continue

        elements = line.split(",")
        if elements[0] in new_dict:
            new_dict[elements[0]] += int(elements[1])
        else:
            new_dict[elements[0]] = int(elements[1])
    data_file.close()

    new_dict["result"] = new_dict.get("supply", 0) - new_dict.get("buy", 0)

    report = open(report_file_name, "w")
    report.write(f"supply,{new_dict.get("supply", 0)}\n")
    report.write(f"buy,{new_dict.get("buy", 0)}\n")
    report.write(f"result,{new_dict["result"]}\n")
    report.close()
