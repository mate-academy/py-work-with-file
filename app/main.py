# write your code here
def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as data_file:
        data = data_file.readlines()
        print(data)
        for line in data:
            operation_type, value = line.split(",")
            if operation_type == "supply":
                supply += int(value)
            elif operation_type == "buy":
                buy += int(value)
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{supply - buy}\n")
        report_file.write("")