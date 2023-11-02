class Pessoa:
    def _init_(self,N, I, P, comida):
        self.nome=N
        self.peso=P
        self.idade=I
        self.comida=comida
        self.comendo=False
        self.andando=False
        self.dormindo=False
        self.andarcomendo = False
        self.andardormindo = False

    def andar(self):
        if self.andando == False:
            self.andando = True
            print(f"{self.nome}  está andando.")
        else:
            print(f"{self.nome} já está andando.")

    def pararAndar(self):
        if self.andando:
            print(f"{self.nome} se cansou e parou de andar.")
            self.andando = False
        else:
            print(f"{self.nome} não está andando mais.")

    def comer(self):
        if self.comendo==False:
            self.comendo=True
            print(f"{self.nome} está comendo {self.comida}, humm, delicia!")
        else:
            print("Já está comendo")
    def pararcomer(self):
        if self.comendo==True:
            print(f"{self.nome} ficou cheio e parou de comer")
        else:
            print(f"{self.nome} ficou cheio e parou de comer")

    def andarComendo(self):
        if self.comendo == True:
            if self.andarcomendo == False:
                self.andarcomendo = True
                print(f"{self.nome} está comendo e não pode andar.")
        else:
            print(f"{self.nome} não está comendo.")

    def dormir(self):
        if self.dormindo == False:
            self.dormindo = True
            print(f"{self.nome} estava com muito sono e dormiu.")
        else:
            print(f"{self.nome} já está dormindo.")

    def andarDormindo(self):
        if self.dormindo == True:
            if self.andardormindo == False:
                self.andardormindo = True
                print("Está dormindo e não pode andar.")
        else:
            print("Não está dormindo.")

    def acordar(self):
        if self.dormindo:
            print(f"{self.nome} acordou do seu belo sono.")
            self.dormindo = False
        else:
            print(f"{self.nome} não está dormindo mais")


