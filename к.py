case1
kun = int(input('hafta kun kiriting>>'))
match kun:
    case 1:
        print('dushanba')
    case 2:
        print('seshanba'
    case 3:
        print('chorshanba')
    case 4:
        print('payshanba')
    case 5:
        print( 'juma')
    case 6:
        print('shanba')
    case 7:
        print('yakshanba')
    case _:
        print('bunday hafta kun yoq')

case2
baho = int(input('k='))
match baho:
    case 1:
        print('yomon')
    case 2:
        print('qoniqarsiz')
    case 3:
        print('qoniqarli')
    case 4:
        print('yaxshi')
    case 5:
        print("A'lo")
    case _:
        print('xato')

case3
oy = int(input('oy raqamini kiriting>>'))
match oy:
    case 12|1|2:
        print('Qish')
    case 3 | 4 | 5:
        print('bahor')
    case 6 | 7 | 8:
        print('yoz')
    case 9 | 10 | 11:
        print('kuz')
    case _:
        print('xato!')

case4
oy = int(input('oy raqamini kiriting>>'))
match oy:
    case 12|1|3|5|7|8|10:
        print('bu oyda 31 kun bor')
    case  4 | 6|9|11:
        print('bu oyda 30 kun bor')
    case 2:
        print('bu oyda 28kun bor')
    case _:
        print('Xato!')

case5
def arifmetik_amallar(a,b,amal):
    match amal:
        case 1:
            return a + b
        case 2:
            return a - b
        case 3:
            if b != 0:
                return a / b
            else:
                return '0 ga bolib bolmaydi'
        case 4:
            return a * b
        case _:
            return "notog'ri amal"

a = int(input('A sonini kiriting'))
b = int(input('B sonini kiriting'))
amal = int(input('amal tanlang , 1-qoshish, 2-ayirish, 3-bolish, 4-kopaytma '))

natija = arifmetik_amallar(a,b,amal)
print(natija)

k = int(input('k='))
birliklar = k%10
onliklar =k// 10%10

birliklar_text = ''
onliklar_text = ''
def num_text(n):
    text =''
    match n:
        case 1:
            text='bir'
        case 2:
            text = 'ikki'
        case 3:
            text = 'uch'
        case 4:
            text = 'tort'
        case 5:
            text = 'besh'
        case 6:
            text = 'olti'
        case 7:
            text = 'yetti'
        case 8:
            text = 'sakkiz'
        case 9:
            text = 'toqqiz'
    return text

birliklar_text=num_text(birliklar)
match onliklar:
    case 1:
        onliklar_text="o'n"
    case 2:
        onliklar_text = "yigirma"
    case 3:
        onliklar_text = "ottiz"
    case 4:
        onliklar_text = "qirq"
    case 5:
        onliklar_text = "ellik"
    case 6:
        onliklar_text = "oltmish"
    case 7:
        onliklar_text = "yetmish"
    case 8:
        onliklar_text = "sakson"
    case 9:
        onliklar_text= 'toqson'

print(onliklar_text, birliklar_text,'inchi masala')
