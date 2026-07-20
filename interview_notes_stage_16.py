# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: InterviewNotes
def monthly_stats(interviews, year=2024):
    stats = {}
    for iv in interviews:
        date = iv.get('scheduled', '').split('-')
        if len(date) != 3 or date[1] != str(year):
            continue
        month = int(date[2])
        key = f"{year}-{month:02d}"
        stats.setdefault(key, {'count': 0, 'avg_score': 0})
        stats[key]['count'] += 1
    total = sum(v['count'] for v in stats.values())
    if total == 0:
        return {}
    weighted_sum = 0.0
    for key, v in stats.items():
        weighted_sum += v['count'] * (v.get('avg_score', 0))
    avg_overall = weighted_sum / total
    result = []
    for key in sorted(stats.keys()):
        v = stats[key]
        result.append({
            'month': int(key.split('-')[1]),
            'year': int(key.split('-')[0]),
            'count': v['count'],
            'avg_score': round(v.get('avg_score', 0), 2),
            'overall_avg': avg_overall,
        })
    return result
