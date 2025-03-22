def create_report(data_file_name, report_file_name):
    with open(data_file_name, "r") as data:
        with open(report_file_name, "w") as report:
            data_list = data.read().splitlines()
            supply = 0
            buy = 0
            for line in data_list:
                if line.split(",")[0] == "supply":
                    supply += int(line.split(",")[1])
                if line.split(",")[0] == "buy":
                    buy += int(line.split(",")[1])
            report.write(f"supply,{supply}\n"
                         f"buy,{buy}\n"
                         f"result,{supply - buy}\n")
