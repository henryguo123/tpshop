
import yaml

def yml_data_with_filename_and_key(file_name, key):
    with open("./data/" + file_name + ".yml", "r", encoding="utf-8") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)[key]
        case_data_list = list()
        for case_data in data.values():
            case_data_list.append(case_data)
        print(case_data_list)
        return case_data_list
