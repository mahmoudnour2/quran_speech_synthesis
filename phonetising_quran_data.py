from text import arabic_to_buckwalter as func
import text

def buckwalter_to_phonemes(buck):
    phonemes = text.buckwalter_to_phonemes(buck)
    return phonemes
count=0
for i in range(1, 6237):
    with open('lab_files_bw/verse_{}_bw.lab'.format(i), 'r', encoding='utf-8') as f:
        try:
            lines = f.readlines()
            buck = lines[0]
            phonemes = buckwalter_to_phonemes(buck)
            print(phonemes)
            with open('phones/verse_{}_phon.lab'.format(i), 'w', encoding='utf-8') as f:
                f.write(phonemes)
        except:
            count=count+1
            print('Error in verse {}'.format(i))
print(count)