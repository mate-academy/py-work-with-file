def create_report(data_file_name: str, report_file_name: str) -> None:
    if not data_file_name == report_file_name:
        with (
            open(data_file_name, "r") as read_file,
            open(report_file_name, "w") as final_report
        ):
            initial_data = read_file.readlines()
            print(initial_data)
            report_dict = {"supply": 0, "buy": 0}

            for line in initial_data:
                stripped_line = line.strip()
                splitted_stripped_line = stripped_line.split(",")
                print(splitted_stripped_line)

                key, value = splitted_stripped_line[0], int(splitted_stripped_line[1])

                report_dict[key] += value

            report_dict["result"] = report_dict["supply"] - report_dict["buy"]

            for key, value in report_dict.items():
                final_report.writelines(key + "," + str(value) + "\n")
