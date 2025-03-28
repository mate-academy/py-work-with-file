# write your code here
def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as input_data, \
            open(report_file_name, "w") as report_data:
        reporting_counter = dict(supply=0, buy=0, result=0)
        for line in input_data:
            action, value = line.split(",")
            reporting_counter[action] += int(value)
        reporting_counter["result"] = \
            reporting_counter["supply"] - reporting_counter["buy"]
        for key, value in reporting_counter.items():
            report_data.write(f"{key},{value}\n")
