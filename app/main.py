def create_report(data_file_name: str, report_file_name: str) -> None:
    input_file = open(data_file_name, "r")
    supply = 0
    buy = 0
    for line in input_file.readlines():
        if line == "":
            continue
        text = line.split(",")
        if text[0] == "supply":
            supply += int(text[1])
        if text[0] == "buy":
            buy += int(text[1])
    input_file.close()
    output_file = open(report_file_name, "w")
    output_file.write(f"supply,{supply}\n")
    output_file.write(f"buy,{buy}\n")
    output_file.write(f"result,{supply - buy}\n")
    output_file.close()
