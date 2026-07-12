def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as d:
        lines = d.readlines()
        for line in lines:
            num = line.split(",")
            if "supply" in num:
                supply += int(num[1])
            elif "buy" in num:
                buy += int(num[1])

    result = supply - buy

    with open(report_file_name, "w") as r:
        r.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
