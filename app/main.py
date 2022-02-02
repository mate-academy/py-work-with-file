def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as f:
        data = f.readlines()

    supply = sum(
        int(line.split(",")[1]) for line in data
        if line.split(",")[0] == "supply"
    )

    buy = sum(
        int(line.split(",")[1]) for line in data
        if line.split(",")[0] == "buy"
    )

    with open(report_file_name, "w") as f:
        f.write(
            f"supply,{supply}\n"
            f"buy,{buy}\n"
            f"result,{supply - buy}\n"
        )
