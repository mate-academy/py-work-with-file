def create_report(data_file_name: str, report_file_name: str):

    supply = 0
    buy = 0

    with open(data_file_name, "r") as data_file:
        lines = data_file.readlines()
        with open(report_file_name, "w") as report_file:
            for line in lines:
                data = line.split(',')
                if data[0] == "supply":
                    supply += int(data[1])
                elif data[0] == "buy":
                    buy += int(data[1])

            report_file.write(f"supply,{supply}\n"
                              f"buy,{buy}\n"
                              f"result,{supply - buy}\n")
