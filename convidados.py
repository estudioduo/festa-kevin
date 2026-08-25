# Fonte única da lista. O convite e o painel são gerados daqui.
# s: confirmou | aguardando | nao
GRUPOS = [
    ("p1",  "Shirley",         "confirmou",  ["Shirley", "Jeferson"]),
    ("p2",  "Xuxu",            "confirmou",  ["Gilson (Xuxu)", "Cida", "Julia (Pinto)", "Luquinhas"]),
    ("p3",  "Jéssica",         "confirmou",  ["Jéssica"]),
    ("p4",  "Joelma",          "confirmou",  ["Joelma"]),
    ("p5",  "Monique",         "confirmou",  ["Monique", "João"]),
    ("p6",  "Jucilaine",       "aguardando", ["Jucilaine", "Arthur"]),
    ("p7",  "Jaciara",         "aguardando", ["Jaciara", "Elion"]),
    ("p8",  "Família Neco",    "aguardando", ["Jeferson (avô)", "Cristiane (avó)", "Julia (Tita)", "Jeferson (tio)", "Maria (bisavó)"]),
    ("p9",  "Pedra",           "confirmou",  ["Beronio", "Lane", "Ryan", "Nátaly"]),
    ("p10", "Andrey",          "confirmou",  ["Andrey", "Lívia"]),
    ("p11", "Saullo",          "confirmou",  ["Saullo", "Érica"]),
    ("p12", "Galeguinho",      "confirmou",  ["Altamir (Galeguinho)", "Mariane (Mari)"]),
    ("p13", "Matheus Casado",  "aguardando", ["Matheus", "Carla"]),
    ("p14", "Jean",            "aguardando", ["Jean", "Jansen", "Marilene", "Juliete", "Maria"]),
    ("p15", "João BK",         "confirmou",  ["João", "Micaela"]),
    ("p16", "Yago",            "confirmou",  ["Yago"]),
    ("p17", "Nicole",          "confirmou",  ["Nicole (Nikk)", "Thiago"]),
    ("p18", "Jonatas",         "confirmou",  ["Jonatas (Jhones)", "Lenita"]),
    ("p19", "Marcondes",       "confirmou",  ["Marcondes (Coninho)", "Isabel"]),
    ("p20", "Davisson",        "confirmou",  ["Davisson"]),
    ("p21", "Luana",           "confirmou",  ["Luana", "Júlio"]),
    ("p22", "Bartô",           "confirmou",  ["Bartolomeu (Bartô)", "Laila"]),
    ("p23", "Jadson",          "confirmou",  ["Jadsoncley (Jadson)", "Alessandra", "Clarissa", "Aninha"]),
    ("p24", "Rafael Matheus",  "confirmou",  ["Matheus", "Letícia"]),
    ("p25", "130 (Bom Parto)", "confirmou",  ["Cida (avó)", "Lapão (avô)", "Josiane (tia)", "Dido (tio)", "Luana (prima)", "Isaac (primo)"]),
]

def js(t):
    return '"' + t.replace('\\', '\\\\').replace('"', '\\"') + '"'

def bloco_convite():
    largura = max(len(g[1]) for g in GRUPOS) + 2
    linhas = []
    for _, nome, _, membros in GRUPOS:
        m = ", ".join(js(x) for x in membros)
        linhas.append("    { g: %s m: [%s] }," % ((js(nome) + ",").ljust(largura + 1), m))
    linhas[-1] = linhas[-1].rstrip(",")
    return "\n".join(linhas)

def bloco_painel():
    largura = max(len(g[1]) for g in GRUPOS) + 2
    linhas = []
    for pid, nome, s, membros in GRUPOS:
        m = ", ".join(js(x) for x in membros)
        linhas.append('    { id: %s nome: %s s: %s q: %d, ob: "", m: [%s], fora: [] },'
                      % ((js(pid) + ",").ljust(7), (js(nome) + ",").ljust(largura + 1),
                         (js(s) + ",").ljust(14), len(membros), m))
    linhas[-1] = linhas[-1].rstrip(",")
    return "\n".join(linhas)

if __name__ == "__main__":
    total = sum(len(g[3]) for g in GRUPOS)
    vao = sum(len(g[3]) for g in GRUPOS if g[2] == "confirmou")
    print("grupos:", len(GRUPOS), "| pessoas na lista:", total, "| contando pro buffet:", vao)
    for st in ("confirmou", "aguardando", "nao"):
        n = [g[1] for g in GRUPOS if g[2] == st]
        print(" ", st, len(n), "->", ", ".join(n) if len(n) < 6 else "")
