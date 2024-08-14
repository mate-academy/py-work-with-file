def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")

    data = [line.replace("\n", "").split(",") for line in data_file]

    result_dict = {}

    for el in data:
        if el[0] in result_dict:
            result_dict[el[0]] += int(el[1])
        else:
            result_dict[el[0]] = int(el[1])

    data_file.close()
    o_file = open(report_file_name, "x")

    o_file.write("supply," + f"{result_dict["supply"]}\n")
    o_file.write("buy," + f"{result_dict["buy"]}\n")
    o_file.write("result," + f"{result_dict["supply"] - result_dict["buy"]}\n")

    o_file.close()
