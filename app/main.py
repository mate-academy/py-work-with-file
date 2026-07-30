def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as f_in:
        for line in f_in:
            sep_line = line.split(",")
            if sep_line[0] == "supply":
                supply += int(sep_line[1])
            if sep_line[0] == "buy":
                buy += int(sep_line[1])
    result = supply - buy
    report = f"supply,{supply}\n" \
             f"buy,{buy}\n" \
             f"result,{result}\n"
    with open(report_file_name, "w") as f_out:
        f_out.write(report)
