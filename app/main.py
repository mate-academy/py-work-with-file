def create_report(data_file_name: str, report_file_name: str):

    with open(data_file_name, "r") as f:
        lines = f.readlines()

    supply = 0
    buy = 0
    for line in lines:
        line = line.strip().split(',')
        if "supply" in line:
            supply += int(line[1])
        elif "buy" in line:
            buy += int(line[1])

    result_list = [
        f"supply,{supply}\n",
        f"buy,{buy}\n",
        f"result,{supply - buy}\n"
    ]

    with open(report_file_name, "w") as f:
        f.writelines(result_list)
