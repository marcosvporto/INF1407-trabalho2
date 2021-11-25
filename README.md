# INF1407 Trabalho 2
## Marcos Vinícius Porto de Sá - 1413428
### Tema: Clube de Benefícios de uma Clínica

Nesse website os usuários podem ser funcionários da clínica, responsáveis pela gestão de clientes, de agendamentos e de planos de benefícios, ou podem ser pacientes/clientes da clínica.

Para os funcionários da clínica, devidamente cadastrados e autenticados,  é possível:
 - Cadastrar, Listar, Alterar e Deletar clientes
 - Cadastrar, Listar, Alterar e Deletar Planos de Benefícios
 - Cadastrar, Listar, Alterar e Deletar Agendamentos de Consultas
 - Associar um plano para cada cliente
 - Associar um cliente a um agendamento

Para um cliente/paciente, que não possui cadastro, é possível:
 - Se cadastrar como cliente/paciente
 - Buscar os agendamentos associados a si
 - Ter ou não associado a si um plano de benefícios, mediante ação de um funcionário autenticado


Para um Plano de Benefícios é possível:
 - Ter um nome
 - Ter uma porcentagem de desconto no valor das consultas

Área secreta do funcionário: Gestão da Clínica
 - ATUALIZAR SEUS DADOS
 - LISTAR CLIENTES
 - CADASTRAR NOVO CLIENTE
 - LISTAR PLANOS DE BENEFÍCIOS
 - CADASTRAR NOVO PLANO DE BENEFÍCIOS
 - LISTAR AGENDAS
 - CADASTRAR NOVA AGENDA

Caminhos mais usados
1. Cadastro e Login de Membro: Home Page -> Membros
2. Cadastro de Cliente pelo Cliente: Home Page -> Clientes -> Cliente Novo
3. Cadastro de Cliente pelo Funcionário Logado: Home Page -> Membros -> Cadastrar Novo Cliente
4. Cadastro de Plano de Benefícios: Home Page -> Membros ->  Cadastrar Novo Plano de Benefícios
5. Cadastro de Agenda: Home Page -> Membros ->  Cadastrar Nova Agenda
6. Retornar para a área de gestão da Clíca: Qualquer página acessada pelo Membro -> Gestão


Um fluxo possível
 - Cliente realiza o próprio cadastro sozinho
 - Funcionário se Cadastra e/ou faz o Login
 - Funionário busca o cadastro do cliente na lista de clientes, onde vê a opção de atualização
 - Funcionário associa ou não um plano de benefícios, na página de atualização de um cliente
 - Funcionário cadastra uma nova agenda (agendamento) e associa um cliente a esta agenda
 - Cliente busca seus agendamentos usando o numero do CPF
 - Cliente vê o custo da consulta já com o desconto aplicado pelo plano, caso haja

Outro fluxo possível (próximo ao que seria na realidade)
 - Funcionário já cadastrado faz o login
 - Funcionário cria várias agendas da semana atual e das próximas
 - Clientes consultam agendas abertas e solicitam agendamento
 - Funcionário associa clientes já cadastrados as agendas conforme solicitação dos mesmos
 - Clientes solicitam upgrade ou downgrade do plano de benefícios
 - Funcionário atualiza o agendamento para que o novo desconto seja aplicado

Onde foi utilizado AJAX:

Clientes podem consultar seus agendamentos apenas digitando seu CPF












