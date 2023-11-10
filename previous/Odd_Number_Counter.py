def countOdds(low: int, high: int) -> int:
    if low % 2 == 0:
        return (high - low + 1) // 2
    return (high - low) // 2 + 1


print(countOdds(2, 10))
print(countOdds(3, 11))