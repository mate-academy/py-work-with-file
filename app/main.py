def create_report(data_file_name: str, report_file_name: str) -> None:
    file1 = (open(data_file_name, "r").read()
             .replace("\n", ",").split(","))
    buy = 0
    supply = 0
    for i in range(0, len(file1), 2):
        if file1[i] == "buy":
            buy += int(file1[i + 1])
        elif file1[i] == "supply":
            supply += int(file1[i + 1])
    with open(report_file_name, "w") as file2:
        file2.write(f"supply,{supply}\n")
        file2.write(f"buy,{buy}\n")
        file2.write(f"result,{supply - buy}\n")
