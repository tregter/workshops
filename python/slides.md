# python - level 1

Introduction to python for engineers.

---
## covering today

- what problems are we solving?
- virtual environment
- exceptions
- data validation
- environment configuration
- credential provider chain
- the perfect interface for reusable code

---
## not covering today

- variables
- loops
- functions
- ...

---
## why should I care?

AI can do it for me

---
## what problems are we solving?

> "I have a script that runs on my machine. But it needs to work on 8 other machines as well as the dev, qa and prod AWS environments for my client. I also want to re-use this code in the future for another client." - you

---
## how do we achieve this?

- isolated dependencies
- proper error handling
- proper data validation
- inject configuration
- better credential management
- write better code APIs

= Engineering

---
## virtual environment

What is a virtual environment?

> The venv module supports creating lightweight “virtual environments”, each with their own independent set of Python packages installed in their site directories. A virtual environment is created on top of an existing Python installation, known as the virtual environment’s “base” Python, and by default is isolated from the packages in the base environment, so that only those explicitly installed in the virtual environment are available. - [docs](https://docs.python.org/3/library/venv.html)

---
## virtual environment

```
┌─────────────────────────┐
│      Your computer      ├────────────────────────────────────────────────────────────────────────────────────────┐
├─────────────────────────┘                                                                                        │
│                                                                                                                  │
│   ┌─── python3.12 base ──────────────────────────────────────────────────────────────────────────────────────┐   │
│   │                                                                                                          │   │
│   │                                                      ┌─────────────────────────┐                         │   │
│   │                                                    ┌─┤     python3.12 venv     ├──────────────────┐      │   │
│   │     Global Packages                                │ └─────────────────────────┘                  │      │   │
│   │     ---------------                                │                                              │      │   │
│   │                                                    │                                              │      │   │
│   │     - pandas 2.3.1                                 │  Local Packages                              │      │   │
│   │     - duckdb                                       │  --------------                              │      │   │
│   │     - django                                       │                                              │      │   │
│   │                                                    │  - pandas 1.3.4                              │      │   │
│   │                                                    │  - duckdb                                    │      │   │
│   │                                                    │  - django                                    │      │   │
│   │                                                    │                                              │      │   │
│   │                                                    │                                              │      │   │
│   │                                                    │                                              │      │   │
│   │                                                    │                                              │      │   │
│   │                                                    │                                              │      │   │
│   │                                                    │                                              │      │   │
│   │                                                    │                                              │      │   │
│   │                                                    │                                              │      │   │
│   │                                                    │                                              │      │   │
│   │                                                    │                                              │      │   │
│   │                                                    │                                              │      │   │
│   │                                                    │                                              │      │   │
│   │                                                    │                                              │      │   │
│   │                                                    │                                              │      │   │
│   │                                                    │                                              │      │   │
│   │                                                    └──────────────────────────────────────────────┘      │   │
│   │                                                                                                          │   │
│   └──────────────────────────────────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                                                  │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
---
## virtual environment

```
┌─────────────────────────┐
│      Your computer      ├────────────────────────────────────────────────────────────────────────────────────────┐
├─────────────────────────┘                                                                                        │
│                                                                                                                  │
│   ┌─── python3.12 base ──────────────────────────────────────────────────────────────────────────────────────┐   │
│   │                                                                                                          │   │
│   │                                                      ┌─────────────────────────┐                         │   │
│   │                                                    ┌─┤     python3.12 venv     ├──────────────────┐      │   │
│   │     Global Packages                                │ └─────────────────────────┘                  │      │   │
│   │     ---------------                                │                                              │      │   │
│   │                                                    │                                              │      │   │
│   │     - pandas 2.3.1                                 │  Local Packages                              │      │   │
│   │     - duckdb                                       │  --------------                              │      │   │
│   │     - django                                       │                                              │      │   │
│   │                                                    │  - pandas 1.3.4                              │      │   │
│   │                                                    │  - duckdb                                    │      │   │
│   │                                                    │  - django                                    │      │   │
│   │                                                    │                                              │      │   │
│   │                                                    └──────────────────────────────────────────────┘      │   │
│   │                                                                                                          │   │
│   │                                                      ┌─────────────────────────┐                         │   │
│   │                                                    ┌─┤     python3.12 venv     ├──────────────────┐      │   │
│   │                                                    │ └─────────────────────────┘                  │      │   │
│   │                                                    │                                              │      │   │
│   │                                                    │                                              │      │   │
│   │                                                    │  Local Packages                              │      │   │
│   │                                                    │  --------------                              │      │   │
│   │                                                    │                                              │      │   │
│   │                                                    │  - fastapi                                   │      │   │
│   │                                                    │  - duckdb                                    │      │   │
│   │                                                    │  - requests                                  │      │   │
│   │                                                    │                                              │      │   │
│   │                                                    └──────────────────────────────────────────────┘      │   │
│   │                                                                                                          │   │
│   └──────────────────────────────────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                                                  │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---
## discussion point

why is it a bad idea to use global dependencies when developing locally?

---
## what is an exception?

---
## exceptions vs

four major types of error handling in programming?

---
## exceptions vs

four major types of error handling in programming?

- None prescribed (sentinel values)
- Explicit error handling (using multiple return values)
- Sum Types
- Exceptions

---
## error handling in C

```c
struct UserData {
    short   err;
    char    email[MAX_STRING_LEN + 1];
    char    first_name[MAX_STRING_LEN + 1];
};

void do_thing() {
    struct UserData user = fetch_user_data();

    if (user.err == 1) {
        printf("we have an error\n");

    } else if (user.err == 2) {
        printf("we have a different error\n");

    } else {
        printf("we have user data\n");

        printf("User Email: %s\n", user.email);
        printf("User First Name: %s\n", user.first_name);
    }
}
```
---

## error handling in Go

```go
package main

import "fmt"
import "myapp/data"

func main() {
  user, err := data.FetchUser()

  if err != nil {
    fmt.Printf("ERROR: %s", err)
    return
  }

  fmt.Printf(user.Email)
  fmt.Printf(user.Name)
}
```

<!-- ```go

func main() {
	user, err := data.FetchUser()
	if err == nil {
		fmt.Println("Error")
	} else {
		fmt.Println(user.Name)
	}
}
``` -->

---

## error handling in Rust

```rust
pub struct User {
    pub name: String,
    pub email: String,
}

pub enum FetchError {
    UserNotFound,
    UnknownError,
}

fn main() {

    // Result<User, FetchError>
    let user_result = data::fetch_user();

    match user_result {
        Ok(user) => {
            println!("{}", user.name);
            println!("{}", user.email);
        }
        Err(error) => {
            println!("We have an error: {:?}", error);
        }
    }
}
```
---
## what is an exception?

> an exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions


---
## data validation

```
                 ┌──────────────────────────────────────┐
    database     │┌────────┐      ┌───────────────────┐ │
─────record ────▶││        │      │                   │ │    write to
    (dynamo)     ││        │      │                   │ │────database─────▶
                 ││        │      │                   │ │
      JSON       ││validate│      │  business logic   │ │      http
─────(http)─────▶││        │─────▶│                   │ │────response─────▶
                 ││        │      │                   │ │
       API       ││        │      │                   │ │    parquet
◀────Request────▶││        │      │                   │ │──────(S3)───────▶
                 │└────────┘      └───────────────────┘ │
                 └──────────────────────────────────────┘
```

---
## environment variables

```python
import boto3

AWS_ACCESS_KEY_ID = "YOUR_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY = "YOUR_SECRET_ACCESS_KEY"
BUCKET_NAME = "your-s3-bucket-name"
OBJECT_KEY = "path/to/your/file.txt"
LOCAL_FILE_PATH = "downloaded_file.txt"

s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

response = s3.get_object(Bucket=BUCKET_NAME, Key=OBJECT_KEY)
file_bytes = response['Body'].read()

with open(LOCAL_FILE_PATH, "w") as f:
    f.write(file_bytes)

```

---
## config

[The Twelve-Factor App](https://12factor.net)

> An app’s config is everything that is likely to vary between deploys (staging, production, developer environments, etc). This includes:
- Resource handles to the database, Memcached, and other backing services
- Credentials to external services such as Amazon S3 or Twitter
- Per-deploy values such as the canonical hostname for the deploy

> Apps sometimes store config as constants in the code. This is a violation of twelve-factor, which requires strict separation of config from code. Config varies substantially across deploys, code does not.

> A litmus test for whether an app has all config correctly factored out of the code is whether the codebase could be made open source at any moment, without compromising any credentials.
---
## config

*refactor: ./scripts/conf.py*

---
## credential provider chain

[aws credential provider chain](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html#credentialProviderChain)

---
## credential provider chain

```
                             │
                        start here
                             │
                             ▼
                ┌─────────────────────────┐
      │         │       Access Keys       │       │
      │         └────────────┬────────────┘       │
      │                      │                    │
      │                      ▼                    │
      │         ┌─────────────────────────┐       │
      │         │ Assumed Role using STS  │       │
      │         └─────────────────────────┘       │
      │                      │                    │
      │                      ▼                    │
      │         ┌─────────────────────────┐       │
more reusable   │   IAM Identity Center   │  more secure
      │         └─────────────────────────┘       │
      │                      │                    │
      │                      ▼                    │
      │         ┌─────────────────────────┐       │
      │         │  Container Credential   │       │
      │         │        Provider         │       │
      │         └─────────────────────────┘       │
      │                      │                    │
      │                      ▼                    │
      ▼         ┌─────────────────────────┐       ▼
                │  Attached Credentials   │
                └─────────────────────────┘
```
---
## credential provider chain

```python
s3 = boto3.client('s3')
```

---
## credential provider chain

*demo: aws-vault*

---
## the perfect interface
