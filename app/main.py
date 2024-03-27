def create_report(data_file_name: str, report_file_name: str) -> None:

    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "w") as report_file):
        result = {}
        for line in data_file:
            parameter, data = line.split(",")
            if parameter not in result:
                result[parameter] = int(data)
            else:
                result[parameter] += int(data)

        report_file.write(f"{"supply"},{result["supply"]}\n")
        report_file.write(f"{"buy"},{result["buy"]}\n")
        report_file.write(f"result,{result["supply"] - result["buy"]}\n")
