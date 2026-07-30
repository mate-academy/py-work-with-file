import re


def create_report(data_file_name: str, report_file_name: str) -> None:
    file_data = open(data_file_name, "r")
    file_lines = file_data.readlines()
    print(file_lines)
    pattern = r"\d+"

    counter_supply = 0
    counter_buy = 0
    for line in file_lines:
        if "supply" in line:
            line = re.findall(pattern, line)
            counter_supply += int(line[0])
        else:
            line = re.findall(pattern, line)
            counter_buy += int(line[0])

    result = counter_supply - counter_buy
    file_data.close()

    file_report = open(report_file_name, "w")
    file_report.write(
        "supply," + str(counter_supply) + "\n"
        "buy," + str(counter_buy) + "\n"
        "result," + str(result) + "\n"
    )
    file_report.close()
