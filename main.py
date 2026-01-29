import re

# لیست Stop Words انگلیسی
STOP_WORDS = {
    "a",
    "an",
    "the",
    "and",
    "or",
    "not",
    "is",
    "are",
    "was",
    "were",
    "be",
    "been",
    "being",
    "have",
    "has",
    "had",
    "do",
    "does",
    "did",
    "will",
    "would",
    "could",
    "should",
    "may",
    "might",
    "must",
    "shall",
    "can",
    "need",
    "dare",
    "ought",
    "used",
    "to",
    "of",
    "in",
    "for",
    "on",
    "with",
    "at",
    "by",
    "from",
    "up",
    "about",
    "into",
    "over",
    "after",
    "beneath",
    "under",
    "above",
    "it",
    "its",
    "this",
    "that",
    "these",
    "those",
    "i",
    "you",
    "he",
    "she",
    "we",
    "they",
    "what",
    "which",
    "who",
    "whom",
    "where",
    "when",
    "why",
    "how",
    "all",
    "each",
    "every",
    "both",
    "few",
    "more",
    "most",
    "other",
    "some",
    "such",
    "no",
    "nor",
    "only",
    "own",
    "same",
    "so",
    "than",
    "too",
    "very",
    "just",
    "but",
    "if",
    "then",
    "because",
    "as",
    "until",
    "while",
    "although",
    "though",
    "once",
    "before",
    "after",
    "during",
    "since",
    "without",
    "between",
    "through",
    "against",
    "any",
    "also",
}


def load_documents_from_file(file_path):
    """
    خواندن اسناد از فایل متنی
    هر خط به عنوان یک سند جداگانه در نظر گرفته می‌شود
    """
    docs = {}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for doc_id, line in enumerate(f, start=1):
                line = line.strip()
                if line:  # خطوط خالی نادیده گرفته می‌شوند
                    docs[doc_id] = line
        print(f"تعداد {len(docs)} سند با موفقیت بارگذاری شد.")
    except FileNotFoundError:
        print(f"خطا: فایل '{file_path}' یافت نشد.")
    except Exception as e:
        print(f"خطا در خواندن فایل: {e}")
    return docs


def preprocess(text):
    """
    پیش‌پردازش متن: تبدیل به حروف کوچک، حذف کاراکترهای غیرحروفی و حذف stop words
    """
    text = text.lower()
    words = re.findall(r"\b\w+\b", text)
    # حذف stop words
    words = [word for word in words if word not in STOP_WORDS]
    return words


def build_inverted_index(docs):
    """
    ساخت ایندکس معکوس از مجموعه اسناد
    """
    inverted_index = {}
    for doc_id, text in docs.items():
        words = preprocess(text)
        for word in set(words):  # استفاده از set برای جلوگیری از تکرار
            if word not in inverted_index:
                inverted_index[word] = set()
            inverted_index[word].add(doc_id)
    return inverted_index


def boolean_and(set1, set2):
    """عملگر AND بولی"""
    return set1 & set2


def boolean_or(set1, set2):
    """عملگر OR بولی"""
    return set1 | set2


def boolean_not(set1, all_docs):
    """عملگر NOT بولی"""
    return all_docs - set1


def search(query, inverted_index, all_docs):
    """
    تابع پردازش عبارت بولی
    قالب‌های پشتیبانی شده:
    - term1 AND term2
    - term1 OR term2
    - NOT term
    - term (جستجوی ساده)
    """
    query_lower = query.lower()
    tokens = query_lower.split()

    if len(tokens) == 0:
        return set()

    # جستجو با AND
    if " and " in query_lower:
        idx = tokens.index("and")
        term1 = tokens[idx - 1] if idx > 0 else ""
        term2 = tokens[idx + 1] if idx + 1 < len(tokens) else ""
        return boolean_and(
            inverted_index.get(term1, set()), inverted_index.get(term2, set())
        )

    # جستجو با OR
    elif " or " in query_lower:
        idx = tokens.index("or")
        term1 = tokens[idx - 1] if idx > 0 else ""
        term2 = tokens[idx + 1] if idx + 1 < len(tokens) else ""
        return boolean_or(
            inverted_index.get(term1, set()), inverted_index.get(term2, set())
        )

    # جستجو با NOT
    elif tokens[0] == "not" and len(tokens) > 1:
        term = tokens[1]
        return boolean_not(inverted_index.get(term, set()), all_docs)

    # جستجوی ساده یک ترم
    else:
        term = tokens[0]
        return inverted_index.get(term, set())


def display_results(results, docs):
    """نمایش نتایج جستجو"""
    if results:
        print(f"\n✓ تعداد {len(results)} سند یافت شد:")
        print("-" * 50)
        for doc_id in sorted(results):
            print(f"  [سند {doc_id}]: {docs[doc_id]}")
    else:
        print("\n✗ هیچ سندی یافت نشد.")


def display_inverted_index(inverted_index):
    """نمایش ایندکس معکوس"""
    print("\n" + "=" * 50)
    print("ایندکس معکوس:")
    print("=" * 50)
    for term in sorted(inverted_index.keys()):
        doc_ids = sorted(inverted_index[term])
        print(f"  '{term}': {doc_ids}")


def main():
    # مسیر فایل اسناد
    file_path = "documents.txt"

    # بارگذاری اسناد از فایل
    docs = load_documents_from_file(file_path)

    if not docs:
        print("خطا: هیچ سندی بارگذاری نشد.")
        return

    # نمایش اسناد بارگذاری شده
    print("\n" + "=" * 50)
    print("اسناد بارگذاری شده:")
    print("=" * 50)
    for doc_id, text in docs.items():
        print(f"  [سند {doc_id}]: {text}")

    # ساخت ایندکس معکوس
    inverted_index = build_inverted_index(docs)

    # نمایش ایندکس معکوس
    display_inverted_index(inverted_index)

    # مجموعه همه اسناد
    all_docs = set(docs.keys())

    # نمونه جستجوها
    print("\n" + "=" * 50)
    print("نمونه جستجوها:")
    print("=" * 50)

    queries = [
        "information AND retrieval",
        "python OR boolean",
        "NOT search",
        "search",
        "indexing",
        "machine AND learning",
    ]

    for query in queries:
        print(f"\n🔍 جستجو: '{query}'")
        results = search(query, inverted_index, all_docs)
        display_results(results, docs)

    # حالت تعاملی
    print("\n" + "=" * 50)
    print("حالت تعاملی (برای خروج 'exit' وارد کنید):")
    print("=" * 50)

    while True:
        query = input("\n🔍 عبارت جستجو را وارد کنید: ").strip()
        if query.lower() == "exit":
            print("خداحافظ!")
            break
        if query:
            results = search(query, inverted_index, all_docs)
            display_results(results, docs)


if __name__ == "__main__":
    main()
