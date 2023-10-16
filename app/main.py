from typing import Any


def create_report(data_file_name: str, report_file_name: str) -> Any:
    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "w") as file_out):
        supply, buy = 0, 0
        information_in_file = file_in.readlines()
        for line in information_in_file:
            res = line.split(",")
            if res[0] == "supply":
                supply += int(res[1])
            else:
                buy += int(res[1])
        file_out.write(f"supply,{supply}\n")
        file_out.write(f"buy,{buy}\n")
        file_out.write(f"result,{supply - buy}\n")
