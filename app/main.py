def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with (
        open(data_file_name, "r") as first,
        open(report_file_name, "w") as second
    ):
        for line in first.readlines():
            line_split = line.split(",")
            if "supply" in line_split:
                supply += int(line_split[1])
            elif "buy" in line_split:
                buy += int(line_split[1])
        second.write(f"supply,{supply}\n")
        second.write(f"buy,{buy}\n")
        second.write(f"result,{supply - buy}\n")
