def create_report(data_file_name: str, report_file_name: str) -> str:
    supply = 0
    buy = 0
    data_file = open(data_file_name, "r")
    result_file = open(report_file_name, "w")

    for row in data_file:
        values = row.strip().split(",")
        if values[0] == "supply":
            value = int(values[1])
            supply += value
        elif values[0] == "buy":
            value = int(values[1])
            buy += value
        result = supply - buy

    result_file.write(f"supply,{str(supply)}\n")
    result_file.write(f"buy,{str(buy)}\n")
    result_file.write(f"result,{str(result)}\n")

    data_file.close()
    result_file.close()
