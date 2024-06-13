An ontology, in the context of computer science and information science, is a formal representation of knowledge within a domain. It involves defining concepts, relationships, attributes, and constraints of a specific subject area. Ontologies aim to model a domain by capturing the essential entities, their properties, and the relationships among them.

The purpose of ontologies are manifold. They are used to share common understanding of the structure of information among people or software agents, to enable reuse of domain knowledge, to make domain assumptions explicit, to separate domain knowledge from the operational knowledge, and to analyze domain knowledge.

The typical structure of an ontology involves the following components:
1. Classes: These are the concepts in the domain. They are typically organized in a taxonomic (subclass–superclass) hierarchy.
2. Instances: These are the actual objects in the specific domain that the ontology is modeling.
3. Properties: These are the aspects, characteristics, attributes, or relations that the instances or classes can have.

The common practices of developing ontologies include:
1. Defining Classes in the Ontology: Identifying the highest level of classes based on the domain and the scope of the ontology.
2. Arranging the Classes in a Taxonomic Hierarchy: Defining subclasses of a class, considering that a class can have multiple subclasses and a subclass can have multiple superclasses.
3. Defining the Properties: Identifying the properties or attributes of the classes and the type of the property values.
4. Filling in the Property Values for Instances: Assigning values to the properties for each instance of the class.

Ontologies can be developed using various ontology languages like RDF(S), OWL, and SKOS. Ontology development tools like Protégé, OntoEdit, and SWOOP facilitate the creation, editing, and browsing of ontologies.

Ontology development also follows iterative refinement, where the ontology is gradually improved and expanded over time. It also involves collaboration and agreement among multiple stakeholders, as the ontology needs to represent a shared understanding of the domain.

A well-formatted ontology should follow the below structure for the effective organization and understanding of the knowledge domain.

1. Namespace Declaration: This is the first section of the ontology. It defines the scope of the ontology and the unique identifier for each concept.

2. Concept/Class Definition: This section includes all the concepts or classes that are part of the ontology. Each concept should be clearly defined.

3. Properties/Relations Definition: This section defines the relationships or properties that link the classes. This can include both object and datatype properties.

4. Constraints/Axioms: These are rules or restrictions that apply to the classes and properties in the ontology.

5. Annotations: These are additional information or notes about the classes and properties. They can include comments, labels, or other metadata.

6. Individuals/Instances: This section includes specific instances or examples of the classes. 

A well-formatted ontology should be readable and understandable, with clear definitions and logical organization. It should effectively represent the knowledge domain, with comprehensive coverage of all relevant concepts, relationships, and constraints. It should also be extensible, allowing for the addition of new concepts and relations as the domain knowledge evolves. Lastly, it should be interoperable, enabling it to be integrated with other ontologies and data sources.