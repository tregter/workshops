# Models & Providers










## What is an LLM?

->  I am not smart enough to answer that question
->  But this guy is: 3Blue1Brown
    ->  Large Language Models explained briefly

























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
























┌────────────┐                                                                                           
│   Memory   │───┐                                                                                       
└────────────┘   │                                                                                       
                 │                                                                                       
┌────────────┐   │                                                                                       
│  Context   │───┤                                  ┌─────────────────┐                                  
└────────────┘   │                                  │                 │                                  
                 │    ┌──────────────────────┐      │                 │      ┌──────────────────────────┐
┌────────────┐   │    │                      │      │                 │      │                          │
│    RAG     │ ──┼───▶│    Wordies go in     │─────▶│       LLM       │─────▶│  Other wordies come out  │
└────────────┘   │    │                      │      │                 │      │                          │
                 │    └──────────────────────┘      │                 │      └──────────────────────────┘
┌────────────┐   │                                  │                 │                                  
│     KB     │───┤                                  └─────────────────┘                                  
└────────────┘   │                                                                                       
                 │                                                                                       
┌────────────┐   │                                                                                       
│  Security  │───┘                                                                                       
└────────────┘                                                                                           















->  "But can't the agent just...?"
->  "Wordies go in, other wordies come out." Everything else is up to us.


















## Model Landscape

->  Gemini
->  Claude
->  GPT
->  Deepseek
->  Titan (embed)
->  Qwen
->  Llama
















---
## Where do LLMs live?


->  They usually run in the cloud
->  The people who host the models are called Model Providers
    ->  AWS Bedrock
    ->  GCP Vertex Model Garden
    ->  Azure AI Foundary
    ->  OpenAI
    ->  Deepseek
    ->  Anthropic
    ->  Spacex ??
->  Can I run it on my laptop though?

















->  My Macbook is an M1 Max 32GB
->  deepseek-r1:671b requires about 450GB of memory to run
->  After OS memory has been loaded, we get 450/26 approx 17 Macbooks
->  This would likely execute at seconds/token instead of tokens/second 


->  But we can run smaller models, like qwen3:8b













---
## Let's build some stuff

Cover:
->  calling an LLM
->  context
    ->  simulated memory
    ->  simulated tool calls
