def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    input_file = open(data_file_name, "r")
    for line in input_file:
        if line.strip():
            parts = line.strip().split(",")
            if parts[0] == "supply":
                supply += int(parts[1])
            if parts[0] == "buy":
                buy += int(parts[1])
    input_file.close()
    result = supply - buy

    output_file = open(report_file_name, "w")
    output_file.write("supply," + str(supply) + "\n")
    output_file.write("buy," + str(buy) + "\n")
    output_file.write("result," + str(result) + "\n")
    output_file.close()
