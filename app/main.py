def create_report(data_file_name: str, report_file_name: str) -> None:
    warehouse = {
        "supply": 0,
        "buy": 0,
        "result": 0
    }
    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "a") as report_file):
        for line in data_file:
            if not line:
                continue
            list_from_line = line.split(",")
            warehouse[list_from_line[0]] += int(list_from_line[1])

        warehouse["result"] = warehouse["supply"] - warehouse["buy"]

        for key, value in warehouse.items():
            report_file.write(f"{key},{value}\n")
