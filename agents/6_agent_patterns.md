# Agent Patterns

## Resources
- https://docs.langchain.com/oss/python/langgraph/workflows-agents


## What is an Agent?


                       ┌──────────────┐                       
                       │              │                       
                       │     LLM      │                       
                       │              │                       
                       └──────────────┘                       
                               ▲                              
                               │                              
                               │                              
┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│              │       │              │       │              │
│    Tools     │◀──────│    Agent     │──────▶│     Data     │
│              │       │              │       │              │
└──────────────┘       └──────────────┘       └──────────────┘
                               │                              
                               │                              
                               ▼                              
                       ┌──────────────┐                       
                       │              │                       
                       │    Memory    │                       
                       │              │                       
                       └──────────────┘







->  My description: An agent is a computer programme that iterates (loops) through LLM calls allowing the model to decide what the
    next best course of action is. Actions are usually presented in the form of tools that allow the programme to read or write
    data. These programmes also typically persists (stores) LLM queries and responses somewhere so that it can be injected into the next 
    iteration of the loop in order to enrich context. This is called "agent memory".
    
->  Tool examples:
    -> get_weather(city) => read data
    -> send_email(recipient, topic, message) => write data


## Insight
- "Agent" is the single most incorrectly used term in this space (including by me). If you are building
  a Workflow or Orchestration pattern you are not necessarily building an Agent.
- Confusingly though, and Orchestration pattern can be made up of multiple Agents.

## Workflows
- Prompt Chaining.
- LLM usage is embedded in pre-defined code paths.

## Orchestration
- Graphs.
- LLM directs control-flow through pre-defined code paths.

## Agent
- ReAct [Reasoning + Acting].
- LLM directs its own actions based on environmental feedback.
