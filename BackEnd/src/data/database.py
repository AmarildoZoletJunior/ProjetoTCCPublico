from sqlalchemy import create_engine,text, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import joinedload
from Database.Base import Base
from config.configuration import configuration
import urllib


class Database:
    def __init__(self):
        self.engine = self.ConnectDataBase()
        if isinstance(self.engine, str):
            print(self.engine)
        else:
            self.Session = sessionmaker(bind=self.engine)
            self.VerifyBaseTables()

    def VerifyBaseTables(self):
        try:
            Base.metadata.create_all(self.engine, checkfirst=True)
        except Exception as e:
            print(f"Ocorreu um erro ao criar as tabelas do banco, verifique a conexão")
            print(str(e))

    def ConnectDataBase(self):
        try:
            params = urllib.parse.quote_plus(
                f"DRIVER={configuration.DRIVER};"
                f"SERVER={configuration.SERVER};"
                f"DATABASE={configuration.DATABASE};"
                f"Trusted_Connection=yes;"
            )
            engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}", echo=False)
            with engine.connect() as connection:
                pass
            return engine
        except Exception as e:
            error_message = f'Ocorreu um erro ao conectar-se ao banco de dados: {str(e)}'
            return error_message
        
        

    def DoSelectWithRelations(self, model, relacoes=None, filtros=None):
        if isinstance(self.engine, str):
            return []

        with self.Session() as session:
            query = session.query(model)
            if filtros:
                query = query.filter_by(**filtros)
            if relacoes:
                for relacao in relacoes:
                    query = query.join(relacao)
            results = query.all()
            dto_list = [self.convert_to_dto(result) for result in results]

            return dto_list


    def DoSelect(self, model, **filters):
        if isinstance(self.engine, str):
            return []
        try:
            with self.Session() as session:
                query = session.query(model).filter_by(**filters)
                results = query.all()
                dto_list = [self.convert_to_dto(result) for result in results]
                return dto_list
        except Exception as e:
            print(f"Erro ao realizar DoSelect: {e}")
            return []

    def objectToDict(self, obj):
        if obj is None:
            return None
        return {column.name: getattr(obj, column.name) for column in obj.__table__.columns}

    def DoInsert(self, model, **data):
        if isinstance(self.engine, str):
            return None
        with self.Session() as session:
            try:
                new_record = model(**data)
                session.add(new_record)
                session.commit()
                return self.objectToDict(new_record)
            except Exception as e:
                session.rollback()
                print(f"Erro ao inserir dados: {e}")
                return None
            
    def DoUpdate(self, model, filters: dict, update_data: dict):
        if isinstance(self.engine, str):
            return None
        
        with self.Session() as session:
            try:
                query = session.query(model).filter_by(**filters)
                updated_count = query.update(update_data, synchronize_session=False)
                session.commit()
                return updated_count
            except Exception as e:
                session.rollback()
                print(f"Erro ao atualizar dados: {e}")
                return None
            
            
    def DoDelete(self, model, **filters):
        if isinstance(self.engine, str):
            return None
        with self.Session() as session:
            try:
                query = session.query(model).filter_by(**filters)
                deleted_count = query.delete(synchronize_session=False)
                session.commit()
                return deleted_count
            except Exception as e:
                session.rollback()
                print(f"Erro ao deletar dados: {e}")
                return None

    
    # def convert_to_dto(self,model_instance):
    #     if isinstance(model_instance, Favorites):
    #         return FavoriteDTO(
    #             model_instance.FVid,
    #             model_instance.FVurl,
    #             model_instance.FVurlImage,
    #             model_instance.FVcreated_at,
    #             self.convert_to_dto(model_instance.category) if model_instance.category else None,
    #             self.convert_to_dto(model_instance.user) if model_instance.user else None,
    #             [self.convert_to_dto(excerpt) for excerpt in model_instance.excerpts],
    #             [self.convert_to_dto(tag.tag) for tag in model_instance.tags_to_favorite]
    #         )
    #     elif isinstance(model_instance, Users):
    #         return UserDTO(
    #             model_instance.USUid,
    #             model_instance.USUsername
    #         )
    #     elif isinstance(model_instance, Category):
    #         return CategoryDTO(
    #             model_instance.CTid,
    #             model_instance.CTname
    #         )
    #     elif isinstance(model_instance, Excerpts):
    #         return ExcerptDTO(
    #             model_instance.ETid,
    #             model_instance.ETExcerpts,
    #             model_instance.ETcreated_at
    #         )
    #     elif isinstance(model_instance, Tags):
    #         return TagDTO(
    #             model_instance.TGid,
    #             model_instance.TGname
    #         )
    #     return None


            
            
            
