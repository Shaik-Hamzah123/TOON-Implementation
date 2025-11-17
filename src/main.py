from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from langgraph.cache.memory import InMemoryCache 
from typing_extensions import TypedDict

from toon_encoder import toon_encode_data
from dummy_api import return_dhs_data

from dotenv import load_dotenv
load_dotenv(override=True)

class MasterState(TypedDict):
    dhs_data: dict
    encoded_data: str   # TOON TEXT STORED HERE
    user_query: str
    chatbot_response: str

def get_data(state: MasterState):
    if not state.get('encoded_data'):
        state["encoded_data"] = return_dhs_data()
    return state

def user_input(state: MasterState):
    state["user_query"] = input("Please enter your query (or 'quit' to exit): ")
    
    if not state["user_query"]:
        state["user_query"] = "Provide a summary of the DHS sessions."
    
    return state

def check_input(state: MasterState):
    if state.get('user_query', '').lower() == "quit":
        return END
    return "chatbot"

def chatbot(state: MasterState):
    model = ChatOpenAI(model_name="gpt-4.1-nano", temperature=0)

    prompt = f"""You are a helpful assistant specializing in analyzing Data Hack Summit 2025 (An AI Conference) session data.

                ## Your Role
                - Answer questions about the DHS session data provided below
                - Provide clear, accurate, and concise responses based on the data
                - If information is not available in the data, clearly state this
                - If the query is unrelated to the session data, politely redirect the user

                ## Available Data
                The following DHS session data is provided in toon-encoded format:
                {state['encoded_data']}         

                ## User Query
                {state.get('user_query', 'No query provided')}

                ## Instructions
                1. Analyze the encoded data carefully to answer the user's question
                2. If the query relates to session data: Provide specific insights, statistics, or summaries as requested
                3. If the query is off-topic: Politely explain that you can only help with questions about the DHS session data
                4. If the data doesn't contain the requested information: Clearly state what information is missing
                5. Format your response in a clear, easy-to-read manner

                Please provide your response:"""
    
    # FOR THE GIVEN ENCODED DATA WE WILL BE SAVING $0.0146 per REQUEST
    # JSON: 17349 tokens
    # TOON: 15892 tokens
    # Savings: 8.4%

    response = model.invoke(prompt)
    state['chatbot_response'] = response.content
    print(f"\nAssistant: {state['chatbot_response']}\n")

    return state

# def build_graph():
#     graph_builder = StateGraph(MasterState)

#     graph_builder.add_node("get_data", get_data)
#     graph_builder.add_node("user_input", user_input)
#     graph_builder.add_node("chatbot", chatbot)

#     graph_builder.set_entry_point("get_data")
#     graph_builder.add_edge("get_data", "user_input")
#     graph_builder.add_conditional_edges(
#         "user_input",
#         check_input,
#         {
#             "chatbot": "chatbot",
#             END: END
#         }
#     )
#     graph_builder.add_edge("chatbot", "user_input")  # Loop back for next query

#     cache = InMemoryCache()
#     graph = graph_builder.compile(cache=cache)

#     return graph

def main():

    graph_builder = StateGraph(MasterState)

    graph_builder.add_node("get_data", get_data)
    graph_builder.add_node("user_input", user_input)
    graph_builder.add_node("chatbot", chatbot)

    graph_builder.set_entry_point("get_data")
    graph_builder.add_edge("get_data", "user_input")
    graph_builder.add_conditional_edges(
        "user_input",
        check_input,
        {
            "chatbot": "chatbot",
            END: END
        }
    )
    graph_builder.add_edge("chatbot", "user_input")  # Loop back for next query

    cache = InMemoryCache()
    graph = graph_builder.compile(cache=cache)
    
    # Initialize with empty state
    result = graph.invoke({
        "encoded_data": None,
        "user_query": "",
        "chatbot_response": ""
    })

    cache.clear()

    print(result)

if __name__ == "__main__":
    main()