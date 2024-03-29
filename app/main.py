def create_report(data_file_name: str, report_file_name: str) -> None:
    result_list = []
    key_list = []

    with open(data_file_name, "r") as f:
        for line in f.read().split("\n"):
            if len(line) > 0:
                result_list.append(line.split(","))
                key_list.append(line.split(",")[0])

    supply = sum([int(data[1]) for data in result_list if data[0] == "supply"])
    buy = sum([int(data[1]) for data in result_list if data[0] == "buy"])
    result = supply - buy

    with open(report_file_name, "a") as f:
        f.write(f"supply,{supply}\n")
        f.write(f"buy,{buy}\n")
        f.write(f"result,{result}\n")
