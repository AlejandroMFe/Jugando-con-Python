import sys

print(f"Nombre del Script: {sys.argv[0]}")

# sys.argv devuelve una lista con todos los
# argumentos que le pasemos al script
# al momento de ejecutarlo.
# por ejemplo: test_sys_argv.py hola que tal son argumentos
for arg in sys.argv[1:]:
    print(f"Argumentos: {arg}")
