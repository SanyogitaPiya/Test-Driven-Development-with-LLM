# Best Practices for Test Driven Development Using LLMs
Welcome to the GitHub page dedicated to our research on Test-Driven Development (TDD) using large language models, specifically focusing on ChatGPT. In this repository, we explore the intersection of large language models with software testing methodologies, providing guidelines and recommendations for effective TDD practices when leveraging large language models like ChatGPT.

## Features and Key Components

- To evaluate the efficacy of TDD with ChatGPT, we selected a set of problems from LeetCode, a platform renowned for its algorithmic challenges. 
- Our experiments leverage the GPT-3.5 architecture,a state-of-the-art language model developed by OpenAI, to analyze and generate test cases. 
- We explore various software testing strategies like Input Space Partitioning techniques to ensure thorough testing coverage across different input domains



## Tech

This research uses a number of open source projects and tools:

- [LeetCode] - The online platform for coding and algorithmic problems intended for users of different skill set
- [Pynguin] - Pynguin is a command line tool written in Python that allows to automatically generate unit tests for Python programs.
- [GPT-3.5] - A set of models that improve on GPT-3 and can understand as well as generate natural language or code
- [Pytest] - Pytest is a Python testing framework that originated from the PyPy project. It can be used to write various types of software tests, including unit tests, integration tests, end-to-end tests, and functional tests. 


## Contents

This research addresses number of research questions:

- [RQ1] - What attributes of the test cases impacts the success of TDD using LLMs?
- [RQ2] - Could Input Space Partitioning lead to effective TDD?
- [RQ3] - How do the datatypes involved in a problem affect TDD using LLMs
- [RQ4] - How is the datatype of inputs compared to the return type matter in TDD using ChatGPT?
- [RQ5] - Explore Ambiguity of string vs integer input tests. Is there less ambiguity for strings compared to integers?
- [RQ6] - Are descriptive tests written in plain text more effective than providing test code in influencing ChatGPT’s performance and understanding of tests? Given that ChatGPT is an LLM based on natural language processing and prompts, do written instructions enhance performance and test understanding?
- [RQ7] - When we consolidate all the unit tests into one test code with multiple assert statements, does this approach mitigate the challenge of ChatGPT forgetting previous test cases when attempting to satisfy new ones?
- [RQ8] - When ChatGPT consistently provides the same failing code despite indications that modifications are necessary, is the source of these code snippets traceable to solution blogs or discussion groups such as Stack Overflow?
- [RQ9] - How does ChatGPT’s performance differ for LeetCode problems before and after its knowledge cutoff, and does it exhibit a capability to discern subtle hints indicative of a specific LeetCode problem within the provided prompt?

   [RQ1]: <https://github.com/SanyogitaPiya/Test-Driven-Development-with-LLM/tree/main/RQ1>
   [RQ2]: <https://github.com/SanyogitaPiya/Test-Driven-Development-with-LLM/tree/main/RQ2>
   [RQ3]: <https://github.com/SanyogitaPiya/Test-Driven-Development-with-LLM/tree/main/RQ3>
   [RQ4]: <https://github.com/SanyogitaPiya/Test-Driven-Development-with-LLM/tree/main/RQ4>
   [RQ5]: <https://github.com/SanyogitaPiya/Test-Driven-Development-with-LLM/tree/main/RQ5>
   [RQ6]: <https://github.com/SanyogitaPiya/Test-Driven-Development-with-LLM/tree/main/RQ6>
   [RQ7]: <https://github.com/SanyogitaPiya/Test-Driven-Development-with-LLM/tree/main/RQ7>
   [RQ8]: <https://github.com/SanyogitaPiya/Test-Driven-Development-with-LLM/tree/main/RQ8>
   [RQ9]: <https://github.com/SanyogitaPiya/Test-Driven-Development-with-LLM/tree/main/RQ9>
  
   [LeetCode]: <https://leetcode.com/>
   [Pynguin]: <https://www.pynguin.eu/>
   [GPT-3.5]:<https://platform.openai.com/docs/models>
   [Pytest]: <https://docs.pytest.org/en/7.4.x/>
