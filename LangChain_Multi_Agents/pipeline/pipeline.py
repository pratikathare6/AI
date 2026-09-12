from agents.agents import critic_chain,writer_chain,build_reader_agent,build_search_agent


def run_research_pipeline(topic : str)-> str:

    state = {}

    print("\n"+" ="*50)
    print("Step 1 - Search agent is working...")
    print("="*50)

    search_agent = build_search_agent()

    search_results =  search_agent.invoke({

        "messages":[("user", f'Find recent, reliable and detailed information about {topic}')]
    })

    state["search_results"] = search_results['messages'][-1].content[:400]

    print("\n search result ",state["search_results"])

    print("\n"+" ="*50)
    print("Step 2 - Reader agent is working...")
    print("="*50)

    reader_agent = build_reader_agent()

    reader_result = reader_agent.invoke({
        "messages":[(
            "user",
            f"Based on the following search results about '{topic}', "
            f"pick the most relevent URL and scrape it for a deeper content. \n\n"
            f"search results: \n {state['search_results'][:300]}"
        )]
    })

    state['scraped_content'] = reader_result['messages'][-1].content[:300]

    print("\n scraped content ",state["scraped_content"])

    print("\n"+" ="*50)
    print("Step 3 - Writer is drafting the report...")
    print("="*50)

    research_combined = (

        f"SEARCH RESULTS: \n {state['search_results']} \n\n"
        f"SCRAPED CONTENT: \n {state['scraped_content']}" 
    )

    state['report'] = writer_chain.invoke({

        "topic" : topic,
        "reaserch" : research_combined
    })


    print("\n Final Reprt\n",state["report"])

    print("\n"+" ="*50)
    print("Step 3 - Writer is drafting the report...")
    print("="*50)

    state["feedback"] = critic_chain.invoke({

        "report": state["report"]
    })

    print("\n Critic Report \n",state["feedback"])

    return state