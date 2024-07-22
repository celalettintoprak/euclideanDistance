# 📚 Python Uygulama 2 - Öklid

## Noktaların Tanımlanması:
points = [(1, 5), (4, 12), (3, 7), (0, 4)]

## Öklid Mesafesi İçin Bir Fonksiyon Yazma:
def euclideanDistance(p1, p2):
    ### Virgülden sonra 3 basamak kalacak şekilde yuvarlama işlemi de eklendi.
    return round(((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5, 3)

## Mesafelerin Hesaplanması:
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

## Minimum Mesafenin Bulunması:
min_distance = min(distances)

## Sonuçları Konsola Yazdırma:
print("Noktalar arası mesafeler:", distances)
print("En kısa mesafe:", min_distance)