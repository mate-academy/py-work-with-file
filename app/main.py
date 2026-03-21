def create_report(
        data_file_name: str,
        report_file_name: str,
):
    supply = 0
    buy = 0

    open_file = open(data_file_name, "r")

    for line in open_file:
        line = line.strip()
        if not line:
            continue

        parts = line.split(",")
        if len(parts) == 2:
            if parts[0] == "supply":
                supply += int(parts[1])
            elif parts[0] == "buy":
                buy += int(parts[1])
        else:
            continue

    open_file.close()

    result = supply - buy

    open_result = open(report_file_name, "w")
    open_result.write(f"supply,{supply}\n")
    open_result.write(f"buy,{buy}\n")
    open_result.write(f"result,{result}\n")

    open_result.close()
