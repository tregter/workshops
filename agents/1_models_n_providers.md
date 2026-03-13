# Models & Providers









------------------------------------
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


-> This is our Axiom [*1]




















->  "But can't the agent just...?"
->  "Wordies go in, other wordies come out." Everything else is up to us.


















## Popular Models
->  Claude
->  Gemini
->  GPT
->  Deepseek
->  Titan
->  Qwen













------------------------------------
# Where do LLMs live?


->  They usually run in the cloud
->  The people who run them are called Model Providers
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
