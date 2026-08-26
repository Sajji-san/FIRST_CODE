# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: InterviewNotes
import statistics

def compute_metrics(interviews):
    if not interviews:
        return {}
    counts = {}
    for i in interviews:
        counts[i['candidate']] = counts.get(i['candidate'], 0) + 1
    return {
        'total': len(interviews),
        'candidates': len(counts),
        'avg_interviews_per_candidate': statistics.mean(counts.values()),
        'avg_score': statistics.mean([i['score'] for i in interviews if 'score' in i]),
        'rejected': sum(1 for i in interviews if i.get('result') == 'rejected'),
        'accepted': sum(1 for i in interviews if i.get('result') == 'accepted'),
        'pending': sum(1 for i in interviews if i.get('result') == 'pending'),
    }
