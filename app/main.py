def create_report(data_file_name: str, report_file_name: str) -> None:
    file1 = open(data_file_name, "r")
    supply = 0
    buy = 0
    for line in file1.readlines():
        lis = line.split(",")
        if "supply" in lis:
            supply += int(lis[1])
        if "buy" in lis:
            buy += int(lis[1])
    result = supply - buy
    file2 = open(report_file_name, "a")
    file2.write(f"supply,{supply}\n")
    file2.write(f"buy,{buy}\n")
    file2.write(f"result,{result}\n")

    file1.close()
    file2.close()
