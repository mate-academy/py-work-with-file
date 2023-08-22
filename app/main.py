def create_report(data_file_name: str, report_file_name: str) -> None:

    with open(data_file_name, "r") as source:
        info = source.readlines()

    file_content = {
        "supply": 0,
        "buy": 0
    }
    for line in info:
        line = line.split(",")
        file_content[line[0]] += int(line[1])
    file_content["result"] = file_content["supply"] - file_content["buy"]
    file_content = [f"{key},{value}\n" for key, value in file_content.items()]
    with open(report_file_name, "w") as report:
        report.write("".join(file_content))
