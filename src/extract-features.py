import os.path
import re

CURRENT_DIR = os.path.dirname(__file__)
WIKI_DIR = os.path.join(CURRENT_DIR, '../data/curated_data/cleaned')
FEATURE_DIR = os.path.join(CURRENT_DIR, '../data/curated_data/features/')


def get_pdtb_filepath(file_name):
    pdtb_dir = 'output/' + file_name + '.pipe'
    return os.path.join(WIKI_DIR, pdtb_dir)


def get_n_discourse_relations_from_pdtb_annotations(pdtb_filepath):
    with open(pdtb_filepath, 'r') as f:
        annotations = f.read()
        explicit_relations = annotations.split('Explicit|')[1:]
        relation_type_to_counts = {}
        for relation in explicit_relations:
            # print(relation)
            relation_type = re.findall(r'\|\|\|[\W\w]*?\|\|\|\|\|\|\|\|\|\|\|', relation)[0]
            relation_type = re.sub(r'\|+', "", relation_type)
            if relation_type.isalpha():
                if relation_type not in relation_type_to_counts.keys():
                    relation_type_to_counts[relation_type] = 1
                else:
                    relation_type_to_counts[relation_type] += 1
        print(explicit_relations)
        n_explicit = len(explicit_relations)
        count_list = []
        for relation_type, count in relation_type_to_counts.items():
            count_list.append(relation_type + "=" + str(count) + '\n')
        relation_type_features = ''.join(count_list)
        return n_explicit, relation_type_features


def read_wc(is_simple=False):
    wc_path = os.path.join(WIKI_DIR, 'simple_wc.txt') if is_simple else os.path.join(WIKI_DIR, 'regular_wc.txt')
    with open(wc_path, 'r') as f:
        wc_list = f.read().split('\n')
        return wc_list


def write_feature_file(is_simple=False):
    wc_list = read_wc(is_simple)
    for doc_count in range(50):
        cleaned_file_name = 'simple' + str(doc_count) + '.txt' if is_simple else 'regular' + str(doc_count) + '.txt'
        # print(cleaned_file_name)
        # print(get_pdtb_filepath(cleaned_file_name))
        n_relations, relation_type_features = get_n_discourse_relations_from_pdtb_annotations(
            get_pdtb_filepath(cleaned_file_name))
        print(n_relations)
        norm_n_explicit = n_relations / int(wc_list[doc_count])
        print(norm_n_explicit)
        output_path = FEATURE_DIR + cleaned_file_name
        with open(output_path, 'w+') as f:
            norm_n_explicit = n_relations / int(wc_list[doc_count])
            f.write('n_explicit=' + str(norm_n_explicit) + '\n')
            f.write(relation_type_features)


def main():
    write_feature_file()
    # write_feature_file(is_simple=True)


if __name__ == '__main__':
    main()
