def create_report(data_file: str, report_file: str) -> None:
    with (open(data_file, "r") as open_file,
          open(report_file, "w") as write_file):
        content = {}
        for line in open_file.readlines():
            key, amount = line.split(",")
            if key not in content.keys():
                content[key] = int(amount)
            else:
                content[key] += int(amount)
        write_file.write(f'supply,{content["supply"]}\n')
        write_file.write(f'buy,{content["buy"]}\n')
        write_file.write(f'result,{content["supply"] - content["buy"]}\n')
