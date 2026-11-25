from conexao import conectar

def menu_instrutores(codigo_usuario):
    while True:
        print("\n=== MENU DE INSTRUTORES ===")
        print("1- Cadastrar")
        print("2- Listar")
        print("3- Editar")
        print("4- Excluir")
        print("0- Voltar")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_instrutor(codigo_usuario)
        elif opcao == "2":
            listar_instrutor(codigo_usuario)
        elif opcao == "3":
            editar_instrutor(codigo_usuario)
        elif opcao == "4":
            excluir_instrutor(codigo_usuario)
        elif opcao == "0":
            break
        else:
            print("Opção inválida")

def cadastrar_instrutor(codigo_usuario):
    print("\n--- CADASTRAR INSTRUTOR ---")
    nome = input("Nome: ").strip()
    cref = input("CREF: ").strip()
    cpf = input("CPF: ").strip()
    telefone = input("Telefone: ").strip()
    especialidade = input("Especialidade: ").strip()
    endereco = input("Endereço: ").strip()

    if not nome or not cref or not cpf:
        print("Nome, CREF e CPF são obrigatórios.")
        return

    conn = conectar()
    cur = conn.cursor()
    try:
        sql = """ 
        INSERT INTO instrutor (nome, cref, cpf, telefone, especialidade, endereco, codigo_usuario)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(sql, (nome, cref, cpf, telefone, especialidade, endereco, codigo_usuario))
        conn.commit()
        print("Instrutor cadastrado com sucesso!")
    except Exception as erro:
        conn.rollback()
        print(f"Erro ao cadastrar instrutor: {erro}")
    finally:
        cur.close()
        conn.close()

def listar_instrutor(codigo_usuario):
    print("\n--- LISTA DE INSTRUTORES ---")
    conn = conectar()
    cur = conn.cursor()
    try:
        sql = """
            SELECT codigo, nome, cref, cpf, telefone, especialidade, endereco
            FROM instrutor
            WHERE codigo_usuario = %s
            ORDER BY nome ASC
        """
        cur.execute(sql, (codigo_usuario,))
        instrutores = cur.fetchall()

        if not instrutores:
            print("Nenhum instrutor cadastrado nesta conta.")
            return

        for inst in instrutores:
            print(
                f"Código: {inst[0]} | Nome: {inst[1]} | CREF: {inst[2]} | "
                f"CPF: {inst[3]} | Tel: {inst[4]} | Esp.: {inst[5]} | End. {inst[6]}"
                )
    except Exception as erro:
        print(f"Erro ao listar isntrutores: {erro}")
    finally:
        cur.close()
        conn.close()

def editar_instrutor(codigo_usuario):
    print("\n--- EDITAR INSTRUTOR ---")
    try:
        codigo_instrutor = int(input("Digite o código do instrutor: ").strip())
    except ValueError:
        print("Código inválido. Digite apenas números.")
        return

    conn = conectar()
    cur = conn.cursor()
    try:
        sql_busca = """
            SELECT codigo, nome, cref, cpf, telefone, especialidade, endereco
            FROM instrutor
            WHERE codigo = %s AND codigo_usuario = %s
        """
        cur.execute(sql_busca, (codigo_instrutor, codigo_usuario))
        instrutor = cur.fetchone()

        if not instrutor:
            print("Instrutor não encontrado nesta conta.")
            return

        print("Deixe em branco para manter o valor atual.")
        novo_nome = input(f"Novo nome [{instrutor[1]}]: ").strip() or instrutor[1]
        novo_cref = input(f"Novo CREF [{instrutor[2]}]: ").strip() or instrutor[2]
        novo_cpf = input(f"Novo CPF [{instrutor[3]}]: ").strip() or instrutor[3]
        novo_tel = input(f"Novo telefone [{instrutor[4]}]: ").strip() or instrutor[4]
        novo_esp = input(f"Nova especialidade [{instrutor[5]}]: ").strip() or instrutor[5]
        novo_end = input(f"Novo endereço [{instrutor[6]}]: ").strip() or instrutor[6]

        sql_update = """
            UPDATE instrutor
            SET nome = %s, cref = %s, cpf = %s, telefone = %s, especialidade = %s, endereco = %s
            WHERE codigo = %s AND codigo_usuario = %s
        """
        cur.execute(
            sql_update,
            (novo_nome, novo_cref, novo_cpf, novo_tel, novo_esp, novo_end, codigo_instrutor, codigo_usuario),
            )
        conn.commit()
        print("Instrutor atualizado com sucesso!")
    except Exception as erro:
        conn.rollback()
        print(f"Erro ao editar instrutor: {erro}")
    finally:
        cur.close()
        conn.close()

def excluir_instrutor(codigo_usuario):
    print("\n--- EXCLUIR INSTRUTOR ---")
    try:
        codigo_instrutor = int(input("Digite o código do instrutor: ").strip())
    except ValueError:
       print("Código inválido. Digite apenas números.")
       return
    conn = conectar()
    cur = conn.cursor()
    try:
        sql_busca = """
            SELECT codigo, nome
            FROM instrutor
            WHERE codigo = %s AND codigo_usuario = %s
        """
        cur.execute(sql_busca, (codigo_instrutor, codigo_usuario))
        instrutor = cur.fetchone()

        if not instrutor:
            print("Instrutor não encontrado nesta conta.")
            return

        sql_treinos = """
            SELECT COUNT(*)
            FROM treino
            WHERE codigo_instrutor = %s
        """
        cur.execute(sql_treinos, (codigo_instrutor,))
        total_treinos = cur.fetchone()[0]

        if total_treinos > 0:
            print(
                f"Não é possível excluir: o instrutor '{instrutor[1]}' só pode ser excluído "
                f"depois que os {total_treinos} treino(s) vinculado(s) forem removidos ou "
                f"transferidos para outro instrutor."
            )
            return
        
        sql_delete = """
            DELETE FROM instrutor
            WHERE codigo = %s AND codigo_usuario = %s
        """
        cur.execute(sql_delete, (codigo_instrutor, codigo_usuario))
        conn.commit()
        print("Instrutor excluído com sucesso!")
    except Exception as erro:
        conn.rollback()
        print(f"Erro ao escluir instrutor: {erro}")
    finally:
        cur.close()
        conn.close()
    

        

