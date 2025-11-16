def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = {}

    file_source = open("../" + data_file_name)
    file_report = open(report_file_name, "w")

    for line in file_source.readlines():
        line_stripped = line.strip()
        if line_stripped == "":
            break

        list_line = line_stripped.split(",")

        report_dict[list_line[0]] = (report_dict.get(list_line[0], 0)
                                     + int(list_line[1]))

    file_source.close()

    file_report.write(f"supply,{report_dict.get("supply", 0)}\n")
    file_report.write(f"buy,{report_dict.get("buy", 0)}\n")
    file_report.write(f"result,{report_dict.get("supply", 0)
                                - report_dict.get("buy", 0)}\n")

    file_report.close()
