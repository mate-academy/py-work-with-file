def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {}

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            line = line.strip()

            if line:
                elements = line.split(",")

                if elements[0] not in result:
                    result[elements[0]] = int(elements[1])
                else:
                    result[elements[0]] += int(elements[1])

        with open(report_file_name, "w") as report_file:
            report_file.write(f"supply,{result["supply"]}\n")
            report_file.write(f"buy,{result["buy"]}\n")
            report_file.write(f"result,{result["supply"] - result["buy"]}\n")
