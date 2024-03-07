from autogen import config_list_from_json
import autogen

config_list = config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        "model": ["gpt-4", "gpt-4-0314", "gpt-3.5-turbo", 
                "gpt-4-32k", "gpt-4-32k-0314", "gpt-4-32k-v0314"],
    },
)
llm_config = {"config_list": config_list, "cache_seed": None}# cache seed set to None for experiemts otherwise it would just pick from latest cache
user_proxy = autogen.UserProxyAgent(
    name="User_proxy",
    system_message="A human admin.",
    max_consecutive_auto_reply=5,
    code_execution_config={
        # "last_n_messages": 2,
        "work_dir": "code_exec",
        "use_docker": True,
    },  # Please set use_docker=True if docker is available to run the generated code. Using docker is safer than running the generated code directly.
    human_input_mode="NEVER",
)
coder = autogen.AssistantAgent(
    name="Coder",
    # system_message="you are an expert in python programming and will write code based on the requirements",
    llm_config=llm_config,
)
solution_architect = autogen.AssistantAgent(
    name="solution_architect",
    system_message="you are a soulutions architect who will create a solution plan for a given problem. If there are multiple steps involved in solving the problem you will list them down (limit to 5 steps)",
    llm_config=llm_config,
)
groupchat = autogen.GroupChat(agents=[user_proxy, solution_architect, coder ], messages=[], max_round=12)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)


if __name__=="__main__":
    results = user_proxy.initiate_chat(
        manager, message="Find a latest paper about gpt-4 on arxiv and find its potential applications in software."
    )
    print(type(results))
    print(results.chat_history)
    