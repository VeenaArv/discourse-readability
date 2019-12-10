import os.path

CURRENT_DIR = os.path.dirname(__file__)
WIKI_DIR = os.path.join(CURRENT_DIR, '../data/curated_data/')
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


def write_feature_file(wiki_file_names):
    for wiki_path in wiki_file_names:
        n_relations = get_n_discourse_relations_from_pdtb_annotations(get_pdtb_filepath(wiki_path))
        output_path = FEATURE_DIR + wiki_path
        with open(output_path, 'w+') as f:
            f.write('n_explicit=' + str(n_relations[0]) + '\n')
            f.write('n_implicit=' + str(n_relations[1]) + '\n')


def main():
    write_feature_file(['komodo_dragon.txt',
                        'simple_komodo_dragon.txt'])


if __name__ == '__main__':
    main()
