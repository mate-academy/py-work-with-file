def create_report(data_file_name: str, report_file_name: str) -> None:
    data_from_file = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            data_from_file[line.split(",")[0]] += int(line.split(",")[1])

    report_text = ""
    for key, value in data_from_file.items():
        report_text += f"{key},{value}\n"

    report_text += (
        f'result,{data_from_file["supply"] - data_from_file["buy"]}\n'
    )
    with open(report_file_name, "w") as report_file:
        report_file.write(report_text)
