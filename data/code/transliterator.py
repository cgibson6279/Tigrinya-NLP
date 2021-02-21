'''
Tigrinya Transliterater

Isayas Adhanom

The following piece of code generates the orthographic representation of a Tigrinya string.

To use this tool, simply select and run (press the play button or hit ctrl + enter) the following cell. You will then be prompted for the Tigrinya text you want to transliterate. Put the text in the provided input box and hit enter. The output will be displayed below the inserted text. If there were non-Tigrinya characters in the string, their count be displayed and they will be outputed without modification.

The orthographic representation is based on the information in this wikipedia article.
'''

phonetic_dict_ti = {'ሀ': 'hä', 'ሁ': 'hu', 'ሂ': 'hi', 'ሃ': 'ha', 'ሄ': 'he', 'ህ': 'h(ə)', 'ሆ': 'ho', 'ለ': 'lä', 'ሉ': 'lu',
                    'ሊ': 'li', 'ላ': 'la', 'ሌ': 'le', 'ል': 'l(ə)', 'ሎ': 'lo', 'ሐ': 'ḥä', 'ሑ': 'ḥu', 'ሒ': 'ḥi', 'ሓ': 'ḥa',
                    'ሔ': 'ḥe', 'ሕ': 'ḥ(ə)', 'ሖ': 'ḥo', 'መ': 'mä', 'ሙ': 'mu', 'ሚ': 'mi', 'ማ': 'ma', 'ሜ': 'me',
                    'ም': 'm(ə)', 'ሞ': 'mo', 'ሠ': 'śä', 'ሡ': 'śu', 'ሢ': 'śi', 'ሣ': 'śa', 'ሤ': 'śe', 'ሥ': 'ś(ə)',
                    'ሦ': 'śo', 'ረ': 'rä', 'ሩ': 'ru', 'ሪ': 'ri', 'ራ': 'ra', 'ሬ': 're', 'ር': 'r(ə)', 'ሮ': 'ro', 'ሰ': 'sä',
                    'ሱ': 'su', 'ሲ': 'si', 'ሳ': 'sa', 'ሴ': 'se', 'ስ': 's(ə)', 'ሶ': 'so', 'ሸ': 'šä', 'ሹ': 'šu', 'ሺ': 'ši',
                    'ሻ': 'ša', 'ሼ': 'še', 'ሽ': 'š(ə)', 'ሾ': 'šo', 'ቀ': 'ḳä', 'ቁ': 'ḳu', 'ቂ': 'ḳi', 'ቃ': 'ḳa', 'ቄ': 'ḳe',
                    'ቅ': 'ḳ(ə)', 'ቆ': 'ḳo', 'ቈ': 'ḳwä', 'ቊ': 'ḳwi', 'ቋ': 'ḳwa', 'ቌ': 'ḳwe', 'ቍ': 'ḳwə', 'ቐ': 'ḳʰä',
                    'ቑ': 'ḳʰu', 'ቒ': 'ḳʰi', 'ቓ': 'ḳʰa', 'ቔ': 'ḳʰe', 'ቕ': 'ḳʰ(ə)', 'ቖ': 'ḳʰo', 'ቘ': 'ḳʰwä', 'ቚ': 'ḳʰwi',
                    'ቛ': 'ḳʰwa', 'ቜ': 'ḳʰwe', 'ቝ': 'ḳʰwə', 'በ': 'bä', 'ቡ': 'bu', 'ቢ': 'bi', 'ባ': 'ba', 'ቤ': 'be',
                    'ብ': 'b(ə)', 'ቦ': 'bo', 'ቨ': 'vä', 'ቩ': 'vu', 'ቪ': 'vi', 'ቫ': 'va', 'ቬ': 've', 'ቭ': 'v(ə)',
                    'ቮ': 'vo', 'ተ': 'tä', 'ቱ': 'tu', 'ቲ': 'ti', 'ታ': 'ta', 'ቴ': 'te', 'ት': 't(ə)', 'ቶ': 'to', 'ቸ': 'čä',
                    'ቹ': 'ču', 'ቺ': 'či', 'ቻ': 'ča', 'ቼ': 'če', 'ች': 'č(ə)', 'ቾ': 'čo', 'ኀ': 'ḫä', 'ኁ': 'ḫu', 'ኂ': 'ḫi',
                    'ኃ': 'ḫa', 'ኄ': 'ḫe', 'ኅ': 'ḫ(ə)', 'ኆ': 'ḫo', 'ኈ': 'ḫwä', 'ኊ': 'ḫwi', 'ኋ': 'ḫwa', 'ኌ': 'ḫwe',
                    'ኍ': 'ḫwə', 'ነ': 'nä', 'ኑ': 'nu', 'ኒ': 'ni', 'ና': 'na', 'ኔ': 'ne', 'ን': 'n(ə)', 'ኖ': 'no',
                    'ኘ': 'ñä', 'ኙ': 'ñu', 'ኚ': 'ñi', 'ኛ': 'ña', 'ኜ': 'ñe', 'ኝ': 'ñ(ə)', 'ኞ': 'ño', 'አ': 'ʾä', 'ኡ': 'ʾu',
                    'ኢ': 'ʾi', 'ኣ': 'ʾa', 'ኤ': 'ʾe', 'እ': 'ʾ(ə)', 'ኦ': 'ʾo', 'ከ': 'kä', 'ኩ': 'ku', 'ኪ': 'ki', 'ካ': 'ka',
                    'ኬ': 'ke', 'ክ': 'k(ə)', 'ኮ': 'ko', 'ኰ': 'kwä', 'ኲ': 'kwi', 'ኳ': 'kwa', 'ኴ': 'kwe', 'ኵ': 'kwə',
                    'ኸ': 'xä', 'ኹ': 'xu', 'ኺ': 'xi', 'ኻ': 'xa', 'ኼ': 'xe', 'ኽ': 'x(ə)', 'ኾ': 'xo', 'ዀ': 'xwä',
                    'ዂ': 'xwi', 'ዃ': 'xwa', 'ዄ': 'xwe', 'ዅ': 'xwə', 'ወ': 'wä', 'ዉ': 'wu', 'ዊ': 'wi', 'ዋ': 'wa',
                    'ዌ': 'we', 'ው': 'w(ə)', 'ዎ': 'wo', 'ዐ': 'ʿä', 'ዑ': 'ʿu', 'ዒ': 'ʿi', 'ዓ': 'ʿa', 'ዔ': 'ʿe',
                    'ዕ': 'ʿ(ə)', 'ዖ': 'ʿo', 'ዘ': 'zä', 'ዙ': 'zu', 'ዚ': 'zi', 'ዛ': 'za', 'ዜ': 'ze', 'ዝ': 'z(ə)',
                    'ዞ': 'zo', 'ዠ': 'žä', 'ዡ': 'žu', 'ዢ': 'ži', 'ዣ': 'ža', 'ዤ': 'že', 'ዥ': 'ž(ə)', 'ዦ': 'žo', 'የ': 'yä',
                    'ዩ': 'yu', 'ዪ': 'yi', 'ያ': 'ya', 'ዬ': 'ye', 'ይ': 'y(ə)', 'ዮ': 'yo', 'ደ': 'dä', 'ዱ': 'du', 'ዲ': 'di',
                    'ዳ': 'da', 'ዴ': 'de', 'ድ': 'd(ə)', 'ዶ': 'do', 'ጀ': 'ǧä', 'ጁ': 'ǧu', 'ጂ': 'ǧi', 'ጃ': 'ǧa', 'ጄ': 'ǧe',
                    'ጅ': 'ǧ(ə)', 'ጆ': 'ǧo', 'ገ': 'gä', 'ጉ': 'gu', 'ጊ': 'gi', 'ጋ': 'ga', 'ጌ': 'ge', 'ግ': 'g(ə)',
                    'ጎ': 'go', 'ጐ': 'gwä', 'ጒ': 'gwi', 'ጓ': 'gwa', 'ጔ': 'gwe', 'ጕ': 'gwə', 'ጠ': 'ṭä', 'ጡ': 'ṭu',
                    'ጢ': 'ṭi', 'ጣ': 'ṭa', 'ጤ': 'ṭe', 'ጥ': 'ṭ(ə)', 'ጦ': 'ṭo', 'ጨ': 'č̣ä', 'ጩ': 'č̣u', 'ጪ': 'č̣i',
                    'ጫ': 'č̣a', 'ጬ': 'č̣e', 'ጭ': 'č̣(ə)', 'ጮ': 'č̣o', 'ጰ': 'p̣ä', 'ጱ': 'p̣u', 'ጲ': 'p̣i', 'ጳ': 'p̣a',
                    'ጴ': 'p̣e', 'ጵ': 'p̣(ə)', 'ጶ': 'p̣o', 'ጸ': 'ṣä', 'ጹ': 'ṣu', 'ጺ': 'ṣi', 'ጻ': 'ṣa', 'ጼ': 'ṣe',
                    'ጽ': 'ṣ(ə)', 'ጾ': 'ṣo', 'ፀ': 'ṣ́ä', 'ፁ': 'ṣ́u', 'ፂ': 'ṣ́i', 'ፃ': 'ṣ́a', 'ፄ': 'ṣ́e', 'ፅ': 'ṣ́(ə)',
                    'ፆ': 'ṣ́o', 'ፈ': 'fä', 'ፉ': 'fu', 'ፊ': 'fi', 'ፋ': 'fa', 'ፌ': 'fe', 'ፍ': 'f(ə)', 'ፎ': 'fo',
                    'ፐ': 'pä', 'ፑ': 'pu', 'ፒ': 'pi', 'ፓ': 'pa', 'ፔ': 'pe', 'ፕ': 'p(ə)', 'ፖ': 'po'}


def ti_transliterator(source_str):
    transliterated_string = ""
    original_string = ""
    non_ti_count = 0
    for i in source_str:
        if (i in phonetic_dict_ti):
            transliterated_string = transliterated_string + phonetic_dict_ti[i]
            original_string = original_string + i.rjust(len(phonetic_dict_ti[i]))
        else:
            transliterated_string = transliterated_string + i
            original_string = original_string + i
            if i != " ":
                non_ti_count += 1
            else:
                transliterated_string = transliterated_string + " "
    if non_ti_count > 0:
        print("\nWARNING: {} non Tigrinya characters found.".format(non_ti_count))

    return (transliterated_string, original_string, non_ti_count)


print(ti_transliterator('ነዊሕ'))
