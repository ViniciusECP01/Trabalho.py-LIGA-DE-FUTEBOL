import tkinter as tk
from tkinter import messagebox
import dados_liga
import motor_jogo
import estatisticas

class LigaFutebolApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Liga de Futebol Pro")
        self.root.geometry("850x650")
        
        self.liga = [] 

        # --- ZONA 1: GESTÃO DE EQUIPAS ---
        frame_gestao = tk.LabelFrame(root, text="1. Gestão de Equipas", padx=10, pady=10)
        frame_gestao.pack(fill="x", padx=10, pady=5)

        tk.Label(frame_gestao, text="Nome da Equipa:").grid(row=0, column=0)
        self.ent_equipa = tk.Entry(frame_gestao, width=20)
        self.ent_equipa.grid(row=0, column=1, padx=5)

        tk.Button(frame_gestao, text="Adicionar", command=self.btn_adicionar).grid(row=0, column=2, padx=2)
        tk.Button(frame_gestao, text="Remover", command=self.btn_remover).grid(row=0, column=3, padx=2)
        tk.Button(frame_gestao, text="Pesquisar", command=self.btn_pesquisar).grid(row=0, column=4, padx=2)

        # --- ZONA 2: MOTOR DE JOGO ---
        frame_jogo = tk.LabelFrame(root, text="2. Registar Jogo", padx=10, pady=10)
        frame_jogo.pack(fill="x", padx=10, pady=5)

        self.ent_casa = tk.Entry(frame_jogo, width=15); self.ent_casa.grid(row=0, column=0)
        self.ent_golos_c = tk.Entry(frame_jogo, width=5); self.ent_golos_c.grid(row=0, column=1)
        tk.Label(frame_jogo, text=" VS ").grid(row=0, column=2)
        self.ent_golos_f = tk.Entry(frame_jogo, width=5); self.ent_golos_f.grid(row=0, column=3)
        self.ent_fora = tk.Entry(frame_jogo, width=15); self.ent_fora.grid(row=0, column=4)
        
        tk.Button(frame_jogo, text="Registar Resultado", bg="lightblue", command=self.btn_registar_jogo).grid(row=1, column=0, columnspan=5, pady=10)

        # --- ZONA 3: CLASSIFICAÇÃO ---
        frame_classificacao = tk.LabelFrame(root, text="3. Tabela Classificativa", padx=10, pady=10)
        frame_classificacao.pack(fill="both", expand=True, padx=10, pady=5)

        self.txt_tabela = tk.Text(frame_classificacao, height=8, state="disabled", font=("Courier", 10))
        self.txt_tabela.pack(fill="both")

        tk.Button(frame_classificacao, text="Atualizar e Ordenar Tabela", command=self.btn_atualizar_tabela).pack(pady=5)

        # --- ZONA 4: ESTATÍSTICAS AVANÇADAS ---
        frame_stats = tk.LabelFrame(root, text="4. Estatísticas do Campeonato", padx=10, pady=10)
        frame_stats.pack(fill="x", padx=10, pady=5)

        self.lbl_stats = tk.Label(frame_stats, text="Total Jogos: 0 | Média Golos: 0.0\nMelhor Ataque: ---", justify="left")
        self.lbl_stats.pack()
        tk.Button(frame_stats, text="Calcular Estatísticas", command=self.btn_calcular_stats).pack(pady=5)

    def btn_adicionar(self):
        nome = self.ent_equipa.get()
        dados_liga.adicionar_equipa(self.liga, nome)
        messagebox.showinfo("Sucesso", f"{nome} adicionada!")
        self.ent_equipa.delete(0, tk.END)

    def btn_remover(self):
        nome = self.ent_equipa.get()
        dados_liga.remover_equipa(self.liga, nome)
        messagebox.showinfo("Sucesso", f"{nome} removida!")

    def btn_pesquisar(self):
        nome = self.ent_equipa.get()
        dados = dados_liga.pesquisar_equipa(self.liga, nome)
        messagebox.showinfo("Dados da Equipa", str(dados))

    def btn_registar_jogo(self):
        eq_c = self.ent_casa.get()
        gl_c = int(self.ent_golos_c.get() or 0)
        eq_f = self.ent_fora.get()
        gl_f = int(self.ent_golos_f.get() or 0)
        motor_jogo.registar_jogo(self.liga, eq_c, gl_c, eq_f, gl_f)
        messagebox.showinfo("Jogo Registado", "Resultado processado com sucesso!")

    def btn_atualizar_tabela(self):
        lista_ordenada = estatisticas.ordenar_classificacao(self.liga)
        self.txt_tabela.config(state="normal")
        self.txt_tabela.delete(1.0, tk.END)
        
        cabecalho = f"{'Equipa':<15} | {'Pontos':<8} | {'Vitórias':<10} | {'Derrotas':<10} | {'Empates':<9} | {'Golos Marc.':<12} | {'Golos Sofr.':<12}\n"
        self.txt_tabela.insert(tk.END, cabecalho)
        self.txt_tabela.insert(tk.END, "-" * 95 + "\n")
        
        if lista_ordenada:
            for eq in lista_ordenada:
                linha = (f"{eq.get('nome', ''):<15} | {eq.get('pontos', 0):<8} | {eq.get('vitorias', 0):<10} | {eq.get('derrotas', 0):<10} | {eq.get('empates', 0):<9} | {eq.get('gm', 0):<12} | {eq.get('gs', 0):<12}\n")
                self.txt_tabela.insert(tk.END, linha)
        self.txt_tabela.config(state="disabled")

    def btn_calcular_stats(self):
        total = estatisticas.calcular_total_jogos(self.liga)
        media = estatisticas.calcular_media_golos(self.liga)
        melhor_ataque = estatisticas.obter_melhor_ataque(self.liga)
        texto = f"Total Jogos: {total} | Média Golos: {media:.2f}\nMelhor Ataque: {melhor_ataque}"
        self.lbl_stats.config(text=texto)

if __name__ == "__main__":
    root = tk.Tk()
    app = LigaFutebolApp(root)
    root.mainloop()