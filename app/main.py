from os import path


def create_report(data_file_name: str, report_file_name: str) -> None:
    base_directory = "C:\\Projects_python\\Mate_Projects\\Work_with_file"
    file_path = path.join(base_directory, data_file_name)

    if not path.exists(file_path):
        print(f"{data_file_name} not found.")
        return

    if not len(report_file_name) or report_file_name[-4:] != ".csv":
        print(
            f'Invalid report_file_name: "{report_file_name}". '
            f'For example: "name.csv"'
        )
        return

    with open(file_path, "r") as input_file:
        with open(report_file_name, "w") as output_file:
            supply_total = 0
            buy_total = 0

            for line in input_file:
                try:
                    parts = line.strip().split(",")
                    action, amount = parts

                    if action == "supply":
                        supply_total += int(amount)

                    elif action == "buy":
                        buy_total += int(amount)

                except ValueError:
                    pass

            result = supply_total - buy_total

            output_file.write(
                f"supply,{supply_total}\n"
                f"buy,{buy_total}\n"
                f"result,{result}\n"
            )
