def create_report(data_file_name: str, report_file_name: str) -> None:

    with open(data_file_name, "r") as file:

        supply = 0
        buy = 0

        for line in file:
            current_line = line.split(",")
            if current_line[0] == "supply":
                supply += int(current_line[1])
            if current_line[0] == "buy":
                buy += int(current_line[1])

        result = supply - buy

        with open(report_file_name, "a") as file2:
            file2.write(f"supply,{supply}\n")
            file2.write(f"buy,{buy}\n")
            file2.write(f"result,{result}\n")
