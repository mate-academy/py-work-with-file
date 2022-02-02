def parse_input_file(file: str) -> dict:
    parsed_data = {'supply': 0, 'buy': 0, 'result': 0}
    with open(file=file, mode='r') as fin:
        for line in fin:
            parsed_line = line.split(',')
            parsed_data[parsed_line[0]] += int(parsed_line[1].strip())

    parsed_data['result'] = parsed_data['supply'] - parsed_data['buy']
    return parsed_data


def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dictionary = parse_input_file(data_file_name)
    with open(file=report_file_name, mode='w') as fout:
        for key in report_dictionary:
            fout.write(f"{key},{report_dictionary[key]}\n")


if __name__ == '__main__':
    create_report('../apples.csv', 'tmp.csv')
