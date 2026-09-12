
def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    line = ""
    with open(data_file_name, "r") as f:
        for row in f:
            line = str(row)
            if "supply" in line:
                supply += int(line[7:])
            if "buy" in line:
                buy += int(line[4:])

    result = supply - buy

    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}\n")
        f.write(f"buy,{buy}\n")
        f.write(f"result,{result}\n")
