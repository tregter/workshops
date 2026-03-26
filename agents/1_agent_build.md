# Intro To Agents
## Models & Providers

---
# What is an LLM?

->  I am not smart enough to answer that question
->  But this guy is: 3Blue1Brown
    ->  Large Language Models explained briefly
    ->  https://www.youtube.com/watch?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&v=LPZh9BOjkQs&feature=youtu.be








                              ┌─────────────────┐                                  
                              │                 │                                  
┌──────────────────────┐      │                 │      ┌──────────────────────────┐
│                      │      │                 │      │                          │
│    Wordies go in     │─────▶│       LLM       │─────▶│  Other wordies come out  │
│                      │      │                 │      │                          │
└──────────────────────┘      │                 │      └──────────────────────────┘
                              │                 │                                  
                              └─────────────────┘                                  


->  This is our Axiom




















->  "But can't the agent just...?"
->  "Wordies go in, other wordies come out." Everything else is up to us.


















## Model Landscape

->  Gemini
->  Claude
->  GPT
->  Deepseek
->  Titan
->  Qwen













---
# Where do LLMs live?


->  They usually run in the cloud
->  The people who host the models are called Model Providers
    ->  AWS Bedrock
    ->  GCP
    ->  Deepseek
    ->  Azure
    ->  OpenAI
    ->  Anthropic
    ->  X
    ->  Meta
->  Can I run it on my laptop though?

















->  My Macbook is an M1 Max 32GB
->  deepseek-r1:671b requires about 450GB of memory to run
->  After OS memory has been loaded, we get 450/26 approx 17 Macbooks


->  But we can run smaller models, like deepseek-r1:8b
->  Let's play with Ollama













---
# Let's build some stuff


-> [Ollama Docs](https://docs.ollama.com/api/introduction)



















---
# Covered

->  calling an LLM
    ->  invoke / generate
    ->  chat / messages
->  context
    ->  simulated memory
    ->  simulated tool calls



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







->  My description: An agent is a computer programme that iterates (loops) through LLM calls allowing the model to decide what the
    next best course of action is. Actions are usually presented in the form of tools that allow the programme to read or write
    data. These programmes also typically persists (stores) LLM queries and responses somewhere so that it can be injected into the next 
    iteration of the loop in order to enrich context. This is called "agent memory".
    
->  Tool examples:
    -> get_weather(city) => read data
    -> send_email(recipient, topic, message) => write data



# Memory


# Agent Memory is not In Memory

->  The single biggest misconception we faced
->  My translation: agent memory => conversation history
->  Why can't Agent Memory be stored In Memory?























                                                                       ┌─────────────────────┐                                  
                                                                       │                     │                                  
                                                                       │                     │                                  
                                                                       │                     │                                  
                                                              ┌──────▶ │       Computer      │─────┐                            
                                                              │        │                     │     │                            
┌─────────────────────┐          ┌─────────────────────┐      │        │                     │     │     ┌─────────────────────┐
│                     │          │                     │      │        │                     │     │     │                     │
│                     │          │                     │      │        └─────────────────────┘     │     │                     │
│                     │          │                     │      │                                    │     │                     │
│       Client        │─────────▶│    Load Balancer    │──────┤                                    ├────▶│       Database      │
│                     │          │                     │      │                                    │     │                     │
│                     │          │                     │      │        ┌─────────────────────┐     │     │                     │
│                     │          │                     │      │        │                     │     │     │                     │
└─────────────────────┘          └─────────────────────┘      │        │                     │     │     └─────────────────────┘
                                                              │        │                     │     │                            
                                                              └──────▶ │       Computer      │─────┘                            
                                                                       │                     │                                  
                                                                       │                     │                                  
                                                                       │                     │                                  
                                                                       └─────────────────────┘






# Let's add Memory

->  Add In Memory Agent Memory
















# Let's talk about storage

->  DBMS vs DB
->  In process database
->  Let's add persistent memory






# Tools
TODO


# Embeddings and Vectors
TODO
 
---
# Resources

->  [Vector Search with LLMs - Computerphile](https://www.youtube.com/watch?v=YDdKiQNw80c)


# React
TODO

# Workflows
TODO

# Deployment
TODO
