# Concept Explorer Engine — Semantic Mapper + Classifier
# Purpose: Discover structure & meaning from unstructured or unknown input

from typing import List, Dict, Any
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json

class ConceptExplorer:
    def __init__(self, num_clusters: int = 5):
        self.vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
        self.num_clusters = num_clusters
        self.kmeans = None
        self.keywords_map = {}

    def fit(self, raw_texts: List[str]) -> Dict[str, Any]:
        tfidf_matrix = self.vectorizer.fit_transform(raw_texts)
        self.kmeans = KMeans(n_clusters=self.num_clusters, random_state=42)
        labels = self.kmeans.fit_predict(tfidf_matrix)

        grouped: Dict[int, List[str]] = {}
        for idx, label in enumerate(labels):
            grouped.setdefault(label, []).append(raw_texts[idx])

        self.keywords_map = self.extract_keywords(grouped, tfidf_matrix)
        return {
            "labels": labels,
            "clusters": grouped,
            "keywords": self.keywords_map
        }

    def extract_keywords(self, groups: Dict[int, List[str]], matrix) -> Dict[int, List[str]]:
        feature_names = self.vectorizer.get_feature_names_out()
        centroids = self.kmeans.cluster_centers_
        keywords = {}
        for idx, center in enumerate(centroids):
            top_indices = center.argsort()[::-1][:5]
            keywords[idx] = [feature_names[i] for i in top_indices]
        return keywords

    def predict_cluster(self, new_input: str) -> Dict[str, Any]:
        tfidf_input = self.vectorizer.transform([new_input])
        label = self.kmeans.predict(tfidf_input)[0]
        return {
            "predicted_cluster": label,
            "related_keywords": self.keywords_map.get(label, [])
        }

    def get_similarity_matrix(self, raw_texts: List[str]) -> np.ndarray:
        tfidf_matrix = self.vectorizer.fit_transform(raw_texts)
        return cosine_similarity(tfidf_matrix)

# Example Usage:
if __name__ == "__main__":
    inputs = [
        "Football match prediction using xG and odds",
        "Cybersecurity breach detection in OSINT",
        "Shodan scan results and IP mapping",
        "Neural network betting system",
        "Intelligence gathering from public APIs",
        "Deep learning match outcome predictor",
        "Automated API data mapper and cleaner"
    ]

    explorer = ConceptExplorer(num_clusters=3)
    result = explorer.fit(inputs)
    print(json.dumps(result, indent=2))

    prediction = explorer.predict_cluster("Create football model using xG and API odds")
    print(json.dumps(prediction, indent=2))
