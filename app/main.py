def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = {}
    data_f = open(f"{data_file_name}", "r")
    report_f = open(f"{report_file_name}", "w")
    for line in data_f.readlines():
        if not line.strip():
            continue
        else:
            parts = line.strip().split(",")
            op = parts[0]
            amount = int(parts[1])
            if op in report_dict:
                report_dict[op] += amount
            else:
                report_dict[op] = amount
    supply = report_dict.get("supply", 0)
    buy = report_dict.get("buy", 0)
    result = supply - buy
    report_f.write(f"supply,{supply}\n")
    report_f.write(f"buy,{buy}\n")
    report_f.write(f"result,{result}\n")
    data_f.close()
    report_f.close()
