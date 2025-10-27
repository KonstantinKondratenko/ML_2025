from collections import defaultdict, Counter

def apriori(transactions, min_support):
    def get_support(itemset, transactions):
        count = 0
        for transaction in transactions.values():
            if all(item in transaction for item in itemset):
                count += 1
        return count
    
    total_transactions = len(transactions)
    min_support_count = min_support * total_transactions
    
    print(f"Минимальная поддержка: {min_support} ({min_support_count}/{total_transactions})")
    
    all_items = set()
    for transaction in transactions.values():
        all_items.update(transaction)
    
    frequent_1 = []
    for item in all_items:
        support = get_support([item], transactions)
        if support >= min_support_count:
            frequent_1.append(([item], support))
    
    frequent_itemsets = {1: frequent_1}
    
    print("Частые 1-наборы:")
    for itemset, support in frequent_itemsets[1]:
        print(f"  {itemset}: поддержка = {support}/{len(transactions)}")
    print()
    
    k = 2
    while True:
        prev_frequent = [itemset for itemset, _ in frequent_itemsets[k-1]]
        candidates = set()
        
        for i in range(len(prev_frequent)):
            for j in range(i + 1, len(prev_frequent)):
                new_candidate = tuple(sorted(set(prev_frequent[i]) | set(prev_frequent[j])))
                if len(new_candidate) == k:
                    candidates.add(new_candidate)
        
        frequent_k = []
        for candidate in candidates:
            support = get_support(candidate, transactions)
            if support >= min_support_count:
                frequent_k.append((list(candidate), support))
        
        if not frequent_k:
            break
            
        frequent_itemsets[k] = frequent_k
        
        print(f"Частые {k}-наборы:")
        for itemset, support in frequent_itemsets[k]:
            print(f"  {itemset}: поддержка = {support}/{len(transactions)}")
        print()
        
        k += 1



def fpgrowth_demo(transactions, min_support):
    total_transactions = len(transactions)
    min_support_count = min_support * total_transactions
    
    print(f"Минимальная поддержка: {min_support} ({min_support_count}/{total_transactions})")
    print()
    
    item_frequencies = Counter()
    for transaction in transactions.values():
        item_frequencies.update(transaction)
    
    print("Частоты отдельных элементов:")
    for item, freq in sorted(item_frequencies.items()):
        print(f"  {item}: {freq}/{total_transactions}")
    print()
    
    frequent_items = {item: freq for item, freq in item_frequencies.items() 
                     if freq >= min_support_count}
    
    print("Частые элементы (>= минимальной поддержки):")
    for item, freq in sorted(frequent_items.items(), key=lambda x: (-x[1], x[0])):
        print(f"  {item}: {freq}/{total_transactions}")
    print()
    
    sorted_transactions = []
    for tid, transaction in transactions.items():
        filtered_sorted = sorted([item for item in transaction if item in frequent_items],
                               key=lambda x: (-frequent_items[x], x))
        if filtered_sorted:
            sorted_transactions.append((tid, filtered_sorted))
    
    print("Отсортированные транзакции (только частые элементы):")
    for tid, transaction in sorted_transactions:
        print(f"  {tid}: {transaction}")
    print()
    
    print("Построение FP-дерева (в упрощенном виде):")
    fp_tree = defaultdict(list)
    for tid, transaction in sorted_transactions:
        current_path = []
        for item in transaction:
            current_path.append(item)
            path_key = tuple(current_path)
            fp_tree[path_key].append(tid)
    
    for path, tids in sorted(fp_tree.items(), key=lambda x: (-len(x[1]), x[0])):
        if len(path) >= 2 and len(tids) >= min_support_count:
            print(f"  Путь {path}: транзакции {tids} (поддержка: {len(tids)})")
    

def task_1():
    import time
    transactions = {
        't1': ['A', 'B', 'C', 'D'],
        't2': ['A', 'C', 'D', 'F'],
        't3': ['A', 'C', 'D', 'E', 'G'],
        't4': ['A', 'B', 'D', 'F'],
        't5': ['B', 'C', 'G'],
        't6': ['D', 'F', 'G'],
        't7': ['A', 'B', 'G'],
        't8': ['C', 'D', 'F', 'G']
    }
    print("-" * 50)
    start = time.time()
    apriori(transactions, 3/8)
    end = time.time()
    print(f'Время выполнения == {end-start}\n')
    print('-' * 40)
    start = time.time()
    fpgrowth_demo(transactions, 2/8)
    end = time.time()
    print(f'Время выполнения == {end-start}\n')


if __name__ == "__main__":
    print("TASK1:")
    task_1()
