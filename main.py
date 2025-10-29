from Data import Data
from Funcionario import Funcionario
from Estudante import Estudante
from Pessoa import Pessoa
from Professor import Professor

f1 = Funcionario(nome = 'Alice',
                 escritorio=2424,
                 salario=3000,
                 admissao= Data(15,12,2025))

p1 = Professor(nome = 'Ronaldo',
                 escritorio=2424,
                 salario=3000,
                 admissao= Data(15,12,2025),
                 qtd_ha=32,
                 qtd_pe=10)

print(f1.informaDescricao())
print(p1.informaDescricao())