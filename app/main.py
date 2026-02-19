def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file:
        for line in file:

            line = line.strip()
            line_list = line.split(",")

            if line_list[0] == "supply":
                supply += int(line_list[1])

            if line_list[0] == "buy":
                buy += int(line_list[1])

    with open(report_file_name, "a") as file:
        file.write(f"supply,{supply}\n")
        file.write(f"buy,{buy}\n")
        result = supply - buy
        file.write(f"result,{result}\n")
