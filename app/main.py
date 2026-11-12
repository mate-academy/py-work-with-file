def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    report_file = open(report_file_name, "w")
    supply_count = 0
    buy_count = 0
    for line in data_file.readlines():
        if len(line) == 0:
            continue
        comes_before_comma = line[:line.index(",")]
        comes_after_comma = int(line[line.index(",") + 1:])
        if comes_before_comma == "supply":
            supply_count += comes_after_comma
        if comes_before_comma == "buy":
            buy_count += comes_after_comma
    report_file.write(f"supply,{supply_count}\n
    buy,{buy_count}\nresult,{supply_count - buy_count}")
    data_file.close()
    report_file.close()
