def hitungFactorial(n: int) -> int:
    """Sebuah fungsi untuk menghitung factorial"""
    if n == 1:
        print(n,'=',end=' ')
        return 1
    
    else:
        print(n,'x',end=' ')
        return n * hitungFactorial(n - 1)