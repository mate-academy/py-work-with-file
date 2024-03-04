def create_report(data_file_name: str, report_file_name: str):
    with open(f"{data_file_name}", "r") as data:
        data_read = data.read()
    data_split = data_read.split("\n")
    supply = sum([int(cash[7:])
                  for cash in data_split
                  if cash.startswith("s")]
                 )
    buy = sum([int(cash[4:])
               for cash in data_split
               if cash.startswith("b")]
              )
    result = supply - buy
    with open(f"{report_file_name}", "w") as file_out:
        file_out.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
