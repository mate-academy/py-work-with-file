def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        supply = 0
        buy = 0
        for line in data_file:
            if line.strip() != "":
                ls_split = line.strip().split(",")
                if ls_split[0] == "supply":
                    supply += int(ls_split[1])
                if ls_split[0] == "buy":
                    buy += int(ls_split[1])
        result = supply - buy
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
