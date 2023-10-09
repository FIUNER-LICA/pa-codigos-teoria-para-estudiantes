import argparse

parser = argparse.ArgumentParser(description='Procesar algunos enteros.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))

# uso correcto para mostrar el mayor de la lista:   python argparse_programa_1 5 6 7 1
# uso incorrecto porque se pasa una letra:          python argparse_programa_1 a
# uso para sumar algunos valores:                   python argparse_programa_1 --sum 1 2 3 4