def create_report(data_file_name: str, report_file_name: str) -> None:
    file_name = open(data_file_name, "r")
    supply = 0
    buy = 0
    for line_file in file_name:
        word = line_file.split(",")
        if word[0] == "supply":
            supply += int(word[1])
        else:
            buy += int(word[1])

    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}")
