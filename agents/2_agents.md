# What is an Agent?

->  You've probably seen something like this before.

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







->  My description: An agent is a programme that iterates (loops) through LLM calls allowing the model to decide what the
    next best course of action is. Actions are usually presented in the form of tools that allow the programme to read or write
    data. These programmes also typically persists (stores) LLM queries and responses somewhere which can be injected into the next 
    iteration of the loop in order to enrich context. This is called "agent memory".
    
->  Tool examples:
    -> get_weather(city) => read data
    -> send_email(recipient, topic, message) => write data
