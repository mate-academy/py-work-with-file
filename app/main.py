def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    with (
        open(data_file_name, "r") as data_file,
        open(report_file_name, "a") as report_file
    ):
        supply = 0
        buy = 0

        for line in data_file.readlines():
            if len(line) != 0:
                operation, amount = line.split(",")

                if operation == "supply":
                    supply += int(amount)
                elif operation == "buy":
                    buy += int(amount)

        result = supply - buy

        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{result}\n")
