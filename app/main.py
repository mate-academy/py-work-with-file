def create_report(data_file_name: int, report_file_name: int) -> None:

    supply = 0
    buy = 0
    data_file = open(f"{data_file_name}", "r")
    report_file = open(f"{report_file_name}", "w")

    for line in data_file:
        operation, amount = line.strip().split(",")
        if "supply" == operation:
            supply += int(amount)
        elif "buy" == operation:
            buy += int(amount)

    result = supply - buy

    report_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
