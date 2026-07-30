def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as data:
        lines = data.readlines()

    supply = []
    buy = []

    for line in lines:
        if line.split(",")[0].lower() == "supply":
            supply.append(int(line.split(",")[-1]))
        elif line.split(",")[0].lower() == "buy":
            buy.append(int(line.split(",")[-1]))


    with open(report_file_name, "w") as report:
        report.writelines("supply," + str(sum(supply)) + "\n")
        report.writelines(("buy," + str(sum(buy))) + "\n")
        report.writelines("result," + str(sum(supply) - sum(buy)) + "\n")
