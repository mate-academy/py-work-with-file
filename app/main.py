def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name) as f:
        for line in f:
            clean_line = line.strip()
            if not clean_line:
                continue
            word = clean_line.split(",")
            if word[0] == "supply":
                supply += int(word[1])
            elif word[0] == "buy":
                buy += int(word[1])
    result = supply - buy
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{result}\n")
