#   Intro to Agents
##  Intro to Computers and Programming


                                  _____
                                 |     |
                                 | | | |  --- Hi
                                 |_____|
                           ____ ___|_|___ ____
                          ()___)         ()___)
                          // /|           |\ \\
                         // / |           | \ \\
                        (___) |___________| (___)
                        (___)   (_______)   (___)
                        (___)     (___)     (___)
                        (___)      |_|      (___)
                        (___)  ___/___\___   | |
                         | |  |           |  | |
                         | |  |___________| /___\
                        /___\  |||     ||| //   \\
                       //   \\ |||     ||| \\   //
                       \\   // |||     |||  \\ //
                        \\ // ()__)   (__()
                              ///       \\\
                             ///         \\\
                           _///___     ___\\\_
                          |_______|   |_______|

---
# Overview
- Why should we care about software?
- What are agents?
- High-level overview of computers and programming concepts.
  - Terminals
  - Python
  - Git
  - Aws

---
# About Me

-  Software Engineering background
-  Practical and precise, not theoretical or imaginative
-  If you can't build it you don't understand it
-  I speak a slightly different language
    -  eg. "agent memory" => "conversation scoped database entries injected into a prompt to provide the LLM with context"
-  No magic, just engineering
-  Don't like slideshows

---
# How you normally learn things

-  Top Down
-  Fastest path to product
-  Leaves you feeling excited and confused

---

                                       ┌────────────────────┐                    
                                       │                    │                    
                                       │                    │                    
                                       │                    │                    
                                       │   Model Provider   │                    
                                       │                    │                    
                                       │             ┌──────┼─────────────┐      
                           ┌───────────┼────────┐    │      │             │      
                           │           │        │    │      │             │      
                           │           └────────┼────┼──────┘             │      
                           │                    │    │        RAG         │      
                           │     Embedding      │    │                    │      
                           │                    │    │                    │      
                ┌──────────┼─────────┐  ┌───────┼────┼───────┐            │      
┌───────────────┼────┐     │  ┌──────┼──┼───────┼────┼───┐   │            │      
│               │    │     │  │      │  │       │    └───┼───┼────────────┘      
│               │    │     └──┼──────┼──┼───────┘        │   │                   
│               │    │  Memory│      │  │   Knowledge Base ┌─┼──────────────────┐
│    Token Limits    │        │      │  │                │ │ │                  │
│               │    │        │      │  │Agent           │ │ │                  │
│               │    │   ┌────┼──────┼──┼─────┐          │ │ │                  │
│      ┌────────┼────┼───┼──┐ │      │  │     │          │ │ │     Model        │
│      │        └────┼───┼──┼─┼──────┘  └─┬───┼──────────┼─┼─┴─┐                │
└──────┼─────────────┘   │  │ │           │   │          │ │   │                │
       │                 │  │ │Langgraph  │   │          │ │   │                │
       │      Context    │  │ │           │   │          │ │   │                │
       │                 │  │ └───────────┼───┼─Langchain┘ └───┼────────────────┘
       │                 │  │             │   │                │                 
       │                 │  │             │   │                │                 
       │                 └──┼─────────────┼───┘                │                 
       └────────────────────┘             │                    │                 
                                          └────────────────────┘                 
                                                          
---
# How I teach things

-  Bottom up
-  Reduce noise (eg. build by hand)
-  Approach each topic in isolation
-  Leaves you feeling bored and empowered

---

┌───────────────┐                                                                        ┌───────────────┐                                            
│  Foundations  │                                                                        │     Noise     │                                            
├───────────────┴────────────────────────────────────────────────────────────────────┐   ├───────────────┴───────────────────────────────────────────┐
│                                                                                    │   │                                                           │
│                                                                                    │   │                                                           │
│                                                                                    │   │                                                           │
│       ┌────────────────────┐  ┌────────────────────┐  ┌────────────────────┐       │   │                                                           │
│       │                    │  │                    │  │                    │       │   │                                                           │
│       │                    │  │                    │  │                    │       │   │                                                           │
│       │                    │  │                    │  │                    │       │   │                                                           │
│       │     Embedding      │  │   Knowledge Base   │  │     Workflows      │       │   │                                                           │
│       │                    │  │                    │  │                    │       │   │      ┌────────────────────┐   ┌────────────────────┐      │
│       │                    │  │                    │  │                    │       │   │      │                    │   │                    │      │
│       │                    │  │                    │  │                    │       │   │      │                    │   │                    │      │
│       │                    │  │                    │  │                    │       │   │      │                    │   │                    │      │
│       └────────────────────┘  └────────────────────┘  └────────────────────┘       │   │      │     Langchain      │   │      Strands       │      │
│                                                                                    │   │      │                    │   │                    │      │
│       ┌────────────────────┐  ┌────────────────────┐  ┌────────────────────┐       │   │      │                    │   │                    │      │
│       │                    │  │                    │  │                    │       │   │      │                    │   │                    │      │
│       │                    │  │                    │  │                    │       │   │      │                    │   │                    │      │
│       │                    │  │                    │  │                    │       │   │      └────────────────────┘   └────────────────────┘      │
│       │       Memory       │  │       Agent        │  │        RAG         │       │   │      ┌────────────────────┐   ┌────────────────────┐      │
│       │                    │  │                    │  │                    │       │   │      │                    │   │                    │      │
│       │                    │  │                    │  │                    │       │   │      │                    │   │                    │      │
│       │                    │  │                    │  │                    │       │   │      │                    │   │                    │      │
│       │                    │  │                    │  │                    │       │   │      │     Langgraph      │   │      Openclaw      │      │
│       └────────────────────┘  └────────────────────┘  └────────────────────┘       │   │      │                    │   │                    │      │
│                                                                                    │   │      │                    │   │                    │      │
│       ┌────────────────────┐  ┌────────────────────┐  ┌────────────────────┐       │   │      │                    │   │                    │      │
│       │                    │  │                    │  │                    │       │   │      │                    │   │                    │      │
│       │                    │  │                    │  │                    │       │   │      └────────────────────┘   └────────────────────┘      │
│       │                    │  │                    │  │                    │       │   │                                                           │
│       │       Model        │  │   Model Provider   │  │      Context       │       │   │                                                           │
│       │                    │  │                    │  │                    │       │   │                                                           │
│       │                    │  │                    │  │                    │       │   │                                                           │
│       │                    │  │                    │  │                    │       │   │                                                           │
│       │                    │  │                    │  │                    │       │   │                                                           │
│       └────────────────────┘  └────────────────────┘  └────────────────────┘       │   │                                                           │
│                                                                                    │   │                                                           │
│                                                                                    │   │                                                           │
└────────────────────────────────────────────────────────────────────────────────────┘   └───────────────────────────────────────────────────────────┘



---
# What are we going to do?

Build an agent from scratch using nothing but our wits, some elbow grease, and a Large Language Model.

Along the way we will learn about:
-  Models
-  Model Providers
-  Agent Loops and other patterns
-  Memory
-  Tools
-  Chunking, Vectors & Embeddings
-  RAG
-  and whatever else you want to


---
# Advice

Ask questions. I know many things about this topic. You can know them too.


---
# What are we doing today?

## Aim
Briefly get everyone up to speed with computers, programming, and AWS.

## Goal
Set you up for further self study, the topics we are going to discuss can take years to master.

## Advice for coding agents
- Coding agents are useful tools, but they are **very** far away from being able to debug
  a containerised production deployment or making sense of networking constraints in an enterprise
  cloud environment.
- Make an effort to understand the limitations. Agents code in isolation. Code never runs in isolation.
- If you don't know what you're doing, you will get stuck very quickly. Then you'll have to pay
  someone like me a lot of money to make you unstuck.
- Use coding agents for guidance, not action.
- I see *a lot* of AI generated code. Trust me on this one.

---
# Why do I need to know about programming to build Agents?
-  What is an Agent?
-  What is an LLM and how does an agent invoke it?
-  What does an LLM consume to transform?

┌──────────────────┐                     ┌──────────────────┐
│                  │                     │                  │
│      Agent       │─────────??─────────▶│       LLM        │
│                  │                     │                  │
└──────────────────┘                     └──────────────────┘

---

┌──────────────────┐                       ┌──────────────────┐
│                  │        [data]         │                  │
│ Agent Programme  │──────── http ────────▶│    LLM Server    │
│                  │                       │                  │
└──────────────────┘                       └──────────────────┘


---

-  An agent is a computer Programme.
-  Large Language Models are usually exposed as HTTP servers.
-  Programmes can invoke Large Language Models through HTTP endpoints.
-  Large Language Models consume **data** and they return **data**.

-  The transformation of data is the only purpose of any program. [Mike Acton]
-  Meaning that the ideal way to work with LLMs is through software.

---
Think of an Agent as a data-broker for your LLM, eg.
-  is the user allowed to access this data?
-  is the LLM allowed to access this data?
-  is this data relevant to the question being asked?

---

                                ┌──────────────────┐
                                │                  │
                                │                  │
                                │    Relational    │
                                │     Database     │
                                │                  │
                                │                  │
                                │                  │
                                └──────────────────┘
                                         ▲
                                         │
                                         │
┌──────────────────┐            ┌────────┴─────────┐                     ┌──────────────────┐
│                  │            │                  │                     │                  │
│                  │            │                  │                     │                  │
│                  │            │                  │                     │                  │
│User Instructions │──────────▶ │ Agent Programme  │────────http────────▶│    LLM Server    │
│                  │            │                  │                     │                  │
│                  │            │                  │                     │                  │
│                  │            │                  │                     │                  │
└──────────────────┘            └──────────────────┘                     └──────────────────┘
                                         │
                                         │
                                         ▼
                                ┌──────────────────┐
                                │                  │
                                │                  │
                                │                  │
                                │   Vector Store   │
                                │                  │
                                │                  │
                                │                  │
                                └──────────────────┘

---
Agentic AI belongs to Subject Matter Experts who can effectively wield Large Language Models. [me]


---
# The Terminal

-  a text based interface for working with your computer
-  user interfaces are for humans, but most programmes don't need user interfaces
-  agents don't need user interfaces

---
# What shells are available?

-> Windows: Powershell
-> Mac/Linux: sh, bash, zsh

---
# Basic Navigation

->  pwd [present working directory]  : where am I right now?
->  ls [list]                        : what files and folders are around me?
->  cd [change directory]            : go somewhere else
->  clear                            : clear my screen
->  rm                               : delete a file

->  code /path                       : to open a VsCode project (if you've installed shell command)
->  zed /path                        : to open a VsCode project (if you've installed shell command)


->  ask your AI assistant to help you create shortcuts [aliases].
---
# Good reasons to become comfortable with the terminal

->  Faster.
->  Less noise.
->  Requirement if you are working on remote servers.

---
# Code Editor

->  Code Editors just edit text, everything else are nice-to-haves.
->  I wrote my first programme in Notepad.
->  *Every* programme is just text being interpreted by your computer.

---
# What are the nice to haves?
->  File-tree explorer
->  File search
->  Syntax highlighting
->  Jump-to-definition
->  Static Analysis
->  Debugging tools
->  Terminal
->  Coding agents
->  Buffer search
->  Fulltext search
->  Git tools
->  Collaborative Editing
->  Extensions

---
# What editors are out there for me?
From Hardcore to Dummy Mode

->  Vim
->  Neovim
->  Emacs
->  VSCode / Zed
->  Jetbrains range
->  VSCode AI Forks
    ->  Cursor
    ->  Windsurf
    ->  Antigravity
    ->  Kiro

---
# Python

## Installation

->  I highly recommend using uv as your Python package manager: https://docs.astral.sh/uv/
    ->  It allows you to install different versions of Python
    ->  It is also a package manager

--- 
## Essence of Programming

->  Variables of different types
->  Conditional branching
->  Iteration / Looping
->  Abstraction (packaging logic into functions)


--- 
## Object Orientation

->  Classes and Objects

---

Do we continue down the Python road?
