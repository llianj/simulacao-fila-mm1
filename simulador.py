# Nome da Tarefa:
# Atividade de simulação
# Descrição:
# Replicar a simulação da versão 2 (a que possui tempos sorteados) trocando a semente pelo seu número de matrícula. 



# Entregue um código python que contenha os seguintes itens:



# 1 Parâmetros no topo, com nome: λ, µ, atendentes, nº de clientes e a MATRICULA como semente.
# 2 Rodada base com λ= 0,8: o log dos 6 primeiros clientes e as métricas com as contas à mostra (ρ, espera, ocupado, total, U, la máxima).
# 3 Teste 1: rodar com λ= 0,5, 0,8 e 0,95. A espera piorou? O U cou perto do ρ?
# 4 Teste 2: λ= 1,2 com 1 e com 2 atendentes. O segundo atendente resolveu?
# 5 Teste 3: rodar duas vezes com a mesma semente. Deu igual? 

#2024003763
#yield guarda o estado onde estava, ele para e guarda até ser chamado de novo
 

import simpy
import random


saidas = [] 

lambdaa = 0.8 
mu = 1.0 
servidores = 1 
n_clientes = 500
semente = 2024003763
mostrar_log = False
contador = 1

esperas = []
servicos = []
fila = []

# def cliente(env, nome, servidor, mu, log):
#     chegada = env.now
#     with servidor.request() as req:
#         fila.append(len(servidor.queue))
#         yield req
#         w = env.now - chegada
#         esperas.append(w)
#         if log:
#             print(f"{env.now:5.2f} {nome} inicia (esperou {w:2f})")
#         x = random.expovariate(mu)
#         servicos.append(x)
#         yield env.timeout(x)

def cliente(env, nome, servidor, mu, log):
    chegada = env.now
    with servidor.request() as req:
        fila.append(len(servidor.queue))
        yield req
        w = env.now - chegada
        esperas.append(w)
        global contador
        if contador != 7 and log:
            print(f"Cliente {contador} {env.now:5.2f} {nome} inicia (esperou {w:2f})")
            contador += 1
        x = random.expovariate(mu)
        servicos.append(x)
        yield env.timeout(x)

def chegadas(env, servidor, lambdaa, mu, n, log):
    for i in range(n):
        yield env.timeout(random.expovariate(lambdaa))
        env.process(cliente(env, f"c{i+1}", servidor, mu, log))

def rodar(lam=lambdaa, mu=mu, servidores=servidores, n=n_clientes, semente=semente, log=mostrar_log):
    random.seed(semente)
    esperas.clear(); servicos.clear(); fila.clear()
    env = simpy.Environment()
    servidor = simpy.Resource(env, capacity=servidores)
    env.process(chegadas(env, servidor, lam, mu, n, log))
    env.run()
    ocupado = sum(servicos)
    total = env.now
    rho = lam / (servidores * mu)
    espera_media = sum(esperas) / len(esperas) if esperas else 0
    U = ocupado / (total * servidores)
    la_maxima = servidores * mu

    print(f"\nλ={lam};\nservidores={servidores};\nsemente={semente}")
    print(f"Ultilizacao = Lamda / (servidores · taxa de servico) = {lam}/({servidores}·{mu}) = {rho:.3f}")
    print(f"\nEspera media = {espera_media:.3f}")
    print(f"\nocupado = {ocupado:.2f}  |  total = {total:.2f}")
    print(f"\nU = ocupado/(total · servidores) = {ocupado:.2f}/({total:.2f}·{servidores}) = {U:.3f}")
    print(f"\nλ maxima (estabilidade) = servidores · taxa de serviço = {la_maxima}")
    return dict(rho=rho, espera=espera_media, U=U, la_maxima=la_maxima)


input("Pressione enter para ir para rodada base  ")
print("Teste base")
rodar(lam=0.8, log=True)
print("\n")

input("Pressione enter para ir para rodada 1  ")
print(f"Rodada 1")
print(f"Teste 1")
for lam in [0.5, 0.8, 0.95]:
    rodar(lam=lam)
# 3 Teste 1: rodar com λ= 0,5, 0,8 e 0,95. A espera piorou? O U cou perto do ρ?
# A espera piorou; e a ultilização ficou perto do ρ, mas não  igual


input("Pressione enter para ir para rodada 2  ")
print("\n")
print(f"Rodada 2")
print("\nTeste  2")
rodar(lam=1.2, servidores=1)
rodar(lam=1.2, servidores=2)
# 4 Teste 2: λ= 1,2 com 1 e com 2 atendentes. O segundo atendente resolveu?
# resolveu, porque o sistema volta a ser estável

input("Pressione enter para ir para rodada 3  ")
print(f"Rodada 3")
print("\nTeste 3")
r1 = rodar(lam=0.8, semente=semente)
r2 = rodar(lam=0.8, semente=semente)
if r1 == r2:
    print("Resultados iguais? Sim")
else:
    print("Resultados iguais? Não")
# print("Resultados iguais?", r1 == r2)
print(f"\n")
# 5 Teste 3: rodar duas vezes com a mesma semente. Deu igual? 
# sim




# rodar();