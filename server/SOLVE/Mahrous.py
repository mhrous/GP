import json
from ntpath import basename

from HELP.file_tool import get_file_from_folder
from SOLVE.solveTree import SolveTree


def main(data):
    result = []
    for item in data:
        tree = SolveTree(item)
        parse = tree.parser()
        result.append(tree.parser())
    return result


if __name__ == '__main__':
    files = get_file_from_folder("../Data/nlp_correct_text/mahrous")

    for path in files:
        file_name = basename(path)
        file = open(path, "r", encoding="utf8")
        text = file.read()
        file.close()
        data = json.loads(text)
        if "data" in data:
            solve = main(data['data'])
            with open(f'../Data/solve/{file_name}', 'w', encoding="utf8") as json_file:
                json.dump(solve, json_file)
