def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "a") as report_file):
        results = {}
        for line in data_file.readlines():
            columns = line.rstrip("\n").split(",")
            [operation, count] = columns
            results[operation] = results.get(operation, 0) + int(count)

        results["result"] = results["supply"] - results["buy"]

        for key, value in results.items():
            report_file.write(f"{key},{value}\n")
