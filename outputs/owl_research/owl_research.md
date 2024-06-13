```xml
<?xml version="1.0"?>
<!DOCTYPE rdf:RDF [
    <!ENTITY owl "http://www.w3.org/2002/07/owl#" >
    <!ENTITY xsd "http://www.w3.org/2001/XMLSchema#" >
    <!ENTITY rdfs "http://www.w3.org/2000/01/rdf-schema#" >
    <!ENTITY rdf "http://www.w3.org/1999/02/22-rdf-syntax-ns#" >
]>
<rdf:RDF xmlns="http://www.example.org/ontology/"
     xml:base="http://www.example.org/ontology"
     xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
     xmlns:owl="http://www.w3.org/2002/07/owl#"
     xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
     xmlns:xsd="http://www.w3.org/2001/XMLSchema#">
    
    <owl:Ontology rdf:about="">
        <rdfs:label>Example Ontology</rdfs:label>
    </owl:Ontology>
    
    <owl:Class rdf:about="#Person">
        <rdfs:label>Person</rdfs:label>
    </owl:Class>
    
    <owl:Class rdf:about="#Organization">
        <rdfs:label>Organization</rdfs:label>
    </owl:Class>
    
    <owl:ObjectProperty rdf:about="#worksFor">
        <rdfs:domain rdf:resource="#Person"/>
        <rdfs:range rdf:resource="#Organization"/>
        <rdfs:label>worksFor</rdfs:label>
    </owl:ObjectProperty>
    
</rdf:RDF>
```
```