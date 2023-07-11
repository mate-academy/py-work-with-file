# write your code here
def create_report(date_file_name: str, report_file_name: str) -> None:
    with open(date_file_name, "r") as data_file, \
         open(report_file_name, "a") as report_file:

        data_of_report = {
            "supply": 0,
            "buy": 0,
            "result": None
        }

        for line in data_file:
            line = line[:-1].split(",")

            name_part = line[0]
            count_of_part = int(line[1])

            data_of_report[name_part] += count_of_part

        difference = data_of_report["supply"] - data_of_report["buy"]
        data_of_report["result"] = difference

        for name, count in data_of_report.items():
            transform_to_string = f"{name},{count}\n"
            report_file.write(transform_to_string)
