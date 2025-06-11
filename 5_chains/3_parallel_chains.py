# we get a document, and we will generate notes and quiz both at the same time then show it to user using parallel chains
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()


model = ChatGroq(
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

model2 = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-8b",
    temperature=0,
    max_tokens=None,
    max_retries=2,
)


prompt1 = PromptTemplate(
    template="Generate short and simple note from the following text: \n {text}",
    input_variables=["text"]
)


prompt2 = PromptTemplate(
    template="Generate 5 short Question answers from the following text: \n {text}",
    input_variables=["text"]
)


prompt3 = PromptTemplate(
    template="Merge the provided notes and quiz into a single document: \n notes -> {notes} \n quiz -> {quiz}",
    input_variables=["notes", "quiz"]
)

parser = StrOutputParser()

# This will help run parallel tasks, in this case we will generate notes and quiz at the same time using parallel chains
parallel_chain = RunnableParallel(
    {
        'notes': prompt1 | model | parser,
        'quiz': prompt2 | model2 | parser
    }
)

merge_chain = prompt3 | model | parser

chain = parallel_chain | merge_chain

text = """
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.
"""

# result = chain.invoke({"text": text})
# print(result)

chain.get_graph().print_ascii()  # Uncomment to print the graph in a more detailed format


