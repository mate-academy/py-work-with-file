def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0
    data_file = open(data_file_name)
    lines = data_file.readlines()
    data_file.close()
    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split(",")
        operation_name = parts[0].strip()
        amount = int(parts[1].strip())
        if operation_name == "supply":
            total_supply += amount
        elif operation_name == "buy":
            total_buy += amount
    result = total_supply - total_buy
    report_content = (
        f"supply,{total_supply}\n"
        f"buy,{total_buy}\n"
        f"result,{result}\n"
    )
    report_file = open(report_file_name, "w")
    report_file.write(report_content)
    report_file.close()
