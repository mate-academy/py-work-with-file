def create_report(data_file_name: str, report_file_name: str) -> None:
    input_file = open(data_file_name, "r")
    supply, buy = 0, 0
    for file_line in input_file:
        if "supply" in file_line:
            supply += int(file_line.split(",")[1])
        if "buy" in file_line:
            buy += int(file_line.split(",")[1])
    input_file.close()
    with open(report_file_name, "a") as res_file:
        res_file.write(",".join(["supply", str(supply)]) + "\n")
        res_file.write(",".join(["buy", str(buy)]) + "\n")
        res_file.write(",".join(["result", str(supply - buy)]) + "\n")
