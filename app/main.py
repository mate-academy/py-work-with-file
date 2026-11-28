def create_report(
    data_file_name:str,
    report_file_name:str
) -> None:

    with open(data_file_name, "rt") as file_object:
        contents = file_object.readlines()

    supply = 0
    buy = 0

    for line in contents:
        operation, amount = line.rstrip().split(",")
        if operation == "supply":
            supply += int(amount)
        elif operation == "buy":
            buy += int(amount)
    result = supply - buy

    new_report = (
        f"supply,{supply}\n"
        f"buy,{buy}\n"
        f"result,{result}\n"
    )
    with open(report_file_name, "a") as file_object:
        file_object.write(new_report)
