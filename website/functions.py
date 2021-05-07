import math
from matplotlib import pyplot as plt

def atenuacaoEspacoLivre(f: "frequencia [GHz]", ptx: "potencia [dBm]", prx_min: "potencia minima [dBm]"):

    l_d = []
    l_prx = []
    l_prx_min = []

    d = 0
    l = 0
    while(ptx - l > prx_min - 2):
        d += 1
        l = 32.44 + 20 * math.log10(d / 1000000) + 20 * math.log10(f * 1000)
        l_prx.append(ptx - l)

    l_d = list(range(1,d+1))
    l_prx_min = [prx_min for i in range(1,d+1)]

    plt.style.use('seaborn-bright')
    plt.plot(l_d, l_prx, label="Prx")
    plt.plot(l_d, l_prx_min, label="Prx_min")

    plt.xlabel('distância [m]')
    plt.ylabel('Potência recebida [dBm]')
    plt.title(f'Nível de sinal recebido (Ptx = {ptx} dBm e f = {f} GHz)')
    plt.legend()
    plt.savefig('website/static/website/images/free-space.jpg')
    plt.close()

