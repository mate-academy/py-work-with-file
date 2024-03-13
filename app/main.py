# write your code here
def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file,\
            open(report_file_name, "w") as report_file:
        data_file = \
            [line.split(",") for line in data_file.read().split("\n")][:-2]
        buy = 0
        supply = 0
        for element in data_file:
            if element[0] == "buy":
                buy += int(element[1])
            else:
                supply += int(element[1])
        result = supply - buy
        report_data = f"supply,{supply}\nbuy,{buy}\nresult,{result}\n"
        report_file.write(report_data)
