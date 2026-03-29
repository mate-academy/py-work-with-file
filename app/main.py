def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {"buy": 0, "supply": 0}
    with open(data_file_name, "r") as file:
        for row in file:
            key, value = row.split(",")
            value = int(value)
            result[key] += value
    with open(report_file_name, "w") as file:
        print("supply", result["supply"], sep=",", file=file)
        print("buy", result["buy"], sep=",", file=file)
        print("result", result["supply"] - result["buy"], sep=",", file=file)
