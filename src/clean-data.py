import os.path
import re

from textstat.textstat import textstat

CURRENT_DIR = os.path.dirname(__file__)
REGULAR_WIKI_DIR = os.path.join(CURRENT_DIR, '../data/curated_data/regular/')
SIMPLE_WIKI_DIR = os.path.join(CURRENT_DIR, '../data/curated_data/simple/')
PDTB_ANNOTATIONS_DIR = os.path.join(CURRENT_DIR, '../data/annotations/')


def read_file(file_name, is_simple=False):
    file_dir = SIMPLE_WIKI_DIR if is_simple else REGULAR_WIKI_DIR
    file_path = os.path.join(file_dir, file_name)
    with open(file_path, "r") as f:
        return f.read()


# TODO(veenaarv) read text_stats doc to see if we need further normalization
def normalize_text(text):
    return re.sub(r'(\[\d*])|(\d*)', "", text)


def print_readability_metrics(text, file_name):
    print(file_name, " readability metrics")
    print("flesch reading ease: ", textstat.flesch_reading_ease(text))
    print("dale chall readability: ", textstat.dale_chall_readability_score(text))
    print("smog index: ", textstat.smog_index(text))
    print('------------------------------------------------')


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


def main():
    regular_text = read_file('komodo_dragon.txt')
    simple_text = read_file('simple_komodo_dragon.txt', is_simple=True)
    reg_norm = normalize_text(regular_text)
    sim_norm = normalize_text(simple_text)
    print_readability_metrics(reg_norm, 'komodo_dragon.txt')
    print_readability_metrics(sim_norm, 'simple_komodo_dragon.txt')
    # print(get_n_discourse_relations_from_pdtb_annotations('wsj_2300.txt.pipe'))


if __name__ == '__main__':
    main()
