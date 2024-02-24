import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    data = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as file:
        for line in file.readlines():
            if line is not None:
                if line[0] == "s":
                    data["supply"] += int(line[7:])
                else:
                    data["buy"] += int(line[4:])
    with open(report_file_name, "w") as f:
        f.write(
            f"supply,{data['supply']}\n"
            f"buy,{data['buy']}\n"
            f"result,{data['supply'] - data['buy']}\n"
        )
