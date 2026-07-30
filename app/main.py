def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name) as data_file,
          open(report_file_name, "a") as report_file):
        file_contents = data_file.read().split("\n")
        csv_result = {}
        for line in file_contents:
            if line:
                key, value = line.split(",")
                if key not in csv_result:
                    csv_result[key] = int(value)
                    continue
                csv_result[key] += int(value)

        csv_result["result"] = csv_result["supply"] - csv_result["buy"]
        report_file.write(
            f"supply,{csv_result['supply']}\nbuy,"
            f"{csv_result['buy']}\nresult,{csv_result['result']}\n"
        )
