# Memory and Streaming
## Memory


Insight: Memory is not In Memory

->  The single biggest misconception we faced
->  My translation: memory => conversation history
->  Why can't Memory be stored In Memory?






























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






## Let's add Memory

->  Add In-Memory chat Memory [conversation history]


## Stream the response

->  this makes LLM code at least 2x harder (especially for frontend code), think carefully before 
    creating streaming responses
