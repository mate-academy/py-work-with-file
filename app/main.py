def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_amount = 0
    buy_amount = 0

    source_file = open(data_file_name)
    for line in source_file.readlines():
        if line == "\n":
            continue

        line_parts = line.split(",")
        if line_parts[0] == "supply":
            supply_amount += int(line_parts[1])
        elif line_parts[0] == "buy":
            buy_amount += int(line_parts[1])

    source_file.close()

    result_amount = supply_amount - buy_amount

    report = (
        f"supply,{supply_amount}\nbuy,{buy_amount}\nresult,{result_amount}\n"
    )

    written_file = open(report_file_name, "w")
    written_file.write(report)
    written_file.close()
