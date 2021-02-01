class Banco():
    logo = None
    monto = None
    sucursal = None
    saldo = None
    informacion = None
    usuario = None
    contraseña = None
    numero_cuenta = None
    numero_cliente = None
    tarjeta = None
    
    
    def __init__(self):
        print ("Clase BBVA Bancomer")
    def Pagar(self):
        print("Atravez de cajero")
    def Depositar(self):
        print("Cuentas o servisios")
    def Retirar(self):
        print("Cajero o ventanilla")
    def Cuenta(self):
        print("Tener cuenta digital")
    def Operaciones(self):
        print("transferencia, pagar servicios extra")




BBVA= Banco()
BBVA.logo=("Azul y blanco")
BBVA.monto=("sin limite")
BBVA.sucursal=("Bancomer")
BBVA.saldo=("$200")
BBVA.informacion=("Brandon Osmar Pazos")
BBVA.usuario=("Brandon")
BBVA.contraseña=("osmar123")
BBVA.numero_cuenta=("1720110318")
BBVA.numero_cliente=("845")
BBVA.tarjeta=("4526 4857 7849 2541")



print(BBVA.logo)
print(BBVA.monto)
print(BBVA.sucursal)
print(BBVA.saldo)
print(BBVA.informacion)
print(BBVA.usuario)
print(BBVA.contraseña)
print(BBVA.numero_cuenta)
print(BBVA.numero_cliente)
print(BBVA.tarjeta)

