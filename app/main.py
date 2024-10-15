def create_report(data_file_name: str, report_file_name: str) -> str:
    with open(data_file_name, "r") as read_file:
        supply = 0
        buy = 0

        for line in read_file:
            if not line.strip():
                continue
            list_ = line.strip().split(",")
            amount = int(list_[1])
            if list_[0] == "supply":
                supply += amount
            if list_[0] == "buy":
                buy += amount

        result = supply - buy

    with open(report_file_name, "w") as write_file:
        write_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
