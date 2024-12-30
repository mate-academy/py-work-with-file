def create_report(data_file_name: str, report_file_name: str) -> int:
    read_file = open(data_file_name, mode="r")
    write_file = open(report_file_name, mode="w")
    output = {}

    line_number = 1
    for line in read_file:
        typ, amount = line.split(",")
        if typ not in output.keys():
            output[typ] = int(amount)
        else:
            output[typ] += int(amount)
        line_number += 1

    output["result"] = output["supply"] - output["buy"]

    result_lines = [
        "supply," + str(output["supply"]),
        "buy," + str(output["buy"]),
        "result," + str(output["result"])
    ]
    return write_file.write("\n".join(result_lines) + "\n")
