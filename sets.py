# Küme oluşturma
fruits = {"apple", "banana", "cherry"}

# Eleman ekleme
fruits.add("orange")

# Eleman çıkarma
fruits.remove("banana")

# Eleman sayısı
print(len(fruits))  # Çıktı: 3

# Kümeler arası işlemler
veggies = {"carrot", "broccoli", "spinach"}

# Birleşim
all_items = fruits.union(veggies)

# Kesişim
common_items = fruits.intersection(veggies)

# Fark
unique_fruits = fruits.difference(veggies)

print(all_items)  # Çıktı: {'carrot', 'cherry', 'broccoli', 'spinach', 'orange', 'apple'}
print(common_items)  # Çıktı: set()
print(unique_fruits)  # Çıktı: {'cherry', 'apple', 'orange'}
