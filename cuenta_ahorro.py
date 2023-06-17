
from cuenta_bancaria import Cuenta_Bancaria

class Cuenta_ahorro (Cuenta_Bancaria):
    def __init__(self, interes: float= 0, numero= None, nombrepropietario= None, saldo:float=0):
        self._interes = interes
        super(Cuenta_ahorro, self).__init__(numero=numero, nombrepropietario=nombrepropietario, saldo=saldo)

        @property
        def interes(self):
            return self._interes

        @interes.setter
        def interes(self, interes):
            self._interes = interes


        def pagar_interes(self):
            self._saldo = self._saldo + ((int(self._saldo) * int(self._interes))/100)
            return self._saldo
if __name__ == '__main__':
            cuentas_ahorros = Cuenta_ahorro (8,'092940452', 'Marjorie', 5200)

            cuentas_ahorros.mostrar_saldo()
            cuentas_ahorros.credito(15000)

            cuentas_ahorros.mostrar_saldo()
            cuentas_ahorros.debito(500)

            print(cuentas_ahorros)