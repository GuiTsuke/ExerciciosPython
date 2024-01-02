from datetime import date
print('ANO BISSEXTO')
an = int(input('Digite um ano qualquer: '))
if an == 0:
    an = date.today().year

if an % 4 == 0 and an % 100 != 0 or an % 400 == 0:
    print('O ano de {} é bissexto e possui 366 dias!'.format(an))
else:
    print('O ano de {} não é bissexto e possui 365 dias!'.format(an))

#if an % 4 == 0:
#   if an % 100 == 0:
#        if an % 400 == 0:
#           print('O ano de {} é bissexto e possui 366 dias!'.format(an))
#        else:
#            print('O ano de {} não é bissexto e possui 365 dias!'.format(an))
#    else:
#        print('O ano de {} é bissexto e possui 366 dias!'.format(an))
#else:
#    print('O ano de {} não é bissexto e possui 365 dias!'.format(an))