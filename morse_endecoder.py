letters = {
    'a':'01',
    'b':'1000',
    'c':'1010',
    'd':'100',
    'e':'0',
    'f':'0010',
    'g':'110',
    'h': '0000',
    'i':'00',
    'j':'0111',
    'k':'101',
    'l': '0100',
    'm':'11',
    'n':'10',
    'o':'111',
    'p':'0110',
    'q': '1101',
    'r':'010',
    's':'000',
    't':'1',
    'u':'001',
    'v':'0001',
    'w':'011',
    'x':'1001',
    'y':'1011',
    'z':'1100',
    ' ':'  ',
    '.':'.',
    '?':'?',
    '!':'!',
    ',':','
}

reversed_letters = dict((y,x) for x,y in letters.items())
reversed_letters['']=''

#encode
def encode(text):
    text = text.lower()
    encoded = ''

    for i in text:
        encoded += letters[i] 
        encoded += ' '

    return encoded

#decode
def decode(text):
    # text = input('Enter encoded text for decoding: ').split('   ')
    text = text.split('   ')
    decoded = ''

    for i in text:
        let = i.split()
        for m in let:
            decoded += reversed_letters[m]
        decoded += ' '

    return decoded




if __name__=='__main__':
    inp = int(input('For encode press 1 and for decode press 2\n'))
    if inp == 1:
        text = input('Enter normal text for encoding: ')
        x = encode(text)
        print(x)
    elif inp ==2:
        text = input('Enter encoded text for decoding: ')
        x = decode(text)
        print(x)
    else:
        print('try again')
