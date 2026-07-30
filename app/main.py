def create_report(data_file_name: str, report_file_name: str) -> None:
    data_dict = {"supply": 0, "buy": 0, "result": 0}
    with open(data_file_name, "r") as file:
        for line in file.read().split("\n")[:-1]:
            key, value = line.split(",")[0], line.split(",")[1]
            data_dict[key] += int(value)

    with open(report_file_name, "w") as file:
        supply = data_dict["supply"]
        buy = data_dict["buy"]
        result = data_dict["supply"] - data_dict["buy"]
        file.write(f"supply,{supply}\n"
                   f"buy,{buy}\n"
                   f"result,{result}\n")
