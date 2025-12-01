# main.py
import os
import sys
from tabulate import tabulate
from database import get_connection, relatorio_veterinarios, relatorio_consultas_agendadas, relatorio_gastos_tutor

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_report(headers, data, title):
    clear_screen()
    print("=" * 60)
    print(f"| {title:^56} |")
    print("=" * 60)
    
    if data:
        print(tabulate(data, headers=headers, tablefmt="fancy_grid", numalign="center"))
    else:
        print("\nNenhum registro encontrado ou falha na consulta.")
    
    print("\nPressione ENTER para voltar ao menu...")
    input()
    clear_screen()

def main_menu():
    conn = get_connection()
    if not conn:
        sys.exit(1) 

    while True:
        print("=" * 40)
        print("| CONSOLE DE RELATÓRIOS VETSYS |")
        print("=" * 40)
        print("1. Relatório de Veterinários e Consultas")
        print("2. Registro de Consultas (Agendadas/Realizadas)")
        print("3. Relatório de Total Gasto por Tutor")
        print("0. Sair")
        print("-" * 40)
        
        choice = input("Escolha uma opção: ")

        headers, data = None, None
        
        if choice == '1':
            headers, data = relatorio_veterinarios(conn)
            display_report(headers, data, "Relatório de Veterinários")
        elif choice == '2':
            headers, data = relatorio_consultas_agendadas(conn)
            display_report(headers, data, "Registro de Consultas")
        elif choice == '3':
            headers, data = relatorio_gastos_tutor(conn)
            display_report(headers, data, "Relatório de Gastos por Tutor")
        elif choice == '0':
            print("\nSaindo do Console. Até mais!")
            conn.close()
            break
        else:
            print("\nOpção inválida. Tente novamente.")
            input()
            clear_screen()

if __name__ == "__main__":
    main_menu()