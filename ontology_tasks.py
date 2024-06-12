# ontology_tasks.py
from crewai import Task
from dotenv import load_dotenv
import os
from crewai_tools import SerperDevTool

load_dotenv()
serper_api_key = os.getenv("SERPER_API_KEY")

search_tool = SerperDevTool()

class OntoTasks:

    def understand_proposal_first(self, agent, chunk, chunk_number):
        description = (
            f"Read the following chunk of the proposal text and understand the domain and scope of the proposed ontology. "
            f"Proposal text: {chunk}"
        )
        expected_output = 'A paragraph or two explaining the domain and scope of the research project.'

        return Task(
            description=description,
            expected_output=expected_output,
            tools=[],  # Ensure this is a list
            agent=agent,
            output_file=f"proposal_summary_{chunk_number}.md"
        )
    
    def understand_proposal(self, agent, chunk, chunk_number, context):
        description = (
            f"Read the following chunk of the proposal text and understand the domain and scope of the proposed ontology. "
            f"Proposal text: {chunk}"
        )
        expected_output = 'A paragraph or two explaining the domain and scope of the research project.'

        return Task(
            description=description,
            expected_output=expected_output,
            tools=[],  # Ensure this is a list
            agent=agent,
            context=[context],  # Ensure this is properly formatted, e.g., a dictionary or list
            output_file=f"proposal_summary_{chunk_number}.md"
        )
    
    def research_existing_ontologies(self, agent, context):
        return Task(
            description=(
                """ Given the context from the previous tasks implemented to 
                understand the research proposal, this task involves searching the internet and research literature
                for existing ontologies that relate to our research topic on social determinants of health
                and justice."""
            ),
            expected_output='A report on existing ontologies that can be reused. For each presented ontology the format should be like this: Name: Example Ontology, Link: www.exampleonto.com, Summary: This ontology includes concepts such as a, b, c,. ',
            tools=[search_tool],
            agent=agent,
            context=context,
            output_file="existing_ontologies_report.md"
        )
    
    def develop_ontology_from_codebook(self, agent, chunk, chunk_number):
        return Task(
            description=(
                f"Given a part of the codebook for a particular dataset, identify what elements would make up the topmost level of an ontology made for this dataset. Codebook part: {chunk}"
            ),
            expected_output='A list of potential topmost level concepts or entities',
            tools=[],
            agent=agent,
            output_file=f"ontology_top_level_{chunk_number}.txt"
        )
    
    def evaluate_ontology(self, agent, proposal_chunk, proposal_chunk_number, ontology_chunk):
        return Task(
            description = (
                f"Given a summary of the research proposal, identify if the listed concepts are relevant for our ontology. "
                f"If they aren't, either propose a similar concept that fits better or just remove it completely. "
                f"Research proposal summary: {proposal_chunk} "
                f"Ontology: \n {ontology_chunk}"
            ),
            expected_output='A finalized list of potential topmost level concepts or entities',
            tools=[],
            agent=agent,
            output_file=f"ontology_top_level_{proposal_chunk_number}.txt"
        )