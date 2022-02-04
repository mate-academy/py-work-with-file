def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, 'r') as f:
        with open(report_file_name, 'w') as wr_file:
            buy = 0
            supply = 0
            for line in f.readlines():
                if line != '':
                    ls = line.split(',')
                    if ls[0] == 'buy':
                        buy += int(ls[1])
                        continue
                    supply += int(ls[1])
            report = (f'supply,{supply}\n'
                      f'buy,{buy}\n'
                      f'result,{supply - buy}\n')
            wr_file.write(report)

