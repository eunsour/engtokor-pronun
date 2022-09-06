from utils.jamo import join_jamos, split_syllable_char, split_syllables
from utils.phoman_code import *


def get_phomanCode(word: str):
    phoman_lst = []

    for char in list(word):
        if char in phoman.keys():
            phoman_lst.append(phoman[char])

    return phoman_lst



def get_hangul(input_text: str):
    hangul_lst = []
    input_text = input_text.replace("ˌ", "").replace("ˈ", "")
    phomanCode = ''.join(get_phomanCode(input_text))

    print(f"포만 코드 : {phomanCode}, {type(phomanCode)}\n")

#############################################################################

    # 어말이나 자음 앞에서 'TS'는 '츠'로 변환
    if phomanCode[-2:] == "TS":
        phomanCode = phomanCode.replace(phomanCode[-2:], "츠")


    # 어말이나 자음 앞에서 'T#'은 '치'로 변환
    if phomanCode[-2:] == "T#":
        phomanCode = phomanCode.replace(phomanCode[-2:], "치")


    # 어말이나 자음 앞에서 'DZ'는 '즈'로 변환
    if phomanCode[-2:] == "DZ":
        phomanCode = phomanCode.replace(phomanCode[-2:], "즈")

    # 어말이나 자음 앞에서 'D3'은 '지'로 변환
    if phomanCode[-2:] == "D3":
        phomanCode = phomanCode.replace(phomanCode[-2:], "지")

#############################################################################

    if phomanCode[-1:] == "#":
        phomanCode = phomanCode.replace(phomanCode[-1:], "ㅣ")
        # phomanCode[-1:] = ["ㅣ"]

    # 'ㅅ' 변환
    elif "#" in "".join(phomanCode):
        idx = phomanCode.index("#")

        change_to = {'#!': '샤','#^': '셔','#E':'세', '#A': '샤', '#U': '슈', '#O': '쇼', '#@': '섀'}

        if phomanCode[idx + 1] == "!":
            phomanCode[idx + 1] = "ㅑ"
        elif phomanCode[idx + 1] == "^":
            phomanCode[idx + 1] = "ㅕ"
        elif phomanCode[idx + 1] == "E":
            phomanCode[idx + 1] = "ㅔ"
        elif phomanCode[idx + 1] == "A":
            phomanCode[idx + 1] = "ㅑ"

        elif phomanCode[idx + 1] == "U":
            phomanCode[idx + 1] = "ㅠ"
        elif phomanCode[idx + 1] == "O":
            phomanCode[idx + 1] = "ㅛ"
        elif phomanCode[idx + 1] == "@":
            phomanCode[idx + 1] = "ㅒ"
        elif phomanCode[idx + 1] in consonant.keys():
            phomanCode[idx + 1] = "ㅠ"




#############################################################################

    for chr in phomanCode:

        # 자음부
        if chr in consonant.keys():
            hangul_lst.append(consonant[chr])

        # 모음부
        elif chr in vowel.keys():
            hangul_lst.append(vowel[chr])
        
        else:
            hangul_lst.append(chr)


    return join_jamos(hangul_lst)

#############################################################################

if __name__ == "__main__":
    # text = "ˌedʒuˈkeɪʃn"
    # text = "ˌfæts"
    # text = "ˈbrɪtɪʃ"
    text = "ʃiːld"

    print(f"결과 : {get_hangul(text)}")