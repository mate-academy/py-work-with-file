def create_report(data_file_name: str, report_file_name: str) -> None:

    with open(data_file_name) as file:
        supply = 0
        buy = 0

        for line in file:
            if not line.strip():
                continue
            word = line.split(",")
            if word[0] == "supply":
                supply += int(word[1])
            elif word[0] == "buy":
                buy += int(word[1])
        result = supply - buy
        with open(report_file_name, "w") as report_file:
            report_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
