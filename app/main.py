def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file:
        lines = []

        for line in file.readlines():
            line = line.strip()
            if line:
                lines.append(line.split(","))

    sums = {}

    for item in lines:
        indicator = item[0]
        value = int(item[1])
        if indicator in sums:
            sums[indicator] += value
        else:
            sums[indicator] = value

    supply = sums.get("supply", 0)
    buy = sums.get("buy", 0)
    result = supply - buy

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{result}\n")
