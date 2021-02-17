import sys
import os
import txt_processing as tp

def main():
    #give the pdf directory path for pdf_to_text.py
    tsv_path = sys.argv[1]

    #run through files in a directory
    for file in os.listdir(tsv_path):

        #get filename
        filename = file[:file.rindex(".")]
        if not f'{filename}.txt' in os.listdir('data/texts/'):
            #convert pdf to text file
            text = tp.convert_pdf_to_string(f'{tsv_path}/{file}')

            #write file in to text directory
            with open(f'data/texts/{filename}.txt', 'w') as txt_file:
                txt_file.write(text.encode('utf-8').decode('utf-8'))

if __name__ == "__main__":
    main()