def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as data_file:
        data = data_file.readlines()

    supply = sum(
        int(line.split(",")[1]) for line in data
        if line.split(",")[0] == "supply"
    )

    buy = sum(
        int(line.split(",")[1]) for line in data
        if line.split(",")[0] == "buy"
    )

    with open(report_file_name, "w") as report_file:
        report_file.write(
            f"supply,{supply}\n"
            f"buy,{buy}\n"
            f"result,{supply - buy}\n"
        )
