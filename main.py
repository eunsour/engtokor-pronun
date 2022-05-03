# 포만코드 대조표

phoman = {
    'ː' : ':',
    'n' : 'N',
    'b' : 'B',
    'z' : 'Z',
    'ɡ' : 'G',
    
    't' : 'T',
    'ʌ' : '^',
    'ə' : 'C',
    'ʊ' : 'C',
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
    'v' : 'ㅂ',
    '&' : 'ㄷ',
    
    # 무성 파열음
    'P' : 'ㅍ',
    'T' : 'ㅌ',
    'K' : 'ㅋ',
    
    # 파찰음
    'TS' : 'ㅊ',
    'T#' : 'ㅊ',
    'D3' : 'ㅈ',
    'DZ' : 'ㅈ',
    
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
    char_lst = []
    for char in list(text):    
        if char in phoman.keys():
            char_lst.append(phoman[char])
            
    return char_lst

def get_hangul(text):
    hangul_lst = []

    for pro in get_phoman(text):
        
        # 자음부 
        if pro in consonant.keys():
            hangul_lst.append(consonant[pro])
            
        # 모음부
        if pro in vowel.keys():
            hangul_lst.append(vowel[pro])

    return hangul_lst

if __name__ == "__main__":
    text = 'ɔɪl'

    print(get_hangul(text=text))