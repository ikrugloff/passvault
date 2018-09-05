from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import select

def db_get_table(table_name):
    db_uri = 'sqlite:///vault.db'
    engine = create_engine(db_uri)
    conn = engine.connect()
    meta = MetaData(engine, reflect=True)
    table = meta.tables[table_name]
    return table, conn

def select_row(table_name, select_st):
    table, conn = db_get_table(table_name)
    res = conn.execute(select_st)
    return res
    # for _row in res:
    #     print(_row)


def select_t_pass():
        table, conn = db_get_table('passwords')
        select_st = select([table])
        res = conn.execute(select_st)
        for _row in res:
                print(_row)

def select_mlogin():
        table, conn = db_get_table('master')
        select_st = select([table.c.login]).where(
                table.c.id == '1')
        res = conn.execute(select_st)
        for _row in res:
                return _row[0]

def select_mpassword():
        table, conn = db_get_table('master')
        select_st = select([table.c.password]).where(
                table.c.id == '1')
        res = conn.execute(select_st)
        for _row in res:
                return _row[0]
