def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as file:
        list_of_lines = file.readlines()
        for line in list_of_lines:
            line = line.replace("\n", "")
            line = line.split(",")
            if line[0] == "supply":
                supply += int(line[1])
            elif line[0] == "buy":
                buy += int(line[1])
    with open(report_file_name, "w") as file:
        file.write("supply,")
        file.write(f"{supply}\n")
        file.write("buy,")
        file.write(f"{buy}\n")
        file.write("result,")
        file.write(f"{supply - buy}\n")
