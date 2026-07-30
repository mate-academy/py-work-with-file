def create_report(data_file_name: str, report_file_name: str) -> None:
    data = open(data_file_name, "r")
    name = open(report_file_name, "w")
    info = data.readlines()
    supply = 0
    buy = 0
    for line in info:
        values = line.split(",")
        if "supply" == values[0]:
            supply += int(values[1])
        elif "buy" == values[0]:
            buy += int(values[1])
    result = supply - buy
    name.write(f"supply,{supply}\n")
    name.write(f"buy,{buy}\n")
    name.write(f"result,{result}\n")

    data.close()
    name.close()
