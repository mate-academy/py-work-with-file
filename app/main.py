def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as old_file,
          open(report_file_name, "w") as new_file):

        supply = 0
        buy = 0

        for line in old_file:
            if line:
                operation_type, amount = line.strip().split(",")
                amount = int(amount)

                if operation_type == "supply":
                    supply += amount
                elif operation_type == "buy":
                    buy += amount

        result = supply - buy

        new_file.write(f"supply,{supply}\n"
                       f"buy,{buy}\n"
                       f"result,{result}\n")
