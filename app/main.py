def create_report(data_file_name: str, report_file_name: str) -> None:
    input = open(data_file_name, "r")
    supply, buy = 0, 0
    for line in input.readlines():
        if "supply" in line:
            supply += int(line.rsplit(",")[1])
        elif "buy" in line:
            buy += int(line.rsplit(",")[1])
        elif not line.strip():
            print("Empty line")
    input.close()
    output = open(report_file_name, "a")
    output.write(f"supply,{supply}\n")
    output.write(f"buy,{buy}\n")
    result = supply - buy
    output.write(f"result,{result}\n")
    input.close()
    output.close()
