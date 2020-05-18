import matplotlib.pyplot as plt
import pymysql.cursors

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='erp',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

autentico = False


def logar_cadastrar():
    usuario_existente = 0
    usuario_master = False
    autenticado = False

    if decisao == 1:
        nome = input('Digite o seu nome: ')
        senha = input('Digite sua senha')

        for linha in resultado:
            if linha['nome'] == nome and linha['senha'] == senha:
                if linha['nivel'] == 1:
                    usuario_master = False
                elif linha['nivel'] == 2:
                    usuario_master = True
                autenticado = True
                break
            else:
                autenticado = False

        if not autenticado:
            print('Usuario ou senha inválidos')

    elif decisao == 2:
        print('Faça seu cadastro: ')
        nome = input('Digite o seu nome: ')
        senha = input('Digite sua senha')
        for linha in resultado:
            if linha['nome'] == nome and linha['senha'] == senha:
                usuario_existente = 1

        if usuario_existente == 1:
            print('Usuário já cadastrado')
        elif usuario_existente == 0:
            try:
                with conexao.cursor() as cursor:
                    cursor.execute(f"insert into cadastros(nome, senha, nivel) values ('{nome}', '{senha}', 1)")
                    conexao.commit()
                    print('Usuário cadastrado com sucesso')
            except:
                print('Erro ao conectar Banco de Dados')

    return autenticado, usuario_master


def cadastrar_produtos():
    nome = input('Digite o nome do produto: ')
    ingredientes = input('Digite os igredientes do produto: ')
    grupo = input('Digite o grupo do produto: ')
    preco = float(input('Digite o preço do produto: '))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('insert into produtos(nome, ingredientes, grupo, preco) values(%s, %s, %s, %s)',(nome, ingredientes, grupo, preco))
            conexao.commit()
            print('Produto cadastrado com sucesso')
    except:
        print('Erro ao conectar Banco de Dados')


def listar_produtos():
    produtos = []

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from produtos')
            produtos_cadstrados = cursor.fetchall()
    except:
        print('Erro ao conectar Banco de Dados')

    for i in produtos_cadstrados:
        produtos.append(i)

    if len(produtos) != 0:
        for i in range(len(produtos)):
            print(produtos[i])
    else:
        print('Nenhum produto cadastrado')


def excluir_produtos():
    id_deletar = int(input('Digite o id do produto que deseja excluir'))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('delete from produtos where id={}'.format(id_deletar))
    except:
        print('Erro ao conectar Banco de Dados')


def listar_pedido():
    pedidos = []
    decision = 1

    while decision != 0:
        pedidos.clear()
        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from pedidos')
                lista_pedido = cursor.fetchall()
        except:
            print('Erro ao conectar Banco de Dados')

        for i in lista_pedido:
            pedidos.append(i)

        if len(pedidos) != 0:
            for i in range(len(pedidos)):
                print(pedidos[i])
        else:
            print('Nenhum pedido foi feito')

        decision = int(input('Digite 1 para dar como entregue ou 0 para voltar'))

        if decision == 1:
            id_deletar = int(input('Digite o id do pedido entregue'))
            try:
                with conexao.cursor() as cursor:
                    cursor.execute('delete from pedidos where id={}'.format(id_deletar))
                    print('Produto dado como entregue')
            except:
                print('Erro ao conectar Banco de Dados')


def gerar_estatistica():
    nome_produto = []
    nome_produto.clear()

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from produtos')
            produtos = cursor.fetchall()
    except:
        print('Erro ao conectar Banco de Dados')

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from estatisticavendido')
            vendido = cursor.fetchall()
    except:
        print('Erro ao conectar Banco de Dados')

    estado = int(input('Digite 0 para sair\n'
                         '1 para pesquisar por nome\n'
                         '2 para pesquisar por grupo\n'))

    if estado == 1:

        decisao3 = int(input('Digite 1 para pesquisar por dinheiro\n'
                             'Digite 2 para pesquisar por quantidade'))

        if decisao3 == 1:
            for i in produtos:
                nome_produto.append(i['nome'])

            valores = []
            valores.clear()

            for h in range(len(nome_produto)):
                soma = -1
                for i in vendido:
                    if nome_produto[h] == i['nome']:
                        soma += i['preco']
                if soma == -1:
                    valores.append(0)
                elif soma > 0:
                    valores.append(soma + 1)

            plt.plot(nome_produto, valores)
            plt.xlabel('produtos')
            plt.ylabel('valores em reais')
            plt.show()

        if decisao3 == 2:
            grupo_unico = []
            grupo_unico.clear()

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from produtos')
                    grupo = cursor.fetchall()
            except:
                print('Erro ao conectar Banco de Dados')

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from estatisticavendido')
                    vendido_grupo = cursor.fetchall()
            except:
                print('Erro ao conectar Banco de Dados')

            for i in grupo:
                grupo_unico.append(i['nome'])

            grupo_unico = sorted(set(grupo_unico))
            qtd_final = []
            qtd_final.clear()

            for i in range(len(grupo_unico)):
                qtd = 0
                for j in vendido_grupo:
                    if grupo_unico[i] == j['nome']:
                        qtd += 1
                qtd_final.append(qtd)

            plt.plot(grupo_unico, qtd_final)
            plt.xlabel('produtos')
            plt.ylabel('quantidades')
            plt.show()

    if estado == 2:
        decisao3 = int(input('Digite 1 para pesquisar por dinheiro\n'
                             'Digite 2 para pesquisar por quantidade'))
        if decisao3 == 1:
            for i in produtos:
                nome_produto.append(i['grupo'])

            valores = []
            valores.clear()

            for h in range(len(nome_produto)):
                soma = -1
                for i in vendido:
                    if nome_produto[h] == i['grupo']:
                        soma += i['preco']
                if soma == -1:
                    valores.append(0)
                elif soma > 0:
                    valores.append(soma + 1)

            plt.plot(nome_produto, valores)
            plt.xlabel('grupo de produtos')
            plt.ylabel('valores em reais')
            plt.show()

        if decisao3 == 2:
            grupo_unico = []
            grupo_unico.clear()

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from produtos')
                    grupo = cursor.fetchall()
            except:
                print('Erro ao conectar Banco de Dados')

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from estatisticavendido')
                    vendido_grupo = cursor.fetchall()
            except:
                print('Erro ao conectar Banco de Dados')

            for i in grupo:
                grupo_unico.append(i['grupo'])

            grupo_unico = sorted(set(grupo_unico))
            qtd_final = []
            qtd_final.clear()

            for i in range(len(grupo_unico)):
                qtd = 0
                for j in vendido_grupo:
                    if grupo_unico[i] == j['grupo']:
                        qtd += 1
                qtd_final.append(qtd)

            plt.plot(grupo_unico, qtd_final)
            plt.xlabel('grupo de produtos')
            plt.ylabel('quantidades')
            plt.show()


while not autentico:
    decisao = int(input('Digite 1 para logar ou 2 para cadastrar: '))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from cadastros')
            resultado = cursor.fetchall()
    except:
        print('Erro ao conectar Banco de Dados')

    autentico, usuario_supremo = logar_cadastrar()

if autentico:
    print('Usuário autenticado')

    if usuario_supremo:

        decisao_usuario = 9

        while decisao_usuario != 0:

            decisao_usuario = int(input('Digite:\n'
                                        '0 para sair\n'
                                        '1 para cadastrar produtos\n'
                                        '2 para listar produtos cadastrados\n'
                                        '3 para listar os pedidos\n'
                                        '4 para visualizar estatísticas'))

            if decisao_usuario == 1:
                cadastrar_produtos()
            elif decisao_usuario == 2:
                listar_produtos()
                delete = int(input('Digite 1 para excluir produto ou 0 para sair'))
                if delete == 1:
                    excluir_produtos()
            elif decisao_usuario == 3:
                listar_pedido()
            elif decisao_usuario == 4:
                gerar_estatistica()


