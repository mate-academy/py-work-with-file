def create_report(data_file_name: str, report_file_name: str) -> None:
    buy = 0
    supply = 0

    with open(data_file_name, "r") as file:
        for line in file:
            if line:
                listed = line.strip().split(",")
                if listed[0] == "supply":
                    supply += int(listed[1])
                elif listed[0] == "buy":
                    buy += int(listed[1])

    result = supply - buy

    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply}\n")
        file.write(f"buy,{buy}\n")
        file.write(f"result,{result}\n")
