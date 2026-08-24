def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as read_file:
        supply = 0
        buy = 0

        for line in read_file:
            if "supply" in line:
                supply += int(line.split(",")[1])
            elif "buy" in line:
                buy += int(line.split(",")[1])

        result = supply - buy

    with open(report_file_name, "w") as write_file:
        write_file.write(f"supply,{supply}\n")
        write_file.write(f"buy,{buy}\n")
        write_file.write(f"result,{result}\n")
