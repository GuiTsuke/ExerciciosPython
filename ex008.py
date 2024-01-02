metros = float(input('Digite um valor em metros: '))
cent = metros * 100
mili = metros * 1000
deci = metros * 10
deca = metros / 10
heca = metros / 100
kilo = metros / 1000
print('A medida de {}m corresponde a \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(metros, kilo, heca, deca, deci, cent, mili))
print('A medida de {}m corresponde a \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(metros, metros / 1000, metros / 100, metros / 10, metros * 10, metros * 100, metros * 1000))

