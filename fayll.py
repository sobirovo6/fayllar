savol = input('malumot kiriting >>')
with open('fayl.txt','a') as fayl:
    fayl.write(savol+'\n')

def tugilgan_kun(tkun):
    with open('pi_million_digits (1) (1).txt') as fayl:
        pi = fayl.read().replace('\n','')


    if tkun in pi:
        return 'tugilgan kuningiz p soni tarkibida uchraydi'
    else:
        return 'tugilgan kuningiz p soni tarkibida uchramaydi'

tkun = '17111006'
pii = tugilgan_kun(tkun)
print(pii)