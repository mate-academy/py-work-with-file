import re


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with (open(data_file_name, "r") as file_in,
            open(report_file_name, "w") as file_out):
        lines = file_in.readlines()
        for line in lines:
            values = re.split(r"[,\n]", line)
            if values[0] == "supply":
                supply += int(values[1])
            else:
                buy += int(values[1])
        file_out.write(f"supply,{supply}\n")
        file_out.write(f"buy,{buy}\n")
        file_out.write(f"result,{supply - buy}\n")
