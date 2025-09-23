prod1= input("nombre del produto:")
vendAnu= float(input("vendas anuais:"))

if vendAnu <= 100:
    print("baixo")
elif vendAnu > 100 and vendAnu<= 500:
    print("medio")
elif vendAnu > 500 and vendAnu<= 1000:
    print("alto")
elif vendAnu > 1000:
    print("primeira necesidade")
