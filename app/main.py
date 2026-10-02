def create_report(data_f_name: str, report_f_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_f_name, "r") as f_in, open(report_f_name, "w") as f_out:
        for line in f_in:
            if line != "\n":
                list_line = line.split(",")
                if list_line[0] == "buy":
                    buy += int(list_line[1])
                elif list_line[0] == "supply":
                    supply += int(list_line[1])
        result = supply - buy
        f_out.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
