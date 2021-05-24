"""
English – Tigrigna Dictionary

| (m) masculine | (f) feminine | (a) adjective | (n) noun | (v) verb | (adv) adverb |
| (prep) preposition | (prn) pronoun | (con) conjunction | (interj) interjection |

"""
import typing
import json
import transliterator as tlr


def main():
    text_path = (
        "C:/Users/camer/Dropbox/CUNY/Tigrinya-NLP/data/texts/eng-tig-dict.txt"
    )
    eng_tig_dict = dict()
    with open(text_path, "r", encoding="utf-8") as eng_tig:
        tig_dict = eng_tig.readlines()
        for i in range(len(tig_dict)):
            tig_dict[i] = tig_dict[i].replace("", "")
            tig_dict[i] = tig_dict[i].replace("\n", "")
            tig_dict[i] = tig_dict[i].replace("(", "|")
            tig_dict[i] = tig_dict[i].replace(")", "|")
            line = tig_dict[i].split("|")
            eng_tig_dict[line[0].replace("-", "").strip()] = {
                "POS": line[1],
                "words": {},
            }
            if "," in line[2]:
                line[2] = line[2].split(",")

                for word in line[2]:
                    x, y, z = tlr.ti_transliterator(word)
                    if (
                        not word
                        in eng_tig_dict[line[0].replace("-", "").strip()][
                            "words"
                        ]
                    ):
                        eng_tig_dict[line[0].replace("-", "").strip()][
                            "words"
                        ][word.strip()] = x.strip()
            else:
                x, y, z = tlr.ti_transliterator(line[2])
                eng_tig_dict[line[0].replace("-", "").strip()]["words"][
                    line[2].strip()
                ] = x.strip()
        # Write to json file.
        json_object = json.dumps(
            eng_tig_dict, ensure_ascii=False, indent=4
        ).encode("utf8")
        with open("../src/eng-tig.json", "w", encoding="utf-8") as f_dict:
            f_dict.write(json_object.decode("utf8"))


if __name__ == "__main__":
    main()
