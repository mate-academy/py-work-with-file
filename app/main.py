import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    result_operation = {"supply": 0, "buy": 0}
    try:
        with open(data_file_name, "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                type_operation, value = row
                if type_operation in result_operation:
                    try:
                        int_value = int(value)
                    except ValueError:
                        print("error value")
                        continue
                    result_operation[type_operation] += int_value
    except FileNotFoundError:
        print("file not found")
        return
    result = result_operation["supply"] - result_operation["buy"]
    try:
        with open(report_file_name, "w") as reportefile:
            reportefile.write(f"supply,{result_operation["supply"]}\n")
            reportefile.write(f"buy,{result_operation["buy"]}\n")
            reportefile.write(f"result,{result}\n")
    except IOError:
        print("write error")
        return
