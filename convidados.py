# Fonte única da lista. O convite e o painel são gerados daqui.
# s: falou | aguardando | sem | confirmou | nao
GRUPOS = [
    ("p1",  "Shirley",         "falou",      ["Shirley", "Jeferson"]),
    ("p2",  "Xuxu",            "falou",      ["Gilson (Xuxu)", "Cida", "Julia (Pinto)", "Luquinhas"]),
    ("p3",  "Jéssica",         "falou",      ["Jéssica"]),
    ("p4",  "Joelma",          "falou",      ["Joelma"]),
    ("p5",  "Monique",         "falou",      ["Monique", "João"]),
    ("p6",  "Jucilaine",       "aguardando", ["Jucilaine", "Arthur"]),
    ("p7",  "Jaciara",         "aguardando", ["Jaciara", "Elion"]),
    ("p8",  "Família Neco",    "aguardando", ["Jeferson (avô)", "Cristiane (avó)", "Julia (Tita)", "Jeferson (tio)", "Maria (bisavó)"]),
    ("p9",  "Pedra",           "falou",      ["Beronio", "Lane", "Ryan", "Nátaly"]),
    ("p10", "Andrey",          "falou",      ["Andrey", "Lívia"]),
    ("p11", "Saullo",          "falou",      ["Saullo", "Érica"]),
    ("p12", "Galeguinho",      "falou",      ["Altamir (Galeguinho)", "Mariane (Mari)"]),
    ("p13", "Matheus Casado",  "aguardando", ["Matheus", "Carla"]),
    ("p14", "Jean",            "aguardando", ["Jean", "Jansen", "Marilene", "Juliete", "Maria"]),
    ("p15", "João BK",         "falou",      ["João", "Micaela"]),
    ("p16", "Yago",            "falou",      ["Yago"]),
    ("p17", "Nicole",          "falou",      ["Nicole (Nikk)", "Thiago"]),
    ("p18", "Jonatas",         "falou",      ["Jonatas (Jhones)", "Lenita"]),
    ("p19", "Marcondes",       "falou",      ["Marcondes (Coninho)", "Isabel"]),
    ("p20", "Davisson",        "falou",      ["Davisson"]),
    ("p21", "Luana",           "falou",      ["Luana", "Júlio"]),
    ("p22", "Bartô",           "falou",      ["Bartolomeu (Bartô)", "Laila"]),
    ("p23", "Jadson",          "falou",      ["Jadsoncley (Jadson)", "Alessandra", "Clarissa", "Aninha"]),
    ("p24", "Rafael Matheus",  "falou",      ["Matheus", "Letícia"]),
    ("p25", "130 (Bom Parto)", "falou",      ["Cida (avó)", "Lapão (avô)", "Josiane (tia)", "Dido (tio)", "Luana (prima)", "Isaac (primo)"]),
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
    vao = sum(len(g[3]) for g in GRUPOS if g[2] in ("falou", "confirmou"))
    print("grupos:", len(GRUPOS), "| pessoas na lista:", total, "| contando pro buffet:", vao)
    for st in ("falou", "aguardando", "sem", "nao"):
        n = [g[1] for g in GRUPOS if g[2] == st]
        print(" ", st, len(n), "->", ", ".join(n) if len(n) < 6 else "")
