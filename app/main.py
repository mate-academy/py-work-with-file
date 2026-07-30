# write your code here
def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file_in, \
            open(report_file_name, "w") as file_out:
        supply = 0
        buy = 0

        for line in file_in:
            try:
                if line[0] == "b":
                    buy += int(line[4:])
                if line[0] == "s":
                    supply += int(line[7:])
            except Exception:
                break

        file_out.write(f"supply,{supply}\n"
                       f"buy,{buy}\n"
                       f"result,{supply - buy}\n")
