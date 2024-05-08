def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as input_file,
          open(report_file_name, "w") as result_file):
        summary = {}
        for line in input_file:
            position, quantity = line.split(",")
            quantity = int(quantity)

            if position in summary:
                summary[position] += quantity
            else:
                summary[position] = quantity

        summary["result"] = summary["supply"] - summary["buy"]

        ordered_positions = ["supply", "buy", "result"]
        for position in ordered_positions:
            result_file.write(f"{position},{summary[position]}\n")
