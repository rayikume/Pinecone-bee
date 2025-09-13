from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def token_overlap(prediction, ground_truth):
    vectorizer = CountVectorizer().fit_transform([prediction, ground_truth])
    vectors = vectorizer.toarray()
    return cosine_similarity(vectors)[0, 1]


class CustomEvaluator:
    def __init__(self, database):
        self.database = database

    def get_ground_truth(self, query, tk=1):
        docs = self.database.similarity_search(query, tk=tk)
        ground_truth = " ".join([page.page_content for page in docs])
        return ground_truth

    def evaluate(self, query, model_outputs):
        ground_truth = self.get_ground_truth(query)
        results = {}

        for model_name, response in model_outputs.items():
            score = token_overlap(response, ground_truth)
            results[model_name] = {
                "score": f"{score}",
                "response": f"{response}",
            }

        return results

