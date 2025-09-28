import argparse
from kb_parser import parse_kb
from graph_search import build_graph, dijkstra_time

def pretty_print_result(res):
    if not res:
        print("⚠️ No se encontró ruta.")
        return
    print("\n📍 Ruta encontrada:\n")
    for i, step in enumerate(res['path'], 1):
        u, v, t, line, switched = step
        s = f"{i}. {u} -> {v} | {t} min | línea={line}"
        if switched:
            s += " (transbordo aplicado)"
        print(s)
    print(f"\n⏱️ Tiempo total estimado: {res['time']:.2f} min")

def run(kbfile, start, goal):
    kb = parse_kb(kbfile)
    graph = build_graph(kb['edges'])
    tp = kb.get('transfer_penalty', 0.0)
    res = dijkstra_time(graph, start, goal, transfer_penalty=tp)
    pretty_print_result(res)
    return res

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sistema de rutas en transporte masivo")
    parser.add_argument("--kb", default="../kb/kb_example.txt", help="Archivo KB con reglas")
    parser.add_argument("--start", required=True, help="Estación de inicio")
    parser.add_argument("--goal", required=True, help="Estación de destino")
    args = parser.parse_args()
    run(args.kb, args.start, args.goal)
