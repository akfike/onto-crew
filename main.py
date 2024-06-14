# main_script.py
import os
from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from ontology_agents import OntoAgents
from ontology_tasks import OntoTasks
from tools.pdf_preprocessing import * # Import the preprocessing function

from dotenv import load_dotenv
load_dotenv()

OpenAIGPT3_5 = ChatOpenAI(
    model="gpt-3.5-turbo-0125"
)

class OntoCrew:

    onto_topics = [
        "Substance Use Disorders",
        "Mental Health Disorders",
        "Prescription Drug Misuse",
        "Prevention and Treatment Programs",
        "Epidemiology and Data Analysis",
    ]

    def run(self):
        agents = OntoAgents()
        tasks = OntoTasks()


        # ontology_evaluator = agents.ontology_evaluator()
        # ontology_developer = agents.ontology_developer()

        ontology_development_expert = agents.ontology_expert()
        domain_expert_agent = agents.domain_expert()
        ontology_developer_agent = agents.ontology_developer()
        ontology_subclass_developer_agent = agents.ontology_subclass_developer()
        onto_to_owl_converter_agent = agents.owl_conversion_agent()
        owl_expert_agent = agents.owl_expert()
        agents_for_topics = []
        for topic in self.onto_topics:
            agents_for_topics.append(agents.topic_researcher(topic))
        # ontology_researcher = agents.existing_ontology_researcher()
        # proposal_expert = agents.proposal_expert_agent()
        
        # Preprocess the PDF file
        # chunks = read_and_tokenize_pdf('NSF--OKN.pdf')

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
        
        # context_chunks = read_and_tokenize_txt("last_text.txt")

        # research_existing_ontologies_task = tasks.research_existing_ontologies(ontology_researcher, all_proposal_tasks) 
        
        # all_tasks = []
        # for chunk in context_chunks:
        #     research_existing_ontologies_task = tasks.research_existing_ontologies(ontology_researcher, chunk) 
        #     all_tasks.append(research_existing_ontologies_task)

        # ontology_research_task = tasks.research_ontology_development(ontology_development_expert)    

        # all_tasks.append(ontology_research_task)
        # all_proposal_tasks.append(research_existing_ontologies_task)
        # all_proposal_tasks.append(ontology_research_task)
        
        # crew = Crew(
        #         agents=[ontology_researcher, ontology_development_expert],
        #         # agents=[proposal_expert, ontology_researcher, ontology_development_expert],
        #         # tasks=all_proposal_tasks,
        #         tasks=all_tasks,
        #         verbose=True,
        #         process=Process.hierarchical,
        #         manager_llm=OpenAIGPT4,
        #         max_rpm=60  # Set the maximum number of requests per minute
        #     )
        # result = crew.kickoff()
        # results.append(result)

        # understand_how_to_make_ontology_task = tasks.research_ontology_development(ontology_development_expert)

        # understand_ontology_domain_task = tasks.understand_ontology_domain(domain_expert_agent)

        # create_highest_level_ontology = tasks.identify_and_define_classes(ontology_developer_agent, [understand_how_to_make_ontology_task, understand_ontology_domain_task])

        # define_secondary_level_ontology = tasks.identify_and_define_subclasses(ontology_subclass_developer_agent, [create_highest_level_ontology])

        # research_owl_task = tasks.research_owl(owl_expert_agent)

        # convert_onto_to_owl_task = tasks.convert_ontology_to_owl(onto_to_owl_converter_agent, [research_owl_task, define_secondary_level_ontology])

        topic_tasks = []
        for idx, topic in enumerate(self.onto_topics):
            topic_tasks.append(tasks.research_topic(agents_for_topics[idx], topic))

        crew = Crew(
            agents=agents_for_topics,
            tasks=topic_tasks,
            # agents=[domain_expert_agent, ontology_development_expert, ontology_developer_agent, ontology_subclass_developer_agent, onto_to_owl_converter_agent],
            # tasks = [understand_how_to_make_ontology_task, understand_ontology_domain_task, create_highest_level_ontology, define_secondary_level_ontology, research_owl_task, convert_onto_to_owl_task],
            verbose=True,
            process=Process.hierarchical,
            manager_llm=OpenAIGPT3_5,
            max_rpm=60
        )
        results = crew.kickoff()
        

        return results


if __name__ == "__main__":

    onto_crew = OntoCrew()
    result = onto_crew.run()
    for res in result:
        print(res)
