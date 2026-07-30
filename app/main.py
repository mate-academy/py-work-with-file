def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file:
        for line in file:
            operations, value = line.split(",")
            if operations == "buy":
                buy += int(value)
            elif operations == "supply":
                supply += int(value)

            else:
                continue

        result = supply - buy

        with open(report_file_name, "w") as file:
            file.write(f"supply,{supply}\n")
            file.write(f"buy,{buy}\n")
            file.write(f"result,{result}\n")
