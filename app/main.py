def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file_in:
        for line in file_in:
            name, values = line.split(",")
            if name == "supply":
                supply += int(values)
            if name == "buy":
                buy += int(values)
        result = supply - buy

    with open(report_file_name, "w") as file_out:
        file_out.write(
            f"supply,{supply}\n"
            f"buy,{buy}\n"
            f"result,{result}\n"
        )
