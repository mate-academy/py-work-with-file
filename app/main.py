def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as f:
        lines = f.readlines()

    supply = 0
    buy = 0
    for line in lines:
        operation_type, amount = line.split(",")
        if operation_type == "supply":
            supply += int(amount)
        else:
            buy += int(amount)

    result = supply - buy

    with open(report_file_name, "w") as f:
        f.writelines(
            [f"supply,{supply}\n", f"buy,{buy}\n", f"result,{result}\n"])
