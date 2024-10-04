
def create_report(data_file_name: str, report_file_name: str) -> None:
    buy = 0
    supply = 0
    with open(f"{data_file_name}") as file:
        for line in file:
            ln = line.split(",")
            if ln[0] == "buy":
                buy += int(ln[1])
            elif ln[0] == "supply":
                supply += int(ln[1])
    with open(f"{report_file_name}", "w") as file:
        file.write(f"supply,{supply}\nbuy,{buy}\n"  # noqa: E231
                   f"result,{supply - buy}\n")  # noqa: E231
