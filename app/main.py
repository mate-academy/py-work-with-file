def create_report(data_file_name: str, report_file_name: str) -> None:
    file1 = open(data_file_name)
    data = {"buy": [], "supply": []}

    for line in file1:
        if line.strip():
            operation, num = line.split(",")
            num = int(num)
            data[operation].append(num)

    file1.close()

    buy_sum = sum(data["buy"])
    supply_sum = sum(data["supply"])
    result = supply_sum - buy_sum

    summary_lines = (
        ",".join(["supply", str(supply_sum)]),
        ",".join(["buy", str(buy_sum)]),
        ",".join(["result", str(result)])
    )
    summary_text = "\n".join(summary_lines) + "\n"

    file_2 = open(report_file_name, "w")
    file_2.write(f"{summary_text}")
    file_2.close()
