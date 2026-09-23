from pydantic import BaseModel
class SubQuery(BaseModel): id:str; text:str; intent:str; entities:list[str]=[]
