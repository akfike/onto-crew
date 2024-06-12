# main_script.py
from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from ontology_agents import OntoAgents
from ontology_tasks import OntoTasks
from tools.pdf_preprocessing import * # Import the preprocessing function

from dotenv import load_dotenv
load_dotenv()

OpenAIGPT4 = ChatOpenAI(
    model="gpt-4"
)

class OntoCrew:

    def run(self):
        agents = OntoAgents()
        tasks = OntoTasks()


        # ontology_evaluator = agents.ontology_evaluator()
        # ontology_developer = agents.ontology_developer()
        ontology_development_expert = agents.ontology_expert()
        ontology_researcher = agents.existing_ontology_researcher()
        proposal_expert = agents.proposal_expert_agent()
        
        # Preprocess the PDF file
        chunks = read_and_tokenize_pdf('NSF--OKN.pdf')

        results = []
        # all_proposal_tasks = []
        # recent_proposal_task = None
        # for idx, chunk in enumerate(chunks):
        #     # Create a task for each chunk
        #     if idx == 0:
        #         understand_proposal_task_first = tasks.understand_proposal_first(proposal_expert, chunk, idx)
        #         all_proposal_tasks.append(understand_proposal_task_first)
        #         recent_proposal_task = understand_proposal_task_first
        #     else:
        #         understand_proposal_task = tasks.understand_proposal(proposal_expert, chunk, idx, recent_proposal_task)
        #         all_proposal_tasks.append(understand_proposal_task)
        #         recent_proposal_task = understand_proposal_task
        
        context_chunks = read_and_tokenize_txt("last_text.txt")

        # research_existing_ontologies_task = tasks.research_existing_ontologies(ontology_researcher, all_proposal_tasks) 
        
        all_tasks = []
        for chunk in context_chunks:
            research_existing_ontologies_task = tasks.research_existing_ontologies(ontology_researcher, chunk) 
            all_tasks.append(research_existing_ontologies_task)

        ontology_research_task = tasks.research_ontology_development(ontology_development_expert)    

        all_tasks.append(ontology_research_task)
        # all_proposal_tasks.append(research_existing_ontologies_task)
        # all_proposal_tasks.append(ontology_research_task)
        
        crew = Crew(
                agents=[ontology_researcher, ontology_development_expert],
                # agents=[proposal_expert, ontology_researcher, ontology_development_expert],
                # tasks=all_proposal_tasks,
                tasks=all_tasks,
                verbose=True,
                process=Process.hierarchical,
                manager_llm=OpenAIGPT4,
                max_rpm=60  # Set the maximum number of requests per minute
            )
        result = crew.kickoff()
        results.append(result)

        return results


if __name__ == "__main__":

    onto_crew = OntoCrew()
    result = onto_crew.run()
    for res in result:
        print(res)
