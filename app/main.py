def create_report(data_file_name: str, report_file_name: str) -> None:
    input_file = open(data_file_name, "r")
    supply, buy = 0, 0
    for line in input_file.readlines():
        if "supply" in line:
            supply += int(line.rsplit(",")[1])
        elif "buy" in line:
            buy += int(line.rsplit(",")[1])
        elif not line.strip():
            print("Empty line")
    input_file.close()
    output_file = open(report_file_name, "a")
    output_file.write(f"supply,{supply}\n")
    output_file.write(f"buy,{buy}\n")
    result = supply - buy
    output_file.write(f"result,{result}\n")
    input_file.close()
    output_file.close()
