import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file_in,\
            open(report_file_name, "w") as file_out:
        reader = csv.reader(file_in)
        dict_to_write = {}
        for row in reader:
            if row[0] in dict_to_write:
                dict_to_write[row[0]] += int(row[1])
            elif row[0] not in dict_to_write:
                dict_to_write[row[0]] = int(row[1])

        dict_to_write["result"] = (
            dict_to_write["supply"] - dict_to_write["buy"]
        )

        file_out.write(
            f"supply,{dict_to_write['supply']}\n"
            f"buy,{dict_to_write['buy']}\n"
            f"result,{dict_to_write['result']}\n"
        )
