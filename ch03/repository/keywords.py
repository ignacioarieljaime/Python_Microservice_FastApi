
from uuid import UUID
from typing import List

keywords_recipe = dict()

class KeywordRepository:
    
    def __init__(self):
        pass 
    
    def insert_keywords(self, id:UUID, keywords: List[str]):
        keywords_recipe[id] = keywords
        
    def add_keywords(self, id:UUID, keyword:str): 
        keywords_recipe[id].push(keyword)
        
    def query_keywords(self, id:UUID):
        return keywords_recipe[id]
    
    def query_all_keywords(self):
        return keywords_recipe
    