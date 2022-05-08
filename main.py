# 포만코드 대조표

phoman = {
#     'ː' : ':',
    'n' : 'N',
    'b' : 'B',
    'z' : 'Z',
    'ɡ' : 'G',
    
    't' : 'T',
    'ʌ' : '^',
    'ə' : 'C',
    'ʊ' : 'U',
    'a' : 'A',
    
    'p' : 'P',
    'r' : 'R',
    'u' : 'U',
    'ŋ' : 'Q',  # 종성 'ㅇ'
    'h' : 'H',
    
    'v' : 'V',
    'ɑ' : 'A',
    'i' : '!',
    'ʒ' : '3',
    'x' : 'X',
    
    'ɔ' : 'O',
    'æ' : '@',
    'd' : 'D',
    'l' : 'L',
    'ʃ' : '#',
    
    'ð' : '&',
    'j' : 'J',
    'ɜ' : 'C',
    'w' : 'W',
    'f' : 'F',
    
    'k' : 'K',
    's' : 'S',
    'θ' : '*',
    'm' : 'M',
    'e' : 'E',
    
    'ɪ' : '!',
    'ɒ' : 'O'
}

# 자음부
consonant = {
    # 마찰음
    'S' : 'ㅅ',
    '*' : 'ㅅ',
    '#' : 'ㅅ',
    'Z' : 'ㅈ',
    '3' : 'ㅈ',
    'F' : 'ㅍ',
    'V' : 'ㅂ',
    '&' : 'ㄷ',
    
    # 무성 파열음
    'P' : 'ㅍ',
    'T' : 'ㅌ',
    'K' : 'ㅋ',
    
    # 파찰음
    'T#' : 'ㅊ',

    # 비음 
    'M' : 'ㅁ',
    'N' : 'ㄴ',
    'Q' : 'ㅇ', # 종성 'ㅇ'
    
    # 유성 파열음
    'B' : 'ㅂ',
    'D' : 'ㄷ',
    'G' : 'ㄱ',
    
    # 유음
    'L' : 'ㄹ',
    'R' : 'ㄹ',
    
    'H' : 'ㅎ'
}

# 모음부
vowel = {
    # 단모음 
    '!' : 'ㅣ',
    'I' : 'ㅣ',
    '^' : 'ㅓ',
    'C' : 'ㅓ',
    'c' : 'ㅓ',
    'E' : 'ㅔ',
    'A' : 'ㅏ',
    'U' : 'ㅜ',
    'O' : 'ㅗ',
    
    # 이중모음
    '@' : 'ㅐ',
    'Q' : 'ㅚ',
}

double = {
     # 파찰음
    'TS' : 'ㅊ',
    'D3' : 'ㅈ',
    'DZ' : 'ㅈ',

    # 이중모음
    'OU' : 'ㅗ',
    'AUC' : 'ㅏ워',
    'UC' : 'ㅝ',
    
    # 반모음
    'W!' : 'ㅟ',
    'W^' : 'ㅝ',
    'WC' : 'ㅝ',
    'WE' : 'ㅞ',
    'WA' : 'ㅘ',
    'WU' : 'ㅜ',
    'WO' : 'ㅝ',
    'WOU' : 'ㅝ',
    'W@' : 'ㅙ',
    'J!' : 'ㅣ',
    'J^' : 'ㅕ',
    'JC' : 'ㅕ',
    'JE' : 'ㅖ',
    'JA' : 'ㅑ',
    'JU' : 'ㅠ',
    'JO' : 'ㅛ',
    'J@' : 'ㅒ',
    
}

# 포만코드 변환
def get_phoman(text):
    phoman_lst = []

    for char in list(text):
        if char in phoman.keys():
            phoman_lst.append(phoman[char])
    return phoman_lst

def get_hangul(text):
    hangul_lst = []

    text = get_phoman(text)
    print(text)

    # 어말이나 자음 앞에서 'TS'는 '츠'로 변환
    if ''.join(text[-2:]) == 'TS':
        text[-2:] = ['ㅊ', 'ㅡ']
        
    # 그 외 TS 는 'ㅊ'으로 변환
    elif 'TS' in ''.join(text):
        idx = text.index("T")
        text[idx : idx + 2] = 'ㅊ'

    # 어말이나 자음 앞에서 'T#'은 '치'로 변환
    if ''.join(text[-2:]) == 'T#':
        text[-2:] = ['ㅊ', 'ㅣ']
        
    # 그 외 'T#'은 'ㅊ'으로 변환    
    elif 'T#' in ''.join(text):
        idx = text.index("T")
        text[idx : idx + 2] = 'ㅊ'
        
    # 어말이나 자음 앞에서 'DZ'는 '즈'로 변환
    if ''.join(text[-2:]) == 'DZ':
        text[-2:] = ['ㅈ', 'ㅡ']
        
    # 그 외 'DZ'는 'ㅈ'으로 변환    
    elif 'DZ' in ''.join(text):
        idx = text.index("D")
        text[idx : idx + 2] = 'ㅈ'
        
    # 어말이나 자음 앞에서 'D3'은 '지'로 변환
    if ''.join(text[-2:]) == 'D3':
        text[-2:] = ['ㅈ', 'ㅣ']
        
    # 그 외 'D3'은 'ㅈ'으로 변환    
    elif 'D3' in ''.join(text):
        idx = text.index("D")
        text[idx : idx + 2] = 'ㅈ'

    rep_word = ''.join(text)
    
    for con, vow in double.items():

        if con in rep_word:

            rep_word = rep_word.replace(con, vow)

    print(f'\n이중 모음 제거 : {rep_word}')
    
    for pro in list(rep_word):
        
        # 자음부
        if pro in consonant.keys():

            try:
                # 같은 자음 연속되면 삭제
                if consonant[pro] == hangul_lst[-1]:
                    hangul_lst.pop()

                # 2. 자음 앞에서는 '저'로 표기한다.
    #             if hangul_lst[-1] == 'ㅈ':
    #                 hangul_lst.append('ㅓ')

                # 자음 앞에서는 중성 모음 'ㅡ'를 추가한다.
    #             if hangul_lst[-1] in consonant.values():
    #                 hangul_lst.append('ㅡ')
                
                if hangul_lst[-1] == "ㅅ" and pro == "N":
                    hangul_lst.append("ㅕ")
                    
                # 6-2. 모음이 따르지 않는 비음 앞에 올 때는 "ㄹㄹ"로 변환
                if hangul_lst[-1] == "ㄹ" and pro in ["M", "N", "Q"]:
                    hangul_lst.append("ㄹ")
                    hangul_lst.append("ㅡ")
                    
            except:
                pass

            hangul_lst.append(consonant[pro])
            

        # 모음부
        elif pro in vowel.keys():

            # 단어의 시작이거나, 종성 'ㅇ' 일 때 초성 'ㅇ'을 삽입
            if len(hangul_lst) == 0:
                hangul_lst.append('ㅇ')

            
            try:
                # 같은 모음 연속되면 삭제
                if vowel[pro] == hangul_lst[-1]:
                    hangul_lst.pop()
                    
                # 모음의 뒤에서는 초성 'ㅇ'을 삽입
                if hangul_lst[-1] in vowel.values():
                    hangul_lst.append('ㅇ')
                
                # 6-2. 어중의 'L'이 모음 앞에 올 때 "ㄹㄹ"로 변환
                if hangul_lst[-1] == "ㄹ":
                    hangul_lst.append("ㄹ")
                    
                '''
                    'M' : 'ㅁ',
                    'N' : 'ㄴ',
                    'Q' : 'ㅇ', 
                '''


            except:
                pass

            hangul_lst.append(vowel[pro])

        else:
            hangul_lst.append(pro)
        
    return hangul_lst

if __name__ == "__main__":
    text = 'ɔɪl'

    print(get_hangul(text))