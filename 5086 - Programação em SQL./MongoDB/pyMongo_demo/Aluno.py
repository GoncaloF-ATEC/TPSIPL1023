import pymongo

class Aluno:

    def __init__(self, nome, Turma, _id = None):
        if _id is None:
            self._id = id(self)
        else:
            self._id = _id

        self.nome = nome
        self.Turma = Turma


    @classmethod
    def init_from_dict(cls, dict):
        return cls(dict['nome'], dict['Turma'], dict['_id'])


    def save(self,conn ):

        db = conn['Escola']
        collection_Alunos = db.get_collection('Aluno')
        collection_Alunos.insert_one(self.__dict__)


    def update(self):
        pass


    def __str__(self):
        return f"_id: {self._id}, nome: {self.nome}, Turma: {self.Turma}"