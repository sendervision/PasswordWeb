from sqlmodel import create_engine, SQLModel, Session

engine = create_engine("sqlite:///database.sqlite")
SQLModel.metadata.create_all(engine)

def db_add_password(data):
    with Session(engine) as session:
        session.add(data)
        session.commit()

