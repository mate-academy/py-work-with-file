
def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as data_file:
        content = data_file.read().split()

    for line in content:
        name, value = line.split(",")
        if name == "supply":
            supply += int(value)
        else:
            buy += int(value)

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{supply - buy}\n")
