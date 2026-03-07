def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = {}

    with open(data_file_name, "r") as file:
        for line in file:
            if line == "" or line == "\n":
                continue

            cleaned_line = line.strip("\n").split(",")

            if cleaned_line[0] not in report_dict:
                report_dict[cleaned_line[0]] = int(cleaned_line[1])
            else:
                report_dict[cleaned_line[0]] += int(cleaned_line[1])

    report_dict["result"] = (report_dict.get("supply", 0)
                             - report_dict.get("buy", 0))

    with open(report_file_name, "w") as file:
        file.write(f'supply,{report_dict.get("supply", 0)}\n'
                   f'buy,{report_dict.get("buy", 0)}\n'
                   f'result,{report_dict.get("result", 0)}\n')
