def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    f1 = open(data_file_name, "r")

    supply = 0
    buy = 0
    for line in f1:
        if "supply" in line:
            supply += int(line.split(",")[-1])
        elif "buy" in line:
            buy += int(line.split(",")[-1])
    f1.close()
    result = supply - buy

    f2 = open(report_file_name, "w")
    f2.write(f"supply,{supply}\n")
    f2.write(f"buy,{buy}\n")
    f2.write(f"result,{result}\n")
    f2.close()
