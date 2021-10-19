def listarTerminos(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")


listarTerminos(IDE="Integrated Development Enviroment", PK="Primary Key")
listarTerminos(DBMS="DataBase Managment System")