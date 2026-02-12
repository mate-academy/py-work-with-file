def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    file_input = open(data_file_name, "r")
    for line in file_input.readlines():
        if "supply" in line:
            supply += int(line.split(",")[1])
        else:
            buy += int(line.split(",")[1])
    file_input.close()
    file_output = open(report_file_name, "w")
    file_output.write(f"supply,{supply}\n")
    file_output.write(f"buy,{buy}\n")
    file_output.write(f"result,{supply - buy}\n")
    file_output.close()
