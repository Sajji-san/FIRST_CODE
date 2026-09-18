# === Stage 43: Добавь пагинацию длинных списков ===
# Project: InterviewNotes
def paginate(items, page_size=10):
    """Return paginated view: (current_page, total_pages, all_pages)."""
    total_pages = max(1, (len(items) + page_size - 1) // page_size)
    pages = []
    for i in range(total_pages):
        start = i * page_size
        end = start + page_size
        pages.append(items[start:end])
    return pages
