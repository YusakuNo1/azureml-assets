The BERT model is a pre-trained model that has been trained on a large corpus of English language data. The model was trained using a masked language modeling (MLM) objective, meaning that the model is able to predict words that were randomly masked in an input sentence. The BERT model can also predict if two sentences were originally consecutive in a text or not. This model is intended to be used as a tool for fine-tuning in various downstream tasks such as sequence classification and question answering, but is not recommended for tasks such as text generation. To use this model, you can utilize a pipeline specifically designed for masked language modeling.

> The above summary was generated using ChatGPT. Review the [original model card](https://huggingface.co/bert-base-cased) to understand the data used to train the model, evaluation metrics, license, intended uses, limitations and bias before using the model.

### Inference samples

Inference type|Python sample (Notebook)|CLI with YAML
|--|--|--|
Real time|[fill-mask-online-endpoint.ipynb](https://aka.ms/azureml-infer-online-sdk-fill-mask)|[fill-mask-online-endpoint.sh](https://aka.ms/azureml-infer-online-cli-fill-mask)
Batch | coming soon


### Finetuning samples

Task|Use case|Dataset|Python sample (Notebook)|CLI with YAML
|---|--|--|--|--|
Text Classification|Emotion Detection|[Emotion](https://huggingface.co/datasets/dair-ai/emotion)|[emotion-detection.ipynb](https://aka.ms/azureml-ft-sdk-emotion-detection)|[emotion-detection.sh](https://aka.ms/azureml-ft-cli-emotion-detection)
Token Classification|Token Classification|[Conll2003](https://huggingface.co/datasets/conll2003)|[token-classification.ipynb](https://aka.ms/azureml-ft-sdk-token-classification)|[token-classification.sh](https://aka.ms/azureml-ft-cli-token-classification)
Question Answering|Extractive Q&A|[SQUAD (Wikipedia)](https://huggingface.co/datasets/squad)|[extractive-qa.ipynb](https://aka.ms/azureml-ft-sdk-extractive-qa)|[extractive-qa.sh](https://aka.ms/azureml-ft-cli-extractive-qa)


### Model Evaluation

|Task|Use case|Dataset|Python sample (Notebook)|
|---|--|--|--|
|Fill Mask|Fill Mask|[imdb](https://huggingface.co/datasets/imdb)|[evaluate-model-fill-mask.ipynb](https://aka.ms/azureml-eval-sdk-fill-mask/)|


### Sample inputs and outputs (for real-time inference)

#### Sample input
```json
{
    "inputs": {
        "input_string": ["Paris is the [MASK] of France.", "Today is a [MASK] day!"]
    },
    "parameters": {
        "top_k": 2
    }
}
```

#### Sample output
```json
[
    [
        {
            "score": 0.9861817359924316,
            "token": 2364,
            "token_str": "capital",
            "sequence": "Paris is the capital of France."
        },
        {
            "score": 0.0037214113399386406,
            "token": 2057,
            "token_str": "center",
            "sequence": "Paris is the center of France."
        }
    ],
    [
        {
            "score": 0.17196792364120483,
            "token": 2712,
            "token_str": "beautiful",
            "sequence": "Today is a beautiful day!"
        },
        {
            "score": 0.12262503802776337,
            "token": 1632,
            "token_str": "great",
            "sequence": "Today is a great day!"
        }
    ]
]
```