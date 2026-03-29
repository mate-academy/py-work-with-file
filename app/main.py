def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file:
        lines = file.readlines()

    supply = sum(
        int(line.split(",")[1]) for line in lines if line.startswith("supply")
    )
    buy = sum(
        int(line.split(",")[1]) for line in lines if line.startswith("buy")
    )
    result = supply - buy

    report_content = (
        f"supply,{supply}\n"
        f"buy,{buy}\n"
        f"result,{result}\n"
    )

    with open(report_file_name, "w") as file:
        file.write(report_content)
