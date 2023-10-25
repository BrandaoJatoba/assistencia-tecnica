# Sistema para Assistência Técnica

 Trabalho referente a 2ª Unidade avaliativa da matéria Projeto de Programação
### Colaboradores: João Felipe Brandão Jatobá, João Victor Araujo, Lucas Beltrão


## 1. Indrodução
### 1.1 Propósito

O presente documento de projeto de software descreve o sistema do projeto de um sistema de gerenciamento de ordem de serviços criado para ser utilizado por empresas prestadoras de serviço de Assistência Técnica.

### 1.2 Escopo

No mercado de prestação de serviços, o controle sobre as atividades e o gerenciamento de bens é essencial para um efetivo trabalho. A importância desse controle é proporcional a demanda, e dessa forma, quanto maior a quantidade de serviços realizados, maior as chances de enganos e conflitos por parte dos profissionais envolvidos. 
Neste contexto, assistências técnicas de equipamentos eletrônicos recebem clientes diariamente e necessitam de um preciso controle, afinal de contas, lhes são confiados pertences alheios possivelmente caros e queridos de seus solicitantes. Nesse caso, é essencial que esse trabalho não seja feito de qualquer forma, se faz necessário então um sistema que consiga monitorar tudo que acontece no estabelecimento. 

## 2. VISÃO GERAL DO SISTEMA

Neste sistema, a função principal será o cadastro de Ordens de Serviço com descrição do serviço a ser realizado. Além disso, será implementado subsistemas para cadastro do corpo técnico da empresa e dos clientes, além de um registro de atualizações para cada ordem de serviço emitida, de forma a refletir o atual status do equipamento em questão.
Os técnicos serão separados conforme suas especialidades, seja em telefones e tablets ou computadores e notebooks, além de suas credenciais. 
Os clientes precisarão ser cadastrados no sistema, sendo fornecido os seguintes dados: nome, CPF, número de telefone e o equipamento. 
Os equipamentos também serão cadastrados, sendo registrados os respectivos donos, técnicos responsáveis e número de série.

## 3. Funcionalidades não implementadas

###  Na GUI, a opção de desativar um técnico
###  Na GUI, a opção de apagar um item do banco de dados (comentário de uma ordem de serviço, por exemplo)
###  Filtragem de input de CPF válido
###  GUI encontra-se em funções, quando poderiam ser Classes.
