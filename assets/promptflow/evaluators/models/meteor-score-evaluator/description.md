| | |
| -- | -- |
| Score range | Float [0-1] |
| What is this metric? | Evaluates the quality of the generated text by considering precision, recall, and a range of linguistic features like synonyms, stemming, and word order. |
| How does it work? | The METEOR score is calculated based on the harmonic mean of unigram precision and recall, with higher weight given to recall. It also incorporates additional features such as stemming (matching word roots), synonym matching, and a penalty for incorrect word order. The final score ranges from 0 to 1, where 1 indicates a perfect match. |
| When to use it? | Use the METEOR score when you want a more linguistically informed evaluation metric that captures not only n-gram overlap but also accounts for synonyms, stemming, and word order. This is particularly useful for evaluating tasks like machine translation, text summarization, and text generation. |
| What does it need as input? | Ground Truth Response, Generated Response |