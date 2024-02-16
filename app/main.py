def create_report(data_file_name: str, report_file_name: str) -> None:
    market_info = {"supply": 0,
                   "buy": 0}
    with (open(data_file_name, "r") as input_file,
          open(report_file_name, "w") as output_file):
        for line in input_file:
            market_info[line.replace(",", " ").split()[0]] += int(
                line.replace(",", " ").split()[1])
        for key, value in market_info.items():
            output_file.write(f"{key}, {value}\n".replace(" ", ""))
        output_file.write(f"result, "
                          f"{market_info["supply"] - market_info["buy"]}\n"
                          .replace(" ", ""))
