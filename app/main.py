def create_report(data_file_name: str, report_file_name: str) -> None:
    supply, buy = 0, 0

    with (
        open(data_file_name, "r") as data_file,
        open(report_file_name, "w") as result_file
    ):
        for line in data_file:
            data = line.split(",")
            if data[0] == "supply":
                supply += int(data[1])
            else:
                buy += int(data[1])

        result_file.write(
            f"supply,{supply}\n"
            f"buy,{buy}\n"
            f"result,{supply - buy}\n"
        )
