from join_jamos import join_jamos, split_syllable_char, split_syllables

# 포만코드 대조표
phoman = {
    #     'ː' : ':',
    "n": "N",
    "b": "B",
    "z": "Z",
    "ɡ": "G",
    "t": "T",
    "ʌ": "^",
    "ə": "C",
    "ʊ": "U",
    "a": "A",
    "p": "P",
    "r": "R",
    "u": "U",
    "ŋ": "Q",  # 종성 'ㅇ'
    "h": "H",
    "v": "V",
    "ɑ": "A",
    "i": "!",
    "ʒ": "3",
    "x": "X",
    "ɔ": "O",
    "æ": "@",
    "d": "D",
    "l": "L",
    "ʃ": "#",
    "ð": "&",
    "j": "J",
    "ɜ": "C",
    "w": "W",
    "f": "F",
    "k": "K",
    "s": "S",
    "θ": "*",
    "m": "M",
    "e": "E",
    "ɪ": "!",
    "ɒ": "O",
}

# 자음부
consonant = {
    # 마찰음
    "S": "ㅅ",
    "*": "ㅅ",
    "#": "ㅅ",
    "Z": "ㅈ",
    "3": "ㅈ",
    "F": "ㅍ",
    "V": "ㅂ",
    "&": "ㄷ",
    # 무성 파열음
    "P": "ㅍ",
    "T": "ㅌ",
    "K": "ㅋ",
    # 파찰음
    "T#": "ㅊ",
    "TS": "ㅊ",
    "D3": "ㅈ",
    "DZ": "ㅈ",
    # 비음
    "M": "ㅁ",
    "N": "ㄴ",
    "Q": "ㅇ",  # 종성 'ㅇ'
    # 유성 파열음
    "B": "ㅂ",
    "D": "ㄷ",
    "G": "ㄱ",
    # 유음
    "L": "ㄹ",
    "R": "ㄹ",
    "H": "ㅎ",
    "-": "-",
}

# 모음부
vowel = {
    # 단모음
    "!": "ㅣ",
    "I": "ㅣ",
    "^": "ㅓ",
    "C": "ㅓ",
    "c": "ㅓ",
    "E": "ㅔ",
    "A": "ㅏ",
    "U": "ㅜ",
    "O": "ㅗ",
    # 이중모음
    "@": "ㅐ",
    "Q": "ㅚ",
    "OU": "ㅗ",
    "AUC": "ㅏ워",
    "UC": "ㅝ",
    # 반모음
    "W!": "ㅟ",
    "W^": "ㅝ",
    "WC": "ㅝ",
    "WE": "ㅞ",
    "WA": "ㅘ",
    "WU": "ㅜ",
    "WO": "ㅝ",
    "WOU": "ㅝ",
    "W@": "ㅙ",
    "J!": "ㅣ",
    "J^": "ㅕ",
    "JC": "ㅕ",
    "JE": "ㅖ",
    "JA": "ㅑ",
    "JU": "ㅠ",
    "JO": "ㅛ",
    "J@": "ㅒ",
}

double = {
    # 파찰음
    "TS": "ㅊ",
    "D3": "ㅈ",
    "DZ": "ㅈ",
    # 이중모음
    "OU": "ㅗ",
    "AUC": "ㅏ워",
    "UC": "ㅝ",
    # 반모음
    "W!": "ㅟ",
    "W^": "ㅝ",
    "WC": "ㅝ",
    "WE": "ㅞ",
    "WA": "ㅘ",
    "WU": "ㅜ",
    "WO": "ㅝ",
    "WOU": "ㅝ",
    "W@": "ㅙ",
    "J!": "ㅣ",
    "J^": "ㅕ",
    "JC": "ㅕ",
    "JE": "ㅖ",
    "JA": "ㅑ",
    "JU": "ㅠ",
    "JO": "ㅛ",
    "J@": "ㅒ",
}

monophthong = ["!", "I", "^", "C", "c", "E", "A", "U", "O"]

__HANGUL_CHOSEONG_FILLER_v__ = int('115F', 16)   # 'ᅟ'  (화면에 안 보임)
__HANGUL_CHOSEONG_FILLER__ =  'ᅟ' # 0x115F # (화면에 안 보임)
__HANGUL_JUNGSEONG_FILLER_v__ = int('1160', 16) # 'ᅠ' (화면에 안 보임)
__HANGUL_JUNGSEONG_FILLER__ = 'ᅠ' # 0x1160 # (화면에 안 보임)

__초성_채움__ = __HANGUL_CHOSEONG_FILLER__
__중성_채움__ = __HANGUL_JUNGSEONG_FILLER__
초성_채움 = __초성_채움__
중성_채움 = __중성_채움__

# 포만코드 변환
def get_phomanCode(word):
    phoman_lst = []

    for char in list(word):
        if char in phoman.keys():
            phoman_lst.append(phoman[char])

    return phoman_lst


def get_hangul(phomanCode: list):

    hangul_lst, previous_word = [], []
    phomanCode = get_phomanCode(phomanCode)
    print(f"Phoman Code : {phomanCode}\n")

    ####################################################################################
    print("".join(phomanCode[-1]))
    # 예외 1. 'R'의 경우 어말이나 자음 앞에서는 무시(묵음 처리)한다.
    # 무시 (묵음 처리)는 없애는 것이 아닌 듯
    if "".join(phomanCode[-1]) == "R":
        # phomanCode.pop()
        phomanCode[-1] = 중성_채움

    elif "R" in "".join(phomanCode):
        # print(phomanCode)
        idx = phomanCode.index("R")
        if phomanCode[idx + 1] in consonant.keys():
            del phomanCode[idx]

    # 어말이나 자음 앞에서 'TS'는 '츠'로 변환
    if "".join(phomanCode[-2:]) == "TS":
        phomanCode[-2:] = ["ㅊ", "ㅡ"]

    # 그 외 TS 는 'ㅊ'으로 변환
    elif "TS" in "".join(phomanCode):
        idx = phomanCode.index("T")
        phomanCode[idx : idx + 2] = "ㅊ"

    # 어말이나 자음 앞에서 'T#'은 '치'로 변환
    if "".join(phomanCode[-2:]) == "T#":
        phomanCode[-2:] = ["ㅊ", "ㅣ"]

    # 어말이나 자음 앞에서 'DZ'는 '즈'로 변환
    if "".join(phomanCode[-2:]) == "DZ":
        phomanCode[-2:] = ["ㅈ", "ㅡ"]

    # 그 외 'DZ'는 'ㅈ'으로 변환
    elif "DZ" in "".join(phomanCode):
        idx = phomanCode.index("D")
        phomanCode[idx : idx + 2] = "ㅈ"

    # 어말이나 자음 앞에서 'D3'은 '지'로 변환
    if "".join(phomanCode[-2:]) == "D3":
        phomanCode[-2:] = ["ㅈ", "ㅣ"]

    # 그 외 'D3'은 'ㅈ'으로 변환
    elif "D3" in "".join(phomanCode):
        idx = phomanCode.index("D")
        phomanCode[idx : idx + 2] = "ㅈ"

    # 'ㅊ' 변환
    if "T#" in "".join(phomanCode):
        idx = phomanCode.index("T")

        if phomanCode[idx + 2] == "!":
            phomanCode[idx : idx + 3] = "ㅊㅑ"
        elif phomanCode[idx + 2] == "^":
            phomanCode[idx : idx + 3] = "ㅊㅕ"
        elif phomanCode[idx + 2] == "E":
            phomanCode[idx : idx + 3] = "ㅊㅔ"
        elif phomanCode[idx + 2] == "A":
            phomanCode[idx : idx + 3] = "ㅊㅑ"
        elif phomanCode[idx + 2] == "U":
            phomanCode[idx : idx + 3] = "ㅊㅠ"
        elif phomanCode[idx + 2] == "O":
            phomanCode[idx : idx + 3] = "ㅊㅛ"
        elif phomanCode[idx + 2] == "@":
            phomanCode[idx : idx + 3] = "ㅊㅒ"
        elif phomanCode[idx + 2] in consonant.keys():
            phomanCode[idx : idx + 2] = "ㅊㅠ"

    # 'ㅅ' 변환
    if "#" in "".join(phomanCode):
        idx = phomanCode.index("#")

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

    if "".join(phomanCode[-1:]) == "#":
        phomanCode[-1:] = ["ㅣ"]

    # print("".join(phomanCode[0]))
    # if "".join(phomanCode[0]) in vowel.keys:
    #     phomanCode.insert(0, 'ㅇ')

    # 자음 처리부 : 어말이나 자음 앞에서는 중성 모음 'ㅡ'를 추가한다.
    # if "".join(phomanCode[-1:]) in consonant.keys():
    #     phomanCode.append("ㅡ")

    ####################################################################################

    rep_word = "".join(phomanCode)

    for con, vow in double.items():

        if con in rep_word:

            rep_word = rep_word.replace(con, vow)

    print(f"이중 모음 제거 : {rep_word}\n")

    ####################################################################################

    for pro in list(rep_word):

        # 자음부
        if pro in consonant.keys():

            try:
                # print(previous_word[-1])
                # print(f'pro : {pro}')
                # 0. 같은 자음 연속되면 삭제
                if consonant[pro] == hangul_lst[-1]:
                    hangul_lst.pop()

                # 2. 자음 앞에서는 '저'로 표기한다.
                if previous_word[-1] == "3":
                    hangul_lst.append("ㅓ")

                # 모음 처리부 : 종성 'ㅇ'의 뒤에서는 초성 'ㅇ'을 삽입한다.
                if previous_word[-1] == "Q":
                    hangul_lst.append("ㅇ")

                # 자음 처리부 : 자음 앞에서는 중성 모음 'ㅡ'를 추가한다.
                if hangul_lst[-1] in consonant.values():
                    hangul_lst.append("ㅡ")

                # 6-2. 'L' 이 모음이 따르지 않는 비음 앞에 올 때는 "ㄹㄹ"로 변환
                if previous_word[-1] in ["M", "N", "Q"] and pro == "L":
                    hangul_lst.append("ㄹ")
                    # hangul_lst.append("ㅡ")

                # 7. 단모음 다음의 어말 무성 파열음 ['P', 'T', 'K'] 은 각각 종성 ['ㅂ', 'ㅅ', 'ㄱ'] 으로 표기한다.
                if previous_word[-1] in monophthong:
                    if pro == "P":
                        consonant[pro] = "ㅂ"
                    if pro == "T":
                        consonant[pro] = "ㅅ"
                    if pro == "K":
                        consonant[pro] = "ㄱ"

            except:
                pass

            hangul_lst.append(consonant[pro])

        # 모음부
        elif pro in vowel.keys():

            # 모음 처리부 : 단어의 시작일 때 초성 'ㅇ'을 삽입
            if len(hangul_lst) == 0:
                hangul_lst.append("ㅇ")

            try:
                # 0. 같은 모음 연속되면 삭제
                if vowel[pro] == hangul_lst[-1]:
                    hangul_lst.pop()

                # 모음 처리부 : 모음의 뒤에서는 초성 'ㅇ'을 삽입
                if hangul_lst[-1] in vowel.values():
                    hangul_lst.append("ㅇ")

                # 6-2. 어중의 'L'이 모음 앞에 올 때 "ㄹㄹ"로 변환
                if len(hangul_lst) > 1 and previous_word[-2] == "L":
                    hangul_lst.append("ㄹ")

                """
                    'M' : 'ㅁ',
                    'N' : 'ㄴ',
                    'Q' : 'ㅇ', 
                """

            except:
                pass

            hangul_lst.append(vowel[pro])

        else:
            hangul_lst.append(pro)

        # print(pro)
        previous_word.append(pro)
    ####################################################################################

    print(split_syllables(hangul_lst))
    # return join_jamos(hangul_lst)

    # for hangul in list(hangul_lst):
    #     print(hangul)


if __name__ == "__main__":
    # text = "ˈænəlɪst"
    # text = "it"
    # text = "ˈmɑːdərnɪzəm"
    # text = "ˈwʌndərfl"
    # text = "əˈraɪvl"
    # text = 'ˌaʊtˈdɔːrz'
    # text = "ˈhɑːlədeɪ"
    # text = "ˈtʃaɪnə"
    # text = 'stɑːrt'
    # text = "ˈpɑːrti"
    # text = "dʒɔɪn"
    # text = "bi:t"
    # text = "ˈvɪʒn"
    # text = "laʊndʒ"
    # text = "ˈæʒər"
    text = "ˈriːdʒənt"
    # text = "ˈnætʃrəl"
    # text = "rɪtʃ"
    # text = "ɪts"
    # text = "ˈskɑːrlət"
    # text = "ˈflaʊər"
    # text = "əˈraɪvl"

    print(f"hangul : {get_hangul(text)}")
