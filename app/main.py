def create_report(data_file_name: str, report_file_name: str) -> None:
    file_open = open(data_file_name, "r")
    content = file_open.read()
    content_lines = content.split("\n")
    supply_total = 0
    buy_total = 0
    for item in content_lines:
        item = item.split(",")
        if item == [""] or item == []:
            continue
        if len(item) != 2:
            continue
        operator = item[0]
        amount = int(item[1])
        if operator == "supply":
            supply_total += amount
        elif operator == "buy":
            buy_total += amount
    result = supply_total - buy_total
    open_file = open(report_file_name, "w")
    open_file.write(f"supply,{supply_total}\n")
    open_file.write(f"buy,{buy_total}\n")
    open_file.write(f"result,{result}\n")
    open_file.close()
    file_open.close()
