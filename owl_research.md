```
<?xml version="1.0"?>
<!DOCTYPE rdf:RDF [
    <!ENTITY xsd "http://www.w3.org/2001/XMLSchema#">
    <!ENTITY owl "http://www.w3.org/2002/07/owl#">
    <!ENTITY rdfs "http://www.w3.org/2000/01/rdf-schema#">
    <!ENTITY rdf "http://www.w3.org/1999/02/22-rdf-syntax-ns#">
]>
<rdf:RDF xmlns="http://example.org/substance_use_disorders#"
     xml:base="http://example.org/substance_use_disorders"
     xmlns:rdfs="&rdfs;"
     xmlns:owl="&owl;"
     xmlns:xsd="&xsd;"
     xmlns:rdf="&rdf;">
     
    <!-- Subclasses of Substance Use Disorders -->
    <owl:Class rdf:about="#SubstanceUseDisorder"/>
    <owl:Class rdf:about="#AlcoholUseDisorder">
        <rdfs:subClassOf rdf:resource="#SubstanceUseDisorder"/>
    </owl:Class>
    <owl:Class rdf:about="#OpioidUseDisorder">
        <rdfs:subClassOf rdf:resource="#SubstanceUseDisorder"/>
    </owl:Class>
    <owl:Class rdf:about="#StimulantUseDisorder">
        <rdfs:subClassOf rdf:resource="#SubstanceUseDisorder"/>
    </owl:Class>
    <!-- Additional subclasses go here -->
    
    <!-- Properties -->
    <owl:ObjectProperty rdf:about="#hasSubstanceUseDisorder"/>
    <owl:ObjectProperty rdf:about="#hasSubstanceType"/>
    
    <!-- Individuals -->
    <owl:NamedIndividual rdf:about="#Individual1">
        <rdf:type rdf:resource="#AlcoholUseDisorder"/>
        <hasSubstanceType rdf:resource="#Alcohol"/>
    </owl:NamedIndividual>
    
</rdf:RDF>
```