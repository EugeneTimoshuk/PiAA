def compute_lps_array(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(pattern, text):
    if not pattern or not text or len(pattern) > len(text):
        return []

    lps = compute_lps_array(pattern)
    print("Массив lps для шаблона:", lps)

    lps = compute_lps_array(pattern)
    i = 0
    j = 0
    occurrences = []
    len_p = len(pattern)
    len_t = len(text)

    print("\n=== Поиск шаблона в тексте ===")
    print(f"Текст:    {text}")
    print(f"Шаблон:   {pattern}")

    while i < len_t:
        print(f"\nСравнение: T[{i}]='{text[i]}' vs P[{j}]='{pattern[j]}'")

        if pattern[j] == text[i]:
            print("  → Совпадение! Двигаем оба указателя (i++, j++)")
            i += 1
            j += 1

            if j == len_p:
                print(f"\n=== Найдено полное вхождение на позиции {i - j}! ===")
                occurrences.append(i - j)
                print(f"  → Сдвигаем j = lps[{j - 1}] = {lps[j - 1]}")
                j = lps[j - 1]
        else:
            if j != 0:
                print(f"  → Несовпадение! Сдвигаем j = lps[{j - 1}] = {lps[j - 1]}")
                j = lps[j - 1]
            else:
                print("  → Несовпадение! j = 0 → двигаем только i")
                i += 1

        print(f"Текущее состояние: i = {i}, j = {j}, Найденные вхождения: {occurrences}")

    return occurrences

P = input("Введите шаблон P: ").strip()
T = input("Введите текст T: ").strip()

result = kmp_search(P, T)

if not result:
    print("Результат: -1")
else:
    print("Результат:", ",".join(map(str, result)))