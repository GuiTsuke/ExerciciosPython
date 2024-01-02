print('QUAL O MAIOR NÚMERO?')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo npumero: '))
n3 = float(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    print('O primeiro é maior!')
else:
    if n1 < n2 and n2 > n3:
        print('O segundo é maior!')
    else:
        if n1 == n2 and n1 > n3:
            print('O primeiro e o segundo sao maiores')
        else:
            if n1 == n3 and n1 > n2:
                print('O primeiro e o terceiro sao maiores')
            else:
                if n1 == n2 and n1 == n3:
                    print('Todos são iguais!')
                else:
                    if n2 == n3 and n2 > n1:
                        print('O segundo e o terceiro são maiores!')
                    else:
                        print("O terceiro é maior!")


if n1 > n2 > n3:
    print('O maior é o primeiro {}'.format(n1))
    print('O menor é o terceiro {}'.format(n3))
else:
    if n2 > n1 > n3:
        print('O maior é o segundo {}'.format(n2))
        print('O menor é o terceiro {}'.format(n3))
    else:
        if n3 > n1 > n2:
            print('O maior é o terceiro {}'.format(n3))
            print('O menor é o segundo {}'.format(n2))
        else:
            if n3 > n2 > n1:
                print('O maior é o terceiro {}'.format(n3))
                print('O menor é o primeiro {}'.format(n1))
            if n2 > n3 > n1:
                print('O maior é o segundo {}'.format(n2))
                print('O menor é o primeiro {}'.format(n1))
            else:
                if n1 > n3 > n2:
                    print('O maior é o primeiro {}'.format(n1))
                    print('O menor é o segundo {}'.format(n2))
                else:
                    print('Digitou números iguais!')