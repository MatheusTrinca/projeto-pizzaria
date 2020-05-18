from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk


class AdminJanela:

    def __init__(self):
        self.root = Tk()
        self.root.title('ADMIN')

        Button(self.root, text='Pedidos', width=20, bg='orange', command=self.tela_pedidos).grid(row=0, column=0, padx=10, pady=10)
        Button(self.root, text='Cadastros', width=20, bg='orange', command=self.cadastro_produtos).grid(row=1, column=0, padx=10, pady=10)

        self.root.mainloop()

# Front-End

    def tela_pedidos(self):
        self.pedidos = Tk()
        self.pedidos.title('Cadastro de Pedidos')
        self.pedidos['bg'] = '#524f4f'

        Label(self.pedidos, text='Cadastro de Pedidos', bg='#524f4f', fg='white').grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        Label(self.pedidos, text='Nome', bg='#524f4f', fg='white').grid(row=1, column=0, columnspan=1, padx=5, pady=5)
        self.nomep = Entry(self.pedidos)
        self.nomep.grid(row=1, column=1,columnspan=1, padx=5, pady=5)

        Label(self.pedidos, text='Ingredientes', bg='#524f4f', fg='white').grid(row=2, column=0, columnspan=1, padx=5, pady=5)
        self.ingredientesp = Entry(self.pedidos)
        self.ingredientesp.grid(row=2, column=1,columnspan=1, padx=5, pady=5)

        Label(self.pedidos, text='Grupo', bg='#524f4f', fg='white').grid(row=3, column=0, columnspan=1, padx=5, pady=5)
        self.grupop = Entry(self.pedidos)
        self.grupop.grid(row=3, column=1,columnspan=1, padx=5, pady=5)

        Label(self.pedidos, text='localEntrega', bg='#524f4f', fg='white').grid(row=4, column=0, columnspan=1, padx=5, pady=5)
        self.localEntregap = Entry(self.pedidos)
        self.localEntregap.grid(row=4, column=1, columnspan=1, padx=5, pady=5)

        Label(self.pedidos, text='Observacoes', bg='#524f4f', fg='white').grid(row=5, column=0, columnspan=1, padx=5, pady=5)
        self.observacoesp = Entry(self.pedidos)
        self.observacoesp.grid(row=5, column=1,columnspan=1, padx=5, pady=5)

        Button(self.pedidos, text='Incluir', width=16, bg='gray', relief='flat', command=self.incluir_pedido_backend).grid(row=6, column=0, padx=5, pady=5)
        Button(self.pedidos, text='Excluir', width=16, bg='gray', relief='flat', command=self.excluir_pedido_backend).grid(row=6, column=1, padx=5, pady=5)
        Button(self.pedidos, text='Atualizar', width=16, bg='gray', relief='flat', command=self.incluir_pedido_backend).grid(row=7, column=0, padx=5, pady=5)
        Button(self.pedidos, text='Limpar', width=16, bg='gray', relief='flat', command=self.limpar_pedidos_backend).grid(row=7, column=1, padx=5, pady=5)

        self.tree = ttk.Treeview(self.pedidos, selectmode='browse', column=('column1', 'column2', 'column3', 'column4', 'column5'), show='headings')

        self.tree.column('column1', width=200, minwidth=100, stretch=NO)
        self.tree.heading('#1', text='Nome')

        self.tree.column('column2', width=200, minwidth=100, stretch=NO)
        self.tree.heading('#2', text='Ingredientes')

        self.tree.column('column3', width=100, minwidth=100, stretch=NO)
        self.tree.heading('#3', text='Grupo')

        self.tree.column('column4', width=200, minwidth=100, stretch=NO)
        self.tree.heading('#4', text='Local de Entrega')

        self.tree.column('column5', width=200, minwidth=100, stretch=NO)
        self.tree.heading('#5', text='Observações')

        self.tree.grid(row=0, column=4, padx=10, pady=10, columnspan=3, rowspan=6)

        self.mostrar_pedidos_backend()

    def cadastro_produtos(self):
        self.cadastrar = Tk()
        self.cadastrar.title('Cadastro de Produtos')
        self.cadastrar['bg'] = '#524f4f'

        Label(self.cadastrar, text='Cadastro de Produtos', bg='#524f4f', fg='white').grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        Label(self.cadastrar, text='Nome', bg='#524f4f', fg='white').grid(row=1, column=0, columnspan=1, padx=5, pady=5)
        self.nome = Entry(self.cadastrar)
        self.nome.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

        Label(self.cadastrar, text='Ingredientes', bg='#524f4f', fg='white').grid(row=2, column=0, columnspan=1, padx=5, pady=5)
        self.ingrediente = Entry(self.cadastrar)
        self.ingrediente.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

        Label(self.cadastrar, text='Grupo', bg='#524f4f', fg='white').grid(row=3, column=0, columnspan=1, padx=5, pady=5)
        self.grupo = Entry(self.cadastrar)
        self.grupo.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

        Label(self.cadastrar, text='Preço', bg='#524f4f', fg='white').grid(row=4, column=0, columnspan=1, padx=5, pady=5)
        self.preco = Entry(self.cadastrar)
        self.preco.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

        Button(self.cadastrar, text='Cadastrar', width=16, bg='gray', relief='flat', command=self.cadastrar_produtos_backend).grid(row=5, column=0, padx=5, pady=5)
        Button(self.cadastrar, text='Excluir', width=16, bg='gray', relief='flat', command=self.excluir_produtos_backend).grid(row=5, column=1, padx=5, pady=5)
        Button(self.cadastrar, text='Atualizar', width=16, bg='gray', relief='flat', command=self.cadastrar_produtos_backend).grid(row=6, column=0, padx=5, pady=5)
        Button(self.cadastrar, text='Limpar Produtos', width=16, bg='gray', relief='flat', command=self.limpar_cadastro_backend).grid(row=6, column=1, padx=5, pady=5)

        self.tree = ttk.Treeview(self.cadastrar, selectmode='browse', column=('column1', 'column2', 'column3', 'column4'), show='headings')

        self.tree.column('column1', width=200, minwidth=100, stretch=NO)
        self.tree.heading('#1', text='Nome')

        self.tree.column('column2', width=400, minwidth=100, stretch=NO)
        self.tree.heading('#2', text='Ingredientes')

        self.tree.column('column3', width=200, minwidth=100, stretch=NO)
        self.tree.heading('#3', text='Grupo')

        self.tree.column('column4', width=100, minwidth=100, stretch=NO)
        self.tree.heading('#4', text='Preço')

        self.tree.grid(row=0, column=4, padx=10, pady=10, columnspan=3, rowspan=6)

        self.mostrar_produtos_backend()

# Back-End

    def limpar_pedidos_backend(self):
        if messagebox.askokcancel('Cuidado!!', 'Deseja apagar todos os pedidos? NÃO HÁ VOLTA'):
            try:
                conexao = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='',
                    db='erp',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor
                )
            except:
                print('Erro ao Conectar Banco de Dados')

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('delete * from pedidos')
                    conexao.commit()
            except:
                print('Erro ao Conectar Banco de Dados')

        self.mostrar_pedidos_backend()

    def excluir_pedido_backend(self):

        pedido_id = int(self.tree.selection()[0])

        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except ConnectionRefusedError:
            print('Erro ao Conectar Banco de Dados')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('delete from pedidos where id={}'.format(pedido_id))
                conexao.commit()
        except ConnectionRefusedError:
            print('Erro ao conectar Banco de Dados')

        self.mostrar_pedidos_backend()

    def incluir_pedido_backend(self):
        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('Erro ao Conectar Banco de Dados')

        linha_i = list()
        linha_i.append(self.nomep.get())
        linha_i.append(self.ingredientesp.get())
        linha_i.append(self.grupop.get())
        linha_i.append(self.localEntregap.get())
        linha_i.append(self.observacoesp.get())

        with conexao.cursor() as cursor:
            cursor.execute('insert into pedidos(nome, ingredientes, grupo, localEntrega, observacoes) '
                           'values(%s, %s, %s, %s, %s)', (linha_i[0], linha_i[1], linha_i[2], linha_i[3], linha_i[4]))
            conexao.commit()

        self.mostrar_pedidos_backend()

        linha_i.clear()

    def mostrar_pedidos_backend(self):
        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('Erro ao Conectar Banco de Dados')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from pedidos')
                resultado = cursor.fetchall()
        except:
            print('Erro ao Conectar Banco de Dados')

        self.tree.delete(*self.tree.get_children())

        linha_p = []

        for linha in resultado:
            linha_p.append(linha['nome'])
            linha_p.append(linha['ingredientes'])
            linha_p.append(linha['grupo'])
            linha_p.append(linha['localEntrega'])
            linha_p.append(linha['observacoes'])

            self.tree.insert('', END, values=linha_p, iid=linha['id'], tag='1')
            linha_p.clear()

    def mostrar_produtos_backend(self):
        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('Erro ao Conectar Banco de Dados')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from produtos')
                resultado = cursor.fetchall()
        except:
            print('Erro ao Conectar Banco de Dados')

        self.tree.delete(*self.tree.get_children())

        linha_c = []

        for linha in resultado:
            linha_c.append(linha['nome'])
            linha_c.append(linha['ingredientes'])
            linha_c.append(linha['grupo'])
            linha_c.append(linha['preco'])

            self.tree.insert('', END, values=linha_c, iid=linha['id'], tag='1')

            linha_c.clear()

    def cadastrar_produtos_backend(self):
        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('Erro ao Conectar Banco de Dados')

        linha_cp = list()
        linha_cp.append(self.nome.get())
        linha_cp.append(self.ingrediente.get())
        linha_cp.append(self.grupo.get())
        linha_cp.append(self.preco.get())

        try:
            with conexao.cursor() as cursor:
                cursor.execute('insert into produtos(nome, ingredientes, grupo, preco) values(%s, %s, %s, %s)', (linha_cp[0], linha_cp[1], linha_cp[2], linha_cp[3]))
                conexao.commit()
        except:
            print('Erro ao Conectar Banco de Dados')

        linha_cp.clear()

        self.mostrar_produtos_backend()

    def excluir_produtos_backend(self):

        id_deletar = int(self.tree.selection()[0])

        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='erp',
                charset='utf8mb4',
                cursorclass = pymysql.cursors.DictCursor
            )
        except:
            print('Erro ao Conectar Banco de Dados')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('delete from produtos where id={}'.format(id_deletar))
                conexao.commit()
        except:
            print('Erro ao Conectar Banco de Dados')

        self.mostrar_produtos_backend()

    def limpar_cadastro_backend(self):
        if messagebox.askokcancel('Cuidado!!', 'Deseja apagar todos os produos? NÃO HÁ VOLTA'):
            try:
                conexao = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='',
                    db='erp',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor
                )
            except:
                print('Erro ao Conectar Banco de Dados')

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('delete * from produtos')
                    conexao.commit()
            except:
                print('Erro ao Conectar Banco de Dados')

        self.mostrar_produtos_backend()


class JanelaLogin:

    def verifica_login(self):
        autenticado = False
        usuario_master = False

        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='erp',
                charset='utf8mb4',
                cursorclass = pymysql.cursors.DictCursor
            )
        except InterruptedError:
            print('Erro ao Conectar Banco de Dados')

        usuario = self.login.get()
        senha = self.senha.get()

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from cadastros')
                resultado = cursor.fetchall()
        except:
            print('Erro ao Conectar Banco de Dados')

        for linha in resultado:
            if usuario == linha['nome'] and senha == linha['senha']:
                if linha['nivel'] == 1:
                    usuario_master = False
                elif linha['nivel'] == 2:
                    usuario_master = True
                autenticado = True
                break
            else:
                autenticado = False

        if not autenticado:
            messagebox.showinfo('login', 'Usuário ou Senha inválido')

        if autenticado:
            self.root.destroy()
            if usuario_master:
                AdminJanela()

    def cadastro_backend(self):
        codigo_padrao = '1234'
        if self.codigo_seguranca.get() == codigo_padrao:
            if len(self.login.get()) <= 20:
                if len(self.senha.get()) <= 50:
                    nome = self.login.get()
                    senha = self.senha.get()

                    try:
                        conexao = pymysql.connect(
                            host='localhost',
                            user='root',
                            password='',
                            db='erp',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor
                        )
                    except:
                        print('Erro ao Conectar Banco de Dados')

                    try:
                        with conexao.cursor() as cursor:
                            cursor.execute('insert into cadastros (nome, senha, nivel) values(%s, %s, %s)', (nome, senha, 1))
                            conexao.commit()
                        messagebox.showinfo('Cadastro', 'Usuário cadastrado com sucesso')
                        self.root.destroy()
                    except:
                        print('Erro ao Conectar Banco de Dados')

                else:
                    messagebox.showinfo('Erro', 'Senha não pode ser maior que 50 caracteres')
            else:
                messagebox.showinfo('Erro', 'Usuario não pode ser maior que 20 caracteres')
        else:
            messagebox.showinfo('Erro', 'Código de segurança inválido')

    def cadastro(self):
        Label(self.root, text='chave de segurança').grid(row=3, column=0, padx=5, pady=5)
        self.codigo_seguranca = Entry(self.root, show='*')
        self.codigo_seguranca.grid(row=3, column=1, padx=10, pady=5)
        Button(self.root, text='confirmar cadastro', width=15, bg='blue1', command=self.cadastro_backend).grid(row=4, column=0, columnspan=3, padx=5, pady=5)

    def update_backend(self):
        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('Erro ao Conectar Banco de Dados')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from cadastros')
                resultado = cursor.fetchall()
        except:
            print('Erro ao Conectar Banco de Dados')

        self.tree.delete(*self.tree.get_children())

        linha_v = []

        for linha in resultado:
            linha_v.append(linha['id'])
            linha_v.append(linha['nome'])
            linha_v.append(linha['senha'])
            linha_v.append(linha['nivel'])
            self.tree.insert('', END, values=linha_v, iid=linha_v[0], tag=1)

            linha_v.clear()

    def visualizar_cadastros(self):
        self.vc = Toplevel()
        self.vc.resizable(False, False)
        self.vc.title('Visualizar Cadastros')

        self.tree = ttk.Treeview(self.vc, selectmode='browse', column=('column1', 'column2', 'column3', 'column4'), show='headings')

        self.tree.column('column1', width=40, minwidth=100, stretch=NO)
        self.tree.heading('#1', text='ID')

        self.tree.column('column2', width=100, minwidth=100, stretch=NO)
        self.tree.heading('#2', text='Usuario')

        self.tree.column('column3', width=100, minwidth=100, stretch=NO)
        self.tree.heading('#3', text='Senha')

        self.tree.column('column4', width=40, minwidth=100, stretch=NO)
        self.tree.heading('#4', text='Nivel')

        self.tree.grid(row=0, column=0, padx=10, pady=10)

        self.update_backend()

        self.vc.mainloop()

    def __init__(self):
        self.root = Tk()
        self.root.title('Login')
        self.root['bg'] = '#524f4f'

        Label(self.root, text='Faça o Login', fg='white', bg='#524f4f').grid(row=0, column=0, columnspan=2)

        Label(self.root, text='Usuário', fg='white', bg='#524f4f').grid(row=1, column=0)
        self.login = Entry(self.root)
        self.login.grid(row=1, column=1, padx=5, pady=5)

        Label(self.root, text='Senha', fg='white', bg='#524f4f').grid(row=2, column=0)
        self.senha = Entry(self.root, show='*')
        self.senha.grid(row=2, column=1, padx=5, pady=5)

        Button(self.root, text='login', bg='#00cc99', fg='black', width=10, command=self.verifica_login).grid(row=5, column=0, padx=5, pady=5)
        Button(self.root, text='cadastrar', bg='orange1', fg='black', width=10, command=self.cadastro).grid(row=5, column=1, padx=5, pady=5)
        Button(self.root, text='visualizar', bg='gray', fg='black', width=10, command=self.visualizar_cadastros).grid(row=6, column=0, columnspan=2, padx=5, pady=5)



        self.root.mainloop()


JanelaLogin()


