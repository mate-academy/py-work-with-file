def create_report(data_file_name: str, report_file_name: str) -> None:

    file_data = open(data_file_name)

    supply = 0
    buy = 0

    for line in file_data:
        line = line.strip()
        if line == "":
            continue

        line_split = line.split(",")
        if line_split[0].strip() == "supply":
            supply += int(line_split[1].strip())
        elif line_split[0].strip() == "buy":
            buy += int(line_split[1].strip())

    result = supply - buy

    file_data.close()

    new_file = open(report_file_name, "w")

    new_file.write(f"supply,{supply}\n")
    new_file.write(f"buy,{buy}\n")
    new_file.write(f"result,{result}\n")

    new_file.close()
