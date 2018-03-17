import csv




def read_csv(filename):
    f = open(filename, 'r', encoding='utf-8')
    reader = csv.reader(f)
    rows=list(reader)
    f.close()
    return rows

def extract_relation(query):
    whereString = query[query.index('{')+1:query.index('}')-1]
    triples=whereString.split(' . ')
    relations=[]
    for triple in triples:
        if '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' in triple:
            continue
        URIs=triple.split(' ')
        URIs=[x for x in URIs if  x!='' and x!=' '] 
        relations.append(URIs[1][1:-1])
    return relations
   
        
    
    
    
if __name__ == "__main__":
    questions=read_csv('LC-QUAD.csv')
    queries=read_csv('Question-SPARQL.csv')
    i=0
    for query in queries:
        questions[i].append(query[1])
        i=i+1
    for question in questions:
        question.append(extract_relation(question[2]))
        
   
        
    
    