# database.py
import psycopg2
from dist.config import DB_CONFIG

def get_connection():
    conn = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except psycopg2.Error as e:
        print(f"\n[ERRO DE CONEXÃO]: Não foi possível conectar ao banco de dados.")
        print(f"Detalhes: {e}")
        return None

def execute_query(conn, query):
    if not conn:
        return None, None
    
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            
            headers = [desc[0] for desc in cur.description]
            data = cur.fetchall()
            return headers, data
            
    except psycopg2.Error as e:
        print(f"[ERRO SQL]: Falha ao executar a consulta. Detalhes: {e}")
        return None, None

def relatorio_veterinarios(conn):
    sql = """
    SELECT
        V.nome AS Veterinario,
        V.especialidade,
        COUNT(C.id_consulta) AS Total_Consultas
    FROM
        veterinario V
    LEFT JOIN
        consulta C ON V.id_vet = C.fk_vet
    GROUP BY
        V.nome, V.especialidade
    ORDER BY
        Total_Consultas DESC;
    """
    return execute_query(conn, sql)

def relatorio_consultas_agendadas(conn):
    sql = """
    SELECT
        C.data_hora AS Data_Hora,
        C.status AS Status,
        A.nome AS Animal,
        T.nome AS Tutor,
        V.nome AS Veterinario
    FROM
        consulta C
    JOIN
        veterinario V ON C.fk_vet = V.id_vet
    JOIN
        animal A ON C.fk_animal = A.id_animal
    JOIN
        tutor T ON A.fk_tutor = T.id_tutor
    WHERE
        C.status IN ('AGENDADA', 'REALIZADA')
    ORDER BY
        C.data_hora DESC;
    """
    return execute_query(conn, sql)

def relatorio_gastos_tutor(conn):
    sql = """
    SELECT
        T.nome AS Tutor,
        COALESCE(SUM(P.valor), 0.00) AS Total_Gasto
    FROM
        tutor T
    LEFT JOIN
        pagamento P ON T.id_tutor = P.fk_tutor
    GROUP BY
        T.nome
    ORDER BY
        Total_Gasto DESC;
    """
    return execute_query(conn, sql)