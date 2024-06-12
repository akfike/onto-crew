from crewai import Agent

class OntoAgents():

    def proposal_expert_agent(self):
        return Agent(
            role='Proposal Expert',
            goal='To understand fully what our research objectives are and the purpose of our project.',
            verbose=True,
            memory=True,
            backstory=(
                "You are the expert on the research proposal. You can answer any question regarding its purpose, background, methods, and proposed final product."
            ),
            tools = [],
            allow_delegation=True,
        )
    
    def existing_ontology_researcher(self):
        return Agent(
            role='Researcher of Existing Ontologies',
            goal='Identify reusable existing ontologies that can be used for our project to avoid redundant efforts to make a new ontology.',
            verbose=True,
            memory=True,
            backstory=(
                "With a keen eye for detail, you specialize in exploring and identifying existing ontologies made by reputable organizations to streamline development efforts."
            ),
            tools=[],
            allow_delegation=True
        )
    
    def ontology_expert(self):
        return Agent(
            role="Ontology Expert",
            goal="You are an expert in ontologies in terms of what they are, how they are created, what they should consist of, and how they should be formatted.",
            backstory=(
                "You specialize in researching topics on what ontologies are, ontology development, and ontology development pipelines."
            ),
            verbose=True,
            memory=True,
            tools=[],
            allow_delegation=True
        )
    
    def ontology_developer(self):
        return Agent(
            role='Ontology Developer',
            goal=(
                'Create the top-level ontology hierarchy based on the partially provided dataset codebook. '
                'The structure of the codebook is a csv with the columns Question_Code, Long_Description, '
                'Short_Description, Related_Variables, Answer_code, and Answer_meaning.'
                'Question_code refers to the variable name in the dataset. Long_Description refers to the longer description from the codebook of what the variable represents.'
                'Short_Description provides the abbreviated version of the variable\'s description.'
                'Ignore Related_Variables. Answer_code refers to each potential value for a given variable.'
                'Answer_code describes what the answer_code means for that variable.'
            ),
            verbose=True,
            memory=True,
            backstory=(
                "You specialize in reading dataset codebooks and creating the foundational structure of ontologies that integrate the variables in a meaningful way."
            ),
            tools=[],
            allow_delegation=True
        )
    
    def ontology_evaluator(self):
        return Agent(
            role='Ontology Evaluator',
            goal='Your aim is to identify and correct given list of concepts/entities as relevant to our research proposal so that in the end our ontology has only relevant variables for our research project.',
            verbose=True,
            memory=True,
            backstory=('Decisive and critical, you can decide whether or not each class listed is needed or not in our ontology.'),
            tools=[],
            allow_delegation=True
        )
   