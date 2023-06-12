def create_report(
        data_file_name: str,
        report_file_name: str) -> None:
    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "w") as file_out):
        operations = {
            "supply": 0,
            "buy": 0
        }

        for row in file_in.read().split("\n"):
            if row:
                operation, value = row.split(",")
                operations[operation] += int(value)

        result = operations["supply"] - operations["buy"]

        supply = operations["supply"]
        buy = operations["buy"]
        file_out.writelines([
            f"supply,{supply}\n",
            f"buy,{buy}\n",
            f"result,{result}\n"
        ])
