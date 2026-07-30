def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as read_file:
        new_f = read_file.readlines()
        sp_file = []
        for text in new_f:
            sp_file.append(text.strip().split(","))
        for sp in sp_file:
            if not sp:
                continue
            if "supply" in sp:
                supply += int(sp[1])
            if "buy" in sp:
                buy += int(sp[1])
    result = supply - buy

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
