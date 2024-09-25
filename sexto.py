num_placa = input("digite o numero final da placa: ")
# o match vai funcionar como o swtch que aprendemos em C
match num_placa:
    case "1" | "2": print("rodizio na segunda feira")
    case "3" | "4": print("rodizio na terça feira")
    case "5" | "6": print("rodizio na quarta feira")
    case "7" | "8": print("rodizio na quinta feira")
    case "9" | "0": print("rodizio na sexta feira")
    case _: print("final invalido")