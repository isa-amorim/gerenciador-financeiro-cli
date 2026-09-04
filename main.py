import time

# ==========================================
# CONFIGURAÇÕES E CONSTANTES
# ==========================================
PIN_CORRETO = "1234"
LIMITE_TENTATIVAS = 3
TAXA_JUROS_ANUAL = 0.10  # 10% a.a.

# Estado global da aplicação (Armazenamento em memória)
saldo_total = 0.0
historico_transacoes = []  # Formato: [{"tipo": "RECEITA", "valor": 100.0, "categoria": "SALARIO"}]


# ==========================================
# HELPER FUNCTIONS (SANITIZAÇÃO E VALIDAÇÃO)
# ==========================================
def sanitizar_texto(texto):
    """Remove espaços extras e converte para caixa alta."""
    return texto.strip().upper()


def validar_valor_positivo(mensagem_input):
    """Garante que o valor digitado seja numérico e maior que zero."""
    tentativas = 0
    while tentativas < 3:
        try:
            valor = float(input(mensagem_input))
            if valor > 0:
                return valor
            print("[ERRO] O valor deve ser maior que zero.")
        except ValueError:
            print("[ERRO] Entrada inválida. Digite apenas números.")
        tentativas += 1
    print("[ALERT] Número máximo de tentativas de digitação excedido.")
    return None


# ==========================================
# REGRAS DE NEGÓCIO
# ==========================================
def autenticar_usuario():
    """RF-01: Controle de acesso com limite de tentativas usando while/break."""
    tentativas = 0
    while tentativas < LIMITE_TENTATIVAS:
        pin = input("Digite seu PIN de 4 dígitos para acessar: ").strip()
        if pin == PIN_CORRETO:
            print("\n[SUCESSO] Acesso concedido!")
            return True
        else:
            tentativas += 1
            restantes = LIMITE_TENTATIVAS - tentativas
            print(f"[ERRO] PIN incorreto. Tentativas restantes: {restantes}")
    
    print("\n[BLOQUEADO] Sistema bloqueado por excesso de tentativas incorretas.")
    return False


def registrar_transacao(tipo):
    """RF-02 & RF-03: Entrada de transações e atualização do fluxo de caixa."""
    global saldo_total
    
    print(f"\n--- Novo Registro de {tipo} ---")
    categoria = input("Digite a categoria (ex: ALIMENTACAO, TRANSPORTE, SALARIO): ")
    categoria = sanitizar_texto(categoria)
    
    valor = validar_valor_positivo(f"Digite o valor da {tipo.lower()}: R$ ")
    if valor is None:
        print("[CANCELADO] Operação cancelada devido a erro nos dados de entrada.")
        return

    if tipo == "DESPESA":
        saldo_total -= valor
    else:
        saldo_total += valor

    transacao = {
        "tipo": tipo,
        "valor": valor,
        "categoria": categoria
    }
    historico_transacoes.append(transacao)
    
    print(f"[SISTEMA] Processando lançamento...")
    time.sleep(0.5)  # Simulação de latência de processamento
    print(f"[OK] {tipo} registrada com sucesso!")


def simular_rendimento():
    """RF-04: Simulação de juros compostos sobre o saldo atual."""
    print("\n--- Simulação de Rendimentos (Fintech Module) ---")
    if saldo_total <= 0:
        print("[AVISO] Rendimento indisponível para saldos zerados ou negativos.")
        return

    anos = validar_valor_positivo("Informe o período do rendimento (em anos): ")
    if anos is None:
        return

    # Fórmula de Juros Compostos: M = P * (1 + i)^t
    montante = saldo_total * ((1 + TAXA_JUROS_ANUAL) ** anos)
    lucro = montante - saldo_total

    print(f"\nSaldo Atual: R$ {saldo_total:.2f}")
    print(f"Taxa Fixa: {TAXA_JUROS_ANUAL * 100:.1f}% a.a.")
    print(f"Projeção para {int(anos)} ano(s): R$ {montante:.2f} (Rendimento: +R$ {lucro:.2f})")


def exibir_extrato_filtrado():
    """RF-05: Relatório de transações com filtragem condicional."""
    print("\n--- Extrato Financeiro ---")
    print("Filtros disponíveis: [1] Todas | [2] Apenas Receitas | [3] Apenas Despesas")
    opcao_filtro = input("Escolha a opção de filtro: ").strip()

    filtro_map = {"1": "TODAS", "2": "RECEITA", "3": "DESPESA"}
    tipo_selecionado = filtro_map.get(opcao_filtro, "TODAS")

    print("\n" + "="*40)
    print(f" EXTRATO DE TRANSAÇÕES - FILTRO: {tipo_selecionado}")
    print("="*40)

    encontrou_registros = False
    for t in historico_transacoes:
        if tipo_selecionado == "TODAS" or t["tipo"] == tipo_selecionado:
            sinal = "+" if t["tipo"] == "RECEITA" else "-"
            print(f"[{t['tipo']}] {t['categoria']:<15} | {sinal} R$ {t['valor']:.2f}")
            encontrou_registros = True

    if not encontrou_registros:
        print("Nenhuma transação encontrada para este filtro.")

    print("-" * 40)
    print(f"SALDO LÍQUIDO ATUAL: R$ {saldo_total:.2f}")
    print("="*40)


# ==========================================
# INTERFACE DE USUÁRIO (LOOP CLI)
# ==========================================
def menu_principal():
    """Loop principal do sistema ativado após autenticação."""
    while True:
        print("\n==========================================")
        print("     GERENCIADOR FINANCEIRO CLI v1.0      ")
        print("==========================================")
        print(f" Saldo Atual: R$ {saldo_total:.2f}")
        print("------------------------------------------")
        print("1. Registrar RECEITA")
        print("2. Registrar DESPESA")
        print("3. Visualizar Extrato")
        print("4. Simular Rendimento Futuro")
        print("5. Sair")
        print("==========================================")
        
        opcao = input("Selecione uma opção (1-5): ").strip()

        if opcao == "1":
            registrar_transacao("RECEITA")
        elif opcao == "2":
            registrar_transacao("DESPESA")
        elif opcao == "3":
            exibir_extrato_filtrado()
        elif opcao == "4":
            simular_rendimento()
        elif opcao == "5":
            print("\nEncerrando sessão com segurança...")
            time.sleep(0.5)
            print("Até logo!")
            break
        else:
            print("[ERRO] Opção inválida. Escolha um número de 1 a 5.")


if __name__ == "__main__":
    # Início da execução do programa
    if autenticar_usuario():
        menu_principal()