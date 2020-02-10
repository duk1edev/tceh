s = [i for i in range(1,  12) if i % 2 == 0]
print(s)

lst = [w for w in range(1, 12) if w < 10]
print(lst)

words = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

stuff = [[w.upper(), w.lower(), len(w)] for w in words]
print(stuff)

l = [j for v in range(2, 5) for i in range(2, v) for j in range(i * 2, 10, i)]
print(l)

country  = ["India", "Pakistan", "Nepal", "Bhutan", "China", "Bangladesh"]
capital = ["New Delhi", "Islamabad", "Kathmandu", "Thimphu", "Beijing", "Dhaka"]

print({country[i]: capital[i] for i in range(len(country)) })