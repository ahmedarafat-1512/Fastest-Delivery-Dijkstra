import heapq
from collections import defaultdict

def dijkstra(graph, start, end):
    # لو المطعم أو العميل مش موجودين في الخريطة أصلاً
    if start not in graph or end not in graph:
        return float('inf'), []

    # المسافات في الأول كلها مالانهاية، المطعم بس 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # عشان نرجع نعيد بناء المسار في الآخر
    parent = {node: None for node in graph}

    # الـ priority queue عشان نجيب أقل مسافة كل مرة
    pq = [(0, start)]  # (المسافة الحالية, اسم العقدة)

    while pq:
        current_dist, current = heapq.heappop(pq)

        # لو لقينا مسار أقصر للنقطة دي قبل كده، متعبش نفسك
        if current_dist > distances[current]:
            continue

        # لو وصلنا للعميل خلاص ممكن نطلع بدري ونوفر وقت
        if current == end:
            break

        # نشوف جيران النقطة الحالية
        for neighbor, weight in graph[current]:
            new_dist = current_dist + weight

            # لو الطريق الجديد أقصر من اللي عندنا، نحدثه
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                parent[neighbor] = current
                heapq.heappush(pq, (new_dist, neighbor))

    # لو لسه المسافة للعميل مالانهاية يبقى مفيش طريق
    if distances[end] == float('inf'):
        return float('inf'), []

    # نرجع نبني المسار من العميل للمطعم وبعدين نعكسه
    path = []
    temp = end
    while temp is not None:
        path.append(temp)
        temp = parent[temp]
    path.reverse()

    return distances[end], path


# الخريطة بتاعة القاهرة (بالدقايق تقريبي حسب الزحمة الصبح)
graph = {
    "Restaurant": [("Nasr City", 8), ("Heliopolis", 6), ("Maadi", 15)],
    "Nasr City": [("Heliopolis", 5), ("New Cairo", 12), ("Downtown", 10)],
    "Heliopolis": [("Nasr City", 5), ("New Cairo", 15), ("Downtown", 8)],
    "Maadi": [("Downtown", 12), ("Giza", 20)],
    "New Cairo": [("Customer", 7), ("Heliopolis", 15)],
    "Downtown": [("Customer", 5), ("Maadi", 12), ("Giza", 10)],
    "Giza": [("Maadi", 20), ("Customer", 25)],
    "Customer": []
}

# اختبار على العميل اللي في التجمع تقريبًا
distance, path = dijkstra(graph, "Restaurant", "Customer")

if distance == float('inf'):
    print("معلش، مفيش طريق يوصل للعميل ده")
else:
    print(f"أقصر وقت للتوصيل: {distance} دقيقة")
    print(f"المسار الأمثل: {' → '.join(path)}")
