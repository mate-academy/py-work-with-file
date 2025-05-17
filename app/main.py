def create_report(data_file_name: str, report_file_name: str) -> None:
    calculated_results = {}

    with (open(data_file_name, "r") as data,
          open(report_file_name, "w") as report):
        for line in data:
            line = line.strip()
            if not line:
                continue

            product, quantity = line.split(",")

            if product not in calculated_results:
                calculated_results[product] = int(quantity)
            else:
                calculated_results[product] += int(quantity)

        calculated_results["result"] = (
            calculated_results.get("supply", 0)
            - calculated_results.get("buy", 0)
        )

        for key in ["supply", "buy", "result"]:
            value = calculated_results.get(key, 0)
            report.write(f"{key},{value}\n")
