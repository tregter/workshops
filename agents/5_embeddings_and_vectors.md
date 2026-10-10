# Embeddings and Vectors


## Resources

->  [3Blue1Brown How word vectors encode meaning](https://www.youtube.com/shorts/FJtFZwbvkI4)
->  [Vector Search with LLMs - Computerphile](https://www.youtube.com/watch?v=YDdKiQNw80c)

## Definitions

->  Embedding: 
An embedding is a representation of data (such as text, images, or audio) as a dense vector of continuous numbers in a high-dimensional space.

It captures the semantic meaning and relationships of the input data. Items with similar meanings or contexts are mapped to vectors that are mathematically close to each other (typically measured by cosine similarity). This enables machine learning models to process, compare, and understand abstract concepts mathematically.

->  Vector
In machine learning and mathematics, a vector is an ordered array or list of numbers. 

It represents a point or a directed magnitude in a multi-dimensional mathematical space. In the context of embeddings, each number in the vector corresponds to a specific dimension or feature of the data, capturing a slice of its semantic meaning.

For example, a simple 3-dimensional vector looks like this: `[0.25, -0.71, 0.88]`. In modern AI models, vectors typically have hundreds or thousands of dimensions (e.g., 768 or 1536).





















▲                                                
│                                                
│                                                
│                                                 
│                                        ██     
│                                            
│                                                
│                                                  
10          ██                              ██
│                                        
│                                                
│                                                
│                                                
│                                                
│                                                
│                                                
│                                                
│                                                
│                                                
│                                                
│                                                
│                                                
│                                                
◍────────────3────────────────────────────────10──▶



[3, 10]
[10, 10]
[10, 12]



















                             Animals───────────────────┐
▲                            │                         │
│                            │                         │
│                            │                         │
│                            │                         │
│  Cars─────────────────┐    │           ██            │
│  │                    │    │                         │
│  │                    │    │                         │
│  │                    │    │                         │
│  │       ██           │    │              ██         │
│  │                    │    │                         │
│  │                    │    │                         │
│  │                    │    └─────────────────────────┘
│  │                    │                               
│  │                    │                               
│  └────────────────────┘                               
│                                                       
│                                                       
│                                                       
│                                                       
│                                                       
│                                                       
│                                                       
│                                                       
◍───────────────────────────────────────────────▶














## Why is this useful?

-> Vector RAG [Retrieval-Augmented Generation] 


Retrieval-Augmented Generation (RAG) is the process of optimizing the output of a large language model, so it references an authoritative knowledge base [KB] outside of its training data sources before generating a response. Large Language Models (LLMs) are trained on vast volumes of data and use billions of parameters to generate original output for tasks like answering questions, translating languages, and completing sentences. RAG extends the already powerful capabilities of LLMs to specific domains or an organization's internal knowledge base, all without the need to retrain the model. It is a cost-effective approach to improving LLM output so it remains relevant, accurate, and useful in various contexts. - [https://aws.amazon.com/what-is/retrieval-augmented-generation/]


Fetch some relevant words to change the words that the LLM returns to you - Ferdi










Hint: 
User prompt RAG isn't always useful on its own. We've found over time that we rely more and more on tools that perform vector searches for us. Example scenario:
->  user uploads a document about cars
->  user prompt "tell me about the latest cars"
->  LLM responds with information from the document
->  user prompt "summarise the uploaded document"
->  this creates a RAG MISS, since the word "document" has nothing to do with the contents in the document.
->  for this case, you would need to provide the LLM with a tool that it can use to load documents




Note: don't confuse RAG with semantic/vector search. There are many ways to do RAG, we typically use Vector RAG.











## Tools of the trade

->  Embedding Models
    ->  Amazon Titan: amazon.titan-embed-text-v2:0

->  Vector Databases / Database Extensions
