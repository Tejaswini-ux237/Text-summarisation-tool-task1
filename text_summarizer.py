# Text Summarization Tool - Task 1 for CODTECH Internship
# Author: UPPALA TEJASWINI

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer  # You can also try LexRankSummarizer or LuhnSummarizer

def summarize_text(text, sentence_count=3):
    """
    Summarizes the input text using LSA (Latent Semantic Analysis).
    
    Parameters:
    text (str): Input text to summarize.
    sentence_count (int): Number of sentences to include in summary.
    
    Returns:
    str: Summary of the input text.
    """
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentence_count)
    
    return ' '.join(str(sentence) for sentence in summary)


# Example usage
if __name__ == "__main__":
    input_text = """
    Natural Language Processing (NLP) is a subfield of artificial intelligence (AI) that focuses on the interaction 
    between computers and humans through natural language. The ultimate objective of NLP is to enable computers 
    to understand, interpret, and generate human languages in a valuable way. Most NLP techniques rely on machine 
    learning to derive meaning from human languages. NLP is used in various applications like chatbots, translation 
    services, sentiment analysis, and speech recognition.
    """

    print("Original Text:\n", input_text)
    print("\nSummary:\n", summarize_text(input_text, sentence_count=2))
