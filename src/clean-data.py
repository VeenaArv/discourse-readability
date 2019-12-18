import os.path
import re

from textstat.textstat import textstat

CURRENT_DIR = os.path.dirname(__file__)
WIKI_DIR = os.path.join(CURRENT_DIR, '../data/curated_data/development/')
OUTPUT_DIR = os.path.join(CURRENT_DIR, '../data/curated_data/cleaned/')


def read_file(file_name, is_simple=False):
    file_path = os.path.join(WIKI_DIR, 'simple/' + file_name) if is_simple else os.path.join(WIKI_DIR,
                                                                                             'complex/' + file_name)
    with open(file_path, "r", encoding='utf8', errors='ignore') as f:
        return f.read()


def write_counts_to_file(is_simple=False):
    file_name = 'simple_wc.txt' if is_simple else 'regular_wc.txt'
    output_file_path = os.path.join(OUTPUT_DIR, file_name)
    wiki_file_count = 0
    doc_count = 0
    with open(output_file_path, 'w+') as f:
        while doc_count < 50:
            wiki_file_name = 'wiki_0' + str(doc_count) if doc_count < 10 else 'wiki_' + str(doc_count)
            wiki_file_count += 1
            text = read_file(wiki_file_name, is_simple)
            doc_list = re.findall(r'</doc>[\S\s]*?</doc>', text)
            for doc in doc_list:
                doc = re.sub(r'</doc>', "", doc)
                doc = re.sub(r'<doc id[\S\s]*>', "", doc)
                doc = re.sub(r'(\[\d*])|(\d*)', "", doc)
                word_count = len(doc.split())
                if len(doc.split()) > 100:
                    f.write(str(word_count))
                    f.write('\n')
                    doc_count += 1
                if doc_count >= 50:
                    break


# TODO(veenaarv) read text_stats doc to see if we need further normalization
def normalize_text(is_simple=False):
    wiki_file_count = 0
    doc_count = 0
    while doc_count < 50:
        wiki_file_name = 'wiki_0' + str(doc_count) if doc_count < 10 else 'wiki_' + str(doc_count)
        wiki_file_count += 1
        text = read_file(wiki_file_name, is_simple)
        print(text)
        doc_list = re.findall(r'</doc>[\S\s]*?</doc>', text)
        # print('doc_list', doc_list)
        for doc in doc_list:
            # print(doc)
            doc = re.sub(r'</doc>', "", doc)
            doc = re.sub(r'<doc id[\S\s]*>', "", doc)
            doc = re.sub(r'(\[\d*])|(\d*)', "", doc)
            file_name = 'simple' + str(doc_count) + '.txt' if is_simple else 'regular' + str(doc_count) + '.txt'
            output_file_path = os.path.join(OUTPUT_DIR, file_name)
            if len(doc.split()) > 100:
                print('doc--------------------------------------------------------')
                print(doc)
                with open(output_file_path, 'w+', encoding='utf8', errors='ignore') as f:
                    f.write(doc)
                    doc_count += 1
            if doc_count >= 50:
                break


def print_readability_metrics(text, file_name):
    print(file_name, " readability metrics")
    print("flesch reading ease: ", textstat.flesch_reading_ease(text))
    print("dale chall readability: ", textstat.dale_chall_readability_score(text))
    print("smog index: ", textstat.smog_index(text))
    print('------------------------------------------------')


def main():
    # regular_text = read_file('komodo_dragon.txt')
    # simple_text = read_file('simple_komodo_dragon.txt')
    # reg_norm = normalize_text(regular_text)
    # sim_norm = normalize_text(simple_text)
    # print_readability_metrics(reg_norm, 'komodo_dragon.txt')
    # print_readability_metrics(sim_norm, 'simple_komodo_dragon.txt')
    # normalize_text()
    # normalize_text(is_simple=True)
    write_counts_to_file()
    write_counts_to_file(is_simple=True)


if __name__ == '__main__':
    main()
