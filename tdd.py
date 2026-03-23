# 1. TEST (əvvəl yazılır)
def test_number():
    assert check_number(5) == "positive"
    assert check_number(-3) == "negative"
    assert check_number(0) == "zero"


# 2. FUNCTION (sonra yazılır)
def check_number(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"


# 3. TESTİ İŞLƏT
test_number()

print("All tests passed ✅")