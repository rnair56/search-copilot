from autogen import config_list_from_json
import autogen

config_list = config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        "model": ["gpt-4", "gpt-4-0314", "gpt-3.5-turbo", 
                "gpt-4-32k", "gpt-4-32k-0314", "gpt-4-32k-v0314"],
    },
)
llm_config = {"config_list": config_list, "cache_seed": 42}
user_proxy = autogen.UserProxyAgent(
    name="User_proxy",
    system_message="A human admin.",
    max_consecutive_auto_reply=5,
    code_execution_config={
        # "last_n_messages": 1,
        "work_dir": "code_exec",
        "use_docker": False,
    },  # Please set use_docker=True if docker is available to run the generated code. Using docker is safer than running the generated code directly.
    human_input_mode="TERMINATE",
)
coder = autogen.AssistantAgent(
    name="Coder",
    llm_config=llm_config,
)
pm = autogen.AssistantAgent(
    name="Product_manager",
    system_message="Creative in software product ideas.",
    llm_config=llm_config,
)
groupchat = autogen.GroupChat(agents=[user_proxy, coder, pm], messages=[], max_round=12)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)


if __name__=="__main__":
    results = user_proxy.initiate_chat(
        manager, message="Find a latest paper about gpt-4 on arxiv and find its potential applications in software."
    )
    print(type(results))
    print(results.chat_history)
    