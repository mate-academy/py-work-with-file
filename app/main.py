import csv


def create_report(data_file_name: str, report_file_name: str):
    result_dict = {}
    with open(data_file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] not in result_dict:
                result_dict[row[0]] = int(row[1])
            else:
                result_dict[row[0]] += int(row[1])
    result_dict["result"] = result_dict["supply"] - \
                            result_dict["buy"]
    with open(report_file_name, "a") as report:
        """
        'write' method performed three times here
        to guarantee the order of lines in final
        report
        """
        report.write(
            f"supply,{result_dict['supply']}\n"
        )
        report.write(
            f"buy,{result_dict['buy']}\n"
        )
        report.write(
            f"result,{result_dict['result']}\n"
        )
