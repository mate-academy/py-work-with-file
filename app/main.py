import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file:
        data = csv.reader(file)
        result_dict = {}
        for row in data:
            if row[0] in result_dict:
                result_dict[row[0]] += int(row[1])
            else:
                result_dict[row[0]] = int(row[1])
        result_dict["result"] = result_dict["supply"] - result_dict["buy"]
        with open(report_file_name, "w") as new_file:
            new_file.write(f"supply,{result_dict['supply']}\n")
            new_file.write(f"buy,{result_dict['buy']}\n")
            new_file.write(f"result,{result_dict['result']}\n")
