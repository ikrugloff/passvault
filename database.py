from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import select

def select_t_pass():
        db_uri = 'sqlite:///vault.db'
        engine = create_engine(db_uri)
        conn = engine.connect()
        meta = MetaData(engine, reflect=True)
        table = meta.tables['passwords']
        select_st = select([table])
        res = conn.execute(select_st)
        for _row in res:
                print(_row)

def select_mlogin():
        db_uri = 'sqlite:///vault.db'
        engine = create_engine(db_uri)
        conn = engine.connect()
        meta = MetaData(engine, reflect=True)
        table = meta.tables['master']
        select_st = select([table.c.login]).where(
                table.c.id == '1')
        res = conn.execute(select_st)
        for _row in res:
                return _row[0]

def select_mpassword():
        db_uri = 'sqlite:///vault.db'
        engine = create_engine(db_uri)
        conn = engine.connect()
        meta = MetaData(engine, reflect=True)
        table = meta.tables['master']
        select_st = select([table.c.password]).where(
                table.c.id == '1')
        res = conn.execute(select_st)
        for _row in res:
                return _row[0]



