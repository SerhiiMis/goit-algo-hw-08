import heapq

def min_cost_to_connect_cables(cables):
    # Створюємо мін-купу з довжин кабелів
    heapq.heapify(cables)
    
    total_cost = 0

    # Поки в купі більше одного елемента
    while len(cables) > 1:
        # Виймаємо два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Витрати на з'єднання двох кабелів
        cost = first + second
        
        # Додаємо витрати до загальних витрат
        total_cost += cost
        
        # Поміщаємо новий кабель назад у купу
        heapq.heappush(cables, cost)
    
    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
print("Мінімальні витрати на з'єднання кабелів:", min_cost_to_connect_cables(cables))
