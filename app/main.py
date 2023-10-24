
def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    with open(data_file_name, "r") as data_file:
        data_list = data_file.read()

    data_list = data_list.strip()
    data_list = data_list.split("\n")
    for index, data in enumerate(data_list):
        data_list[index] = data.split(",")
    supply = 0
    buy = 0
    for data in data_list:
        if data[0] == "supply":
            supply += int(data[1])
        if data[0] == "buy":
            buy += int(data[1])
    result = supply - buy

    report = f"supply,{supply}\nbuy,{buy}\nresult,{result}\n"

    with open(report_file_name, "w") as result_file:
        result_file.write(report)
