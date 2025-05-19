def create_report(data_file_name: str, report_file_name: str) -> None:
    file_input = open(data_file_name, "r")
    file_output = open(report_file_name, "a")
    supply, buy = 0, 0
    for line in file_input:
        if line.split(",")[0] == "supply":
            supply += int(line.strip("\n").split(",")[1])
        if line.split(",")[0] == "buy":
            buy += int(line.strip("\n").split(",")[1])
    result = supply - buy
    file_output.write(f"supply,{supply}\n")
    file_output.write(f"buy,{buy}\n")
    file_output.write(f"result,{result}\n")
    file_input.close()
    file_output.close()
