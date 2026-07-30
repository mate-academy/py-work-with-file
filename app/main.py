def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {"supply": 0, "buy": 0}
    with (open(data_file_name) as file_in,
          open(report_file_name, "w") as file_out):
        for line in file_in:
            operation, amount = line.split(",")
            result[operation] += int(amount)
        result["result"] = result["supply"] - result["buy"]
        print(result)
        [print(f"{key},{value}", file=file_out)
         for key, value in result.items()]
