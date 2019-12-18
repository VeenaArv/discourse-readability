import os.path

CURRENT_DIR = os.path.dirname(__file__)
WIKI_DIR = os.path.join(CURRENT_DIR, '../data/curated_data/cleaned/')
FEATURE_DIR = os.path.join(CURRENT_DIR, '../data/curated_data/features/')


def get_pdtb_filepath(file_name):
    pdtb_dir = 'output/' + file_name + '.pipe'
    return os.path.join(WIKI_DIR, pdtb_dir)


def get_n_discourse_relations_from_pdtb_annotations(pdtb_filepath):
    with open(pdtb_filepath, 'r') as f:
        annotations = f.read()
        n_implicit = 0
        n_explicit = 0
        for relation in annotations.split("|||||||||||||"):
            relation_type = relation.split("|||")[0].strip()
            if relation_type == "Implicit":
                n_implicit += 1
            elif relation_type == "Explicit":
                n_explicit += 1
            else:
                # add value to logs
                print(relation_type)
        return n_explicit, n_implicit


def read_wc(is_simple=False):
    wc_path = os.path.join(WIKI_DIR, 'simple_wc.txt') if is_simple else os.path.join(WIKI_DIR, 'regular_wc.txt')
    with open(wc_path, 'r') as f:
        wc_list = f.read().split('\n')
        return wc_list


def write_feature_file(is_simple=False):
    wc_list = read_wc(is_simple)
    for doc_count in range(50):
        cleaned_file_name = 'simple' + str(doc_count) + '.txt' if is_simple else 'regular' + str(doc_count) + '.txt'
        n_relations = get_n_discourse_relations_from_pdtb_annotations(get_pdtb_filepath(cleaned_file_name))
        output_path = FEATURE_DIR + cleaned_file_name
        with open(output_path, 'w+') as f:
            norm_n_explicit = n_relations[0] / int(wc_list[doc_count])
            norm_n_implicit = n_relations[1] / int(wc_list[doc_count])
            f.write('n_explicit=' + str(norm_n_explicit) + '\n')
            f.write('n_implicit=' + str(norm_n_implicit) + '\n')


def main():
    write_feature_file()
    write_feature_file(is_simple=True)


if __name__ == '__main__':
    main()
