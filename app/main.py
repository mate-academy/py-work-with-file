def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "w") as file_out):
        for line in file_in:
            if line.strip():
                name, value = line.strip().split(",")
                if name == "supply":
                    supply += int(value)
                elif name == "buy":
                    buy += int(value)

        data_to_write = f"supply,{supply}\n" \
                        f"buy,{buy}\n" \
                        f"result,{supply - buy}\n"
        file_out.write(data_to_write)
