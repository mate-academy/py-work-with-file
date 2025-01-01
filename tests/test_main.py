from app.main import process_csv
import tempfile
import os


def test_process_csv():
    # Создаем временные файлы
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as input_file, \
         tempfile.NamedTemporaryFile(mode='w', delete=False) as output_file:

        # Записываем данные в input.csv
        input_file.write("supply,30\nbuy,10\nbuy,13\nsupply,17\nbuy,10\n")
        input_file.close()

        # Запускаем функцию
        process_csv(input_file.name, output_file.name)

        # Закрываем output_file явно перед его удалением
        output_file.close()

        # Читаем результат из output.csv
        with open(output_file.name, 'r') as f:
            lines = f.readlines()

        # Проверяем результаты
        assert lines[0].strip() == "supply,47"
        assert lines[1].strip() == "buy,33"
        assert lines[2].strip() == "result,14"

        # Удаляем временные файлы
        os.remove(input_file.name)
        os.remove(output_file.name)