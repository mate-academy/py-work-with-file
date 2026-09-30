def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as input_file:

        with open(report_file_name, "a") as output_file:
            obj: dict = {}

            for line in input_file:
                arr = line.strip().split(",")
                if arr[0] in obj:
                    obj[arr[0]] = int(obj[arr[0]]) + int(arr[1])
                else:
                    obj[arr[0]] = int(arr[1])

            supply = obj.get("supply", 0)
            buy = obj.get("buy", 0)
            result = supply - buy

            output_file.write(f"supply,{supply}\n")
            output_file.write(f"buy,{buy}\n")
            output_file.write(f"result,{result}\n")


create_report("apples.csv", "new_apples.csv")
create_report("bananas.csv", "new_bananas.csv")
create_report("grapes.csv", "new_grapes.csv")
create_report("oranges.csv", "new_oranges.csv")
