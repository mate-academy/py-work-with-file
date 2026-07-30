def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    try:
        with open(f"{data_file_name}", "r") as file_in,\
             open(report_file_name, "w") as file_out:
            for line in file_in:
                list_line = line.split(",")
                if list_line[0] == "supply":
                    supply += int(list_line[1])
                if list_line[0] == "buy":
                    buy += int(list_line[1])

            file_out.write(
                f"supply,{supply}\n"
                f"buy,{buy}\n"
                f"result,{supply - buy}\n"
            )
    except FileNotFoundError:
        print(f"FileNotFoundError: "
              f'No such file or directory: "{data_file_name}"')
