def create_report(data_file_name: str, report_file_name: str) -> None:
    input_file = open(data_file_name, "r")
    buy = 0
    supply = 0
    for line in input_file.readlines():
        current_list = line.split(",")
        if current_list[0] == "buy":
            buy += int(current_list[1])
        if current_list[0] == "supply":
            supply += int(current_list[1])

    input_file.close()

    result = supply - buy

    output_file = open(report_file_name, "a")
    output_file.write(f"supply, {supply}\n".replace(", ", ","))
    output_file.write(f"buy, {buy}\n".replace(", ", ","))
    output_file.write(f"result, {result}\n".replace(", ", ","))
    output_file.close()
