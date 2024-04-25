import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.llms import AzureOpenAI
from langchain_openai import AzureChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

load_dotenv()
model = AzureChatOpenAI(temperature=0.6,
                        deployment_name="gpt-4")

def generate_sport_team_name_and_branding_strategy(sport):
    prompt_template_name = PromptTemplate(
        input_variables = ['sport'],
        template = "I am establishing new sports team to play {sport}. Suggest an epic name for this."
    )

    name_chain = LLMChain(llm=model, prompt=prompt_template_name, output_key = "Name")

    prompt_template_branding = PromptTemplate(
        input_variables = ['Name'],
        template = "Suggest branding strategy for my sport team named {Name}. Provide at least the name of the arena, the name of the mascot, and the style of the team's logo."
    )

    branding_chain = LLMChain(llm=model, prompt=prompt_template_branding, output_key="branding_info")
    
    chain = SequentialChain(
        chains = [name_chain, branding_chain],
        input_variables = ['sport'],
            output_variables = ['Name', 'branding_info']
    )

    response = chain({'sport' : sport})    
    
    return response

print(generate_sport_team_name_and_branding_strategy("Hockey"))