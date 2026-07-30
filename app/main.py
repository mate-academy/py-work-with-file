def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file1:
        file_content = file1.readlines()
    supply = 0
    buy = 0
    for line in file_content:
        ele = line.split(",")
        if ele[0] == "buy":
            buy += int(ele[1])
        elif ele[0] == "supply":
            supply += int(ele[1])
    result = supply - buy

    with open(report_file_name, "w") as file2:
        file2.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
