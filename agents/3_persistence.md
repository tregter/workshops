# Persistence










> the continued or prolonged existence of something
> Developer term for "storing things in a database"




























## Why?
- Persistence is the backbone of many chapters in the book, let's review
  - Security [what resources do we have access to?]
  - Observability [how do we see what actually happened?]
  - Governance []
  - Knowledge [What useful context can we inject?]
  - Memory [what happened previously?] [conversation history]
  - Orchestration [handing over data in background jobs*]
  - UX [display data in the frontend]
  - Integration [track tool calls with inputs*]


* A real-world limitation that we deal with is per-minute token limits on providers,
  if you are building for a large usecase you have to start engineering workflows
  far beyond what Langgraph can support.
* We've managed to debug many problems by looking at tool calls and responses. Error-
  handling in these projects are not as straight forward as in traditional code. LLMs
  can easily hallucinate when things go wrong which tends to hide bugs.

























> This is not a crazy new revelation that I had
> I've been taught about 3-tier architectures since 2012
> 3-tier architecture: front-end, back-end, database



                                                                       ┌─────────────────────┐                                  
                                                                       │                     │                                  
                                                                       │                     │                                  
                                                                       │                     │                                  
                                                              ┌──────▶ │         API         │─────┐                            
                                                              │        │                     │     │                            
┌─────────────────────┐          ┌─────────────────────┐      │        │                     │     │     ┌─────────────────────┐
│                     │          │                     │      │        │                     │     │     │                     │
│                     │          │                     │      │        └─────────────────────┘     │     │                     │
│                     │          │                     │      │                                    │     │                     │
│         UI          │─────────▶│    Load Balancer    │──────┤                                    ├────▶│       Database      │
│                     │          │                     │      │                                    │     │                     │
│                     │          │                     │      │        ┌─────────────────────┐     │     │                     │
│                     │          │                     │      │        │                     │     │     │                     │
└─────────────────────┘          └─────────────────────┘      │        │                     │     │     └─────────────────────┘
                                                              │        │                     │     │                            
                                                              └──────▶ │         API         │─────┘                            
                                                                       │                     │                                  
                                                                       │                     │                                  
                                                                       │                     │                                  
                                                                       └─────────────────────┘




























## Let's talk about storage
- In process database vs Database Server

-> postgres
-> mysql

DATABASE SERVERS
------------------------------
IN PROCESS DATABASES

-> sqlite
-> duckdb
























## Options for Today
- Postgres: hard to set up, more scalable.
- Duckdb: easy to set up, single process.
- SQLite: easy to set up, single process.
















->  Let's add persistent memory
