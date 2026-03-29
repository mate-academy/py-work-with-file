def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    report_dict = {
        "supply": 0,
        "buy": 0,
        "result": 0
    }

    with open(data_file_name, "r") as file:
        while True:
            line = file.readline()

            if not line:
                break

            data = line.replace("\n", "").split(",")
            key = data[0]
            value = int(data[1])

            report_dict[key] += value

    supply = report_dict["supply"]
    buy = report_dict["buy"]
    result = report_dict["result"] = supply - buy

    report_content = (f"supply,{supply}\n"
                      f"buy,{buy}\n"
                      f"result,{result}\n")

    with open(report_file_name, "w") as file:
        file.write(report_content)
