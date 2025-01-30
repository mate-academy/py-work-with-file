# write your code here
def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as data_f,
          open(report_file_name, "a") as report_f):
        actions_dict = {}
        actions = []
        lines = data_f.readlines()
        for line in lines:
            words = line.strip().split(",")
            actions.append(words)
        for action in actions:
            if not action[0] in actions_dict:
                actions_dict[f"{action[0]}"] = int(action[1])
            else:
                actions_dict[f"{action[0]}"] += int(action[1])
        report_f.write(f"supply,{actions_dict["supply"]}\n")
        report_f.write(f"buy,{actions_dict["buy"]}\n")
        report_f.write(f"result,{actions_dict["supply"]
                                 - actions_dict["buy"]}\n")
