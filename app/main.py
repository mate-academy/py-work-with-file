def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            line = line.strip()
            if not line:
                continue

            key, value = line.split(",")

            if key == "supply":
                supply += int(value)
            elif key == "buy":
                buy += int(value)

    report = f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n"
    with open(report_file_name, "a") as report_file:
        report_file.write(report)
