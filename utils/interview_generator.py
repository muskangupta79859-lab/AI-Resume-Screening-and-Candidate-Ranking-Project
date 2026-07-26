question_bank = {

    "python": [
        "Explain decorators in Python.",
        "What is the difference between list and tuple?",
        "What are generators?",
        "Explain OOP concepts in Python."
    ],

    "sql": [
        "Explain INNER JOIN and LEFT JOIN.",
        "What is normalization?",
        "Difference between DELETE, DROP and TRUNCATE?",
        "What are indexes?"
    ],

    "machine learning": [
        "What is overfitting?",
        "Explain cross-validation.",
        "Difference between classification and regression?",
        "What is feature engineering?"
    ],

    "tensorflow": [
        "What is a Tensor?",
        "Explain backpropagation.",
        "What is an optimizer?",
        "Difference between TensorFlow and PyTorch?"
    ],

    "pandas": [
        "Difference between loc and iloc?",
        "How do you handle missing values?",
        "Explain groupby()."
    ],

    "numpy": [
        "Difference between array and list?",
        "Explain broadcasting.",
        "What is vectorization?"
    ],

    "git": [
        "Difference between merge and rebase?",
        "Explain Git branching.",
        "What is a pull request?"
    ],

    "docker": [
        "What is Docker?",
        "Difference between Docker Image and Container?",
        "Why do we use Docker?"
    ]
}


def generate_questions(skills):

    questions = {}

    for skill in skills:

        key = skill.lower()

        if key in question_bank:
            questions[skill] = question_bank[key]

    return questions