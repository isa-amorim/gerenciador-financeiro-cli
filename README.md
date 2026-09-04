# Gerenciador Financeiro CLI

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-projeto%20funcional-brightgreen)

Aplicação prática em linha de comando (CLI — interface de texto por terminal) desenvolvida para controle de fluxo de caixa pessoal e simulações financeiras. O projeto foi construído para resolver a dor de inconsistências de dados e falta de previsibilidade no saldo, aplicando validações rigorosas que impedem o programa de fechar por erros de digitação do usuário.

---

## 📌 O que a Aplicação Faz na Prática

* **Tela de Acesso Protegida:** Controle de acesso por senha numérica (PIN) com bloqueio automático após 3 tentativas incorretas, prevenindo acessos não autorizados.
* **Gestão de Fluxo de Caixa:** Registro categorizado de entradas (**Receitas**) e saídas (**Despesas**) com atualização do saldo final em tempo real.
* **Limpeza Automática de Dados:** Padronização de textos digitados (remoção de espaços sobressalentes e conversão para maiúsculas) para evitar duplicação de categorias no histórico.
* **Relatório e Extrato Filtrado:** Visualização detalhada das transações com suporte a filtros dinâmicos por tipo de operação.
* **Simulador Fintech (Calculadora de Juros):** Projeção de rendimentos futuros sobre o saldo ativo aplicando a fórmula de juros compostos $M = P \cdot (1 + i)^t$.

---

## 🛠️ Conhecimentos e Tecnologias Aplicadas

* **Linguagem Utilizada:** Python 3.10+
* **Estrutura e Organização do Código:**
  * **Encapsulamento (técnica de proteção que junta os dados e as regras do sistema):** Uso da Classe `SistemaFinanceiro` para organizar o estado da aplicação e eliminar o antipadrão de uso de variáveis globais (dados soltos que causam bugs).
  * **Desacoplamento de Responsabilidades:** Separação entre a regra de cálculo do sistema e a camada de visualização de texto no terminal.
  * **Tipagem de Dados (Type Hints):** Declaração explícita dos tipos de entrada e saída nos métodos para aumentar a legibilidade e facilidade de manutenção.
* **Tratamento de Exceções:** Validação defensiva no recebimento de dados numéricos para evitar que erros de digitação façam a aplicação parar de funcionar (`Crash`).

---

## 🏗️ Estrutura Atual do Repositório

```text
gerenciador-financeiro-cli/
│
├── LICENSE        # Termo de licença de uso livre do código (MIT)
├── README.md      # Documentação e manual explicativo do projeto
└── main.py        # Código-fonte completo com a regra de negócio e interface CLI
```

## 🚀 Como Executar o Projeto na Sua Máquina
**Pré-requisitos:**

- Python 3.10 ou superior instalado na máquina.

- Git (ferramenta para controle e download de versões de código).

## Passo a Passo
1. Baixe o projeto (Clone o repositório):
```
git clone https://github.com/isa-amorim/gerenciador-financeiro-cli.git
cd gerenciador-financeiro-cli
```

2. Execute a aplicação diretamente:
```
python main.py
```
*(Caso esteja no Linux ou macOS, utilize python3 main.py)*

| Senha padrão para acesso: 1234

## 📊 Decisões de Construção do Código
- Segurança de Estado: A escolha por encapsular o saldo e o histórico dentro da Classe SistemaFinanceiro foi feita para impedir alteração indevida de dados por funções externas.

- Sanitização de Dados: O tratamento de strings padroniza entradas como " alimentacao " para "ALIMENTACAO", mantendo os dados consolidados.

- Experiência de Usuário no Terminal: O programa conta com limpeza adaptativa de tela (cls no Windows e clear no Linux/macOS) e pausas estratégicas de tempo (time.sleep) para tornar a leitura do menu fluida.

## 📄 Licença de Uso
Este projeto está sob a licença MIT (modelo de licença livre que permite utilização, modificação e distribuição). Veja o arquivo LICENSE para mais detalhes.
