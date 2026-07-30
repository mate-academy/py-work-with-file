def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "a") as report_file):
        total_dict = {}

        for line in data_file:
            key, val = line.strip().split(",")

            if key in total_dict:
                total_dict[key] += int(val)
            else:
                total_dict[key] = int(val)

        total_dict["result"] = total_dict["supply"] - total_dict["buy"]

        if "supply" in total_dict:
            report_file.write(f'supply,{total_dict["supply"]}\n')  # noqa: E231

        if "buy" in total_dict:
            report_file.write(f'buy,{total_dict["buy"]}\n')  # noqa: E231

        report_file.write(f'result,{total_dict["result"]}\n')  # noqa: E231


if __name__ == "__main__":
    create_report("../data.csv", "../report.csv")
