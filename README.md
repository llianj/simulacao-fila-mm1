# Simulação de Fila M/M/1

Simulação de uma fila de atendimento (chegadas e serviços aleatórios) usando a biblioteca `simpy`.

## O que o código faz

## Parâmetros

| Parâmetro | Significado |
|---|---|
| `lambdaa` (λ) | taxa de chegada de clientes |
| `mu` (µ) | taxa de atendimento por servidor |
| `servidores` | número de atendentes |
| `n_clientes` | número de clientes simulados |
| `semente` | semente do gerador aleatório |

## Como rodar

```bash
python simulador.py
```

O programa executa em 4 etapas, pausando com Enter entre elas:

1. **Rodada base** (λ=0,8): mostra o log dos 6 primeiros clientes e as métricas.
2. **Teste 1**: roda com λ = 0,5, 0,8 e 0,95, para ver o efeito da utilização na espera.
3. **Teste 2**: roda com λ=1,2 usando 1 e depois 2 atendentes, para ver se um atendente extra resolve a instabilidade.
4. **Teste 3**: roda duas vezes com a mesma semente, para confirmar que o resultado é reprodutível.

