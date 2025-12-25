def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    information = dict()

    for value in data_file.readlines():

        index = value.find(",")
        key = value[: index]
        number = int(value[index + 1:])
        if information.get(key):

            information[key] += number
        else:

            information[key] = number

    data_file.close()

    result = information["supply"] - information["buy"]
    supply = information.get("supply")
    buy = information.get("buy")
    report_file = open(report_file_name, "a")
    report_file.write(f"supply,{supply}\n")
    report_file.write(f"buy,{buy}\n")
    report_file.write(f"result,{result}\n")
    report_file.close()
