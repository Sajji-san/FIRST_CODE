# === Stage 20: Добавь восстановление записей из архива ===
# Project: InterviewNotes
def restore_from_archive(archive_path, output_path):
    """Восстанавливает записи из текстового архива формата InterviewNotes."""
    records = []
    with open(archive_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split('|||')
            record = {
                'id': int(parts[0]),
                'candidate_name': parts[1],
                'questions': parts[2].split(';') if ';' in parts[2] else [parts[2]],
                'scores': [int(x) for x in parts[3].split(';')] if ';' in parts[3] else [int(parts[3])],
                'decision': parts[4],
                'date': parts[5] if len(parts) > 5 else 'unknown'
            }
            records.append(record)
    with open(output_path, 'w', encoding='utf-8') as f:
        for r in records:
            line = (f"{r['id']}|||{r['candidate_name']}|||" +
                    ';'.join(r['questions']) + '|||' +
                    ';'.join(str(s) for s in r['scores']) + '|||' +
                    r['decision'] + '|||' + r['date'])
            f.write(line + '\n')
    print(f"Восстановлено {len(records)} записей в файл: {output_path}")
