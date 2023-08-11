def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name) as file_in,
          open(report_file_name, "w") as file_out):
        lines = [word.split(",") for word in file_in.readlines() if word]
        print(lines[0])
        my_dict = {
            "supply": sum(
                [int(value[1]) for value in lines if value[0] == "supply"]
            ),
            "buy": sum(
                [int(value[1]) for value in lines if value[0] == "buy"]
            )
        }
        my_dict["result"] = my_dict["supply"] - my_dict["buy"]
        file_out.write(f"supply,{my_dict['supply']}\n"
                       f"buy,{my_dict['buy']}\n"
                       f"result,{my_dict['result']}\n")
