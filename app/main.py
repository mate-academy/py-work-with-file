def create_report(
    data_file_name: str,
    report_file_name: str,
) -> None:
    input_file = open(data_file_name, "r")
    supply = 0
    buy = 0
    for line in input_file.readlines():
        action, amount = line.split(",")[0], line.split(",")[1]
        if action == "supply":
            supply += int(amount)
        if action == "buy":
            buy += int(amount)
    input_file.close()
    output_file = open(report_file_name, "w")
    text = f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n"
    output_file.write(text)
    output_file.close()
