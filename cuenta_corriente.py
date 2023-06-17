
from cuenta_bancaria import Cuenta_Bancaria

class Cuenta_corriente (Cuenta_Bancaria):
    def __init__(self, numero= None, nombrepropietario= None, saldo:float= 0, tiene_Cheque=bool):
        self._tiene_Cheque= tiene_Cheque
        super(Cuenta_corriente, self).__init__(numero=numero, nombrepropietario=nombrepropietario, saldo=saldo)

    @property
    def tiene_Cheque(self):
        return self._tiene_Cheque

    @tiene_Cheque.setter
    def tiene_Cheque(self, tiene_Cheque):
        self.tiene_Cheque = tiene_Cheque
        return self._saldo

    def pagar_cheque(self):
        self._saldo = self._saldo + ((int (self._saldo) - int (self._pagar_cheque)))
        return self._saldo

if __name__=='__main__':
    cuentas_corrientes = Cuenta_corriente('091020653', 'MARJORIE', 4300, bool)

    cuentas_corrientes.mostrar_saldo()
    cuentas_corrientes.credito(4850)

    cuentas_corrientes.mostrar_saldo()
    cuentas_corrientes.debito(850)
    print(cuentas_corrientes)