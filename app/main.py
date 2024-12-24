def create_report(data_file_name: str, report_file_name: str) -> None:
    count_cont = {}

    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "w") as file_out):
        content_in = file_in.read()
        sep_cont = content_in.split("\n")
        for position in sep_cont:
            item_list = position.split(",")
            if len(item_list) == 2:
                if item_list[0] in count_cont:
                    count_cont[item_list[0]] += int(item_list[1])
                else:
                    count_cont[item_list[0]] = int(item_list[1])
            else:
                break
        supply = f"supply,{count_cont["supply"]}"
        buy = f"buy,{count_cont["buy"]}"
        calc = int(count_cont["supply"]) - int(count_cont["buy"])
        result = f"result,{calc}"
        content_out = f"{supply}\n{buy}\n{result}\n"
        file_out.write(content_out)
