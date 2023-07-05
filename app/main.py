def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as data_f, \
            open(report_file_name, "w") as report_f:
        for line in data_f:
            words = line.split(",")

            if words[0] == "supply":
                supply += int(words[1])
            elif words[0] == "buy":
                buy += int(words[1])

        report_f.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
