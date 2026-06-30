from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v1')


def rank_candidates(job_text, candidates):

    job_emb = model.encode(job_text, convert_to_tensor=True)

    results = []

    for c in candidates:

        skills = " ".join([s.get("name", "") for s in c.get("skills", [])])
        career = " ".join([j.get("title", "") for j in c.get("career_history", [])])

        text = skills + " " + career

        cand_emb = model.encode(text, convert_to_tensor=True)

        score = util.cos_sim(job_emb, cand_emb).item() * 100

        results.append({
            "candidate_id": c.get("candidate_id"),
            "score": round(score, 2),
            "reason": "Matched skills + experience + semantic similarity"
        })

    return sorted(results, key=lambda x: x["score"], reverse=True)