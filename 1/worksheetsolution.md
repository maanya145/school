answers to the worksheet:

## PYTHON – REVISION TOUR

1. "Welcome" is **a string** literal.

2. $ symbol can be used in naming an identifier (**False**).

3. Write any 2 data types available in Python: **int, str**.

4. "Division by zero" is an example of **a runtime** error.

5. `range(1,10)` will return values in the range of **1 to 9**.

6. `randint(1,10)` will return values in the range of **1 to 10**.

7. 
   - `"Computer Science"[0:6]` = **"Comput"**  
   - `"Computer Science"[3:10]` = **"puter S"**  
   - `"Computer Science"[::-1]` = **"ecneicS retupmoC"**  
   - `"Computer Science"[-8:]` = **"er Science"**  

8. Output of `print("Ok"*4 + "Done")`: **"OkOkOkOkDone"**.

9. Output of `print(print("Why?"))`:  
   - First, `"Why?"` will be printed.  
   - Then, `print()` returns `None`, so output is:  
     ```
     Why?
     None
     ```

10. Correct Expression: **C = A // B**.

11. Output of:
    ```python
    C = -11 % 4
    print(C)
    ```
    **1**

12. Two advantages of Python:
    - **Easy to learn and read**.
    - **Large standard library**.

    Two disadvantages of Python:
    - **Slower execution compared to compiled languages**.
    - **Not ideal for mobile development**.

13. Valid and invalid identifiers:
    - Valid: **_bonus, Emp1**
    - Invalid: **Emp-Code, While, SrNo., for, #count, 123Go, Bond007@**

14. Type of literals:
    - (i) `123` → **Integer**
    - (ii) `"Hello"` → **String**
    - (iii) `"Bye\nSee You"` → **String**
    - (iv) `'A'` → **String**
    - (v) `345.55` → **Float**
    - (vi) `10+4j` → **Complex**
    - (vii) `0x12` → **Hexadecimal Integer**

15. Size of each string:
    - (i) `"Python"` → **6**
    - (ii) `"Learning@\nCS"` → **12**
    - (iii) `"\table"` → **6**

16. Output of:
    - `True + True` = **2**
    - `100 + False` = **100**
    - `-1 + True` = **0**
    - `bool(-1 + True)` = **False**

17. Output of:
    - `2 * 7` = **14**
    - `2 ** 7` = **128**
    - `2**2**3` = **256**
    - `17 % 20` = **17**
    - `not(20>6) or (19>7) and (20==20)` = **True**

18. Output:
    ```python
    a, b, c = 20, 40, 60
    b += 10
    c += b
    print(a, b, c)
    ```
    **20 50 110**

19. **Python program to find sum and product of two numbers:**
    ```python
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum:", a + b)
    print("Product:", a * b)
    ```

20. **Python program to convert Fahrenheit to Celsius:**
    ```python
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5/9
    print("Temperature in Celsius:", c)
    ```

21. **Denomination breakdown program:**
    ```python
    money = int(input("Enter amount: "))
    denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    for denom in denominations:
        count = money // denom
        money %= denom
        print(f"{denom} = {count}")
    ```

22. **List operations:**
    ```python
    MyFamily = ["Father", "Mother", "Brother", "Sister", "Jacky"]
    print(MyFamily[2])  # "Brother"
    print(MyFamily[::-1])  # Reverse order
    print("Sister" in MyFamily)  # Check existence
    MyFamily[4] = "Tiger"  # Update Jacky to Tiger
    print(MyFamily.pop(4))  # Remove and print Jacky
    MyFamily.append("Tommy")  # Add Tommy
    ```

23. Correct Expression: **Record = Record + (50,)**.

24. **Difference between List and Tuple:**
    - List: **Mutable, defined with `[]`**.
    - Tuple: **Immutable, defined with `()`**.

25. **Difference between List and String:**
    - List: **Collection of elements, mutable**.
    - String: **Immutable sequence of characters**.

26. **Ordered vs Unordered collection:**
    - Ordered collection: **Maintains the sequence of elements**
                          **Example: List, Tuple**.
    - Unordered collection: **Does not guarantee element order**
                            **Example:  Set, Dictionary**.

27. **Dictionary operations:**
    ```python
    Employee = {'Empno': 1, 'Name': 'Snehil', 'Salary': 80000}
    print(Employee["Name"])  # Employee name
    Employee["Salary"] = 90000  # Update salary
    print(Employee.values())  # Get all values
    ```

28. Output of:
    ```python
    Num = 100
    Isok = False
    print(type(Num))  # <class 'int'>
    print(type(Isok))  # <class 'bool'>
    ```
    - **`<class 'int'>`**
    - **`<class 'bool'>`**

29. Required libraries:
    - `floor()` → **math**
    - `randrange()` → **random**
    - `randint()` → **random**
    - `sin()` → **math**

30. **Corrected code:**
    ```python
    To = 30
    for K in range(0, To):
        if K % 4 == 0:
            print(K * 4)
        else:
            print(K + 3)
    ```

31. **Corrected code:**
    ```python
    a = 5
    work = True
    b = "hello"
    c = a + len(b)  # Corrected
    for i in range(10):
        if i % 7 == 0:
            continue
    ```

32. **Corrected code:**
    ```python
    for Name in ["Ramesh", "Suraj", "Priya"]:
        if Name[0] == 'S':
            print(Name)
    ```

33. **Corrected code:**
    ```python
    a = b = 10
    c = a + b
    while c <= 20:
        print(c, end="*")
        c += 10
    ```

34. Possible outputs:
    - (i) **`2 1 3`**
    - (iv) **`5 3 5`**

35. **Type conversion in Python:**
    Type conversion in Python refers to converting one data type into another. It can be done in two ways:  

   ### **1. Implicit Type Conversion (Automatic Conversion)**  
   Python automatically converts a smaller data type into a larger one to prevent data loss.

   #### **Example:**  
   ```python
   a = 5      # Integer
   b = 2.5    # Float
   c = a + b  # Integer + Float → Float
   print(c)   # Output: 7.5
   print(type(c))  # Output: <class 'float'>
   ```

   ### **2. Explicit Type Conversion (Type Casting)**
   The programmer manually converts one data type into another using functions like int(), float(), str(), etc.

   #### **Example:**  
   ```python
   x = "10"   # String
   y = int(x) # Convert string to integer
   print(y, type(y))  # Output: 10 <class 'int'>
   
   a = 5
   b = float(a)  # Convert integer to float
   print(b, type(b))  # Output: 5.0 <class 'float'>
   
   num = 100
   text = str(num)  # Convert integer to string
   print(text, type(text))  # Output: '100' <class 'str'>
   ```


36. Infinite loop: **`while True:`**.

37. **Check divisibility by 7:**
    ```python
    num = int(input("Enter number: "))
    print("Divisible by 7" if num % 7 == 0 else "Not divisible")
    ```

38. 
    - `for i in range(10, 101, 10):`
    - `for i in range(10, 0, -1):`
39. **Output when `n = 10` and `n = 11`**  
    ```python
    i = 2
    while i < n:
        if i % 5 == 0:
            break
        print(i)
        i += 1
    else:
        print("done")
    ```
    - When `n = 10`: Output → **2 3 4 "done"**
    - When `n = 11`: Output → **2 3 4 "done"**

40. **Difference in outputs:**
    ```python
    # (i)
    for i in range(1, 10):
        if i % 4 == 0:
            break
        print(i)
    ```
    Output: **1 2 3** (Loop stops at `i = 4`)

    ```python
    # (ii)
    for i in range(1, 10):
        if i % 4 == 0:
            continue
        print(i)
    ```
    Output: **1 2 3 5 6 7 9** (Skips 4 and 8)

41. **Possible outputs for given random selection:**
    - (ii) **30#40#50#**  
    - (iii) **50#60#70#**

    Maximum values:  
    - `FROM = 3`
    - `TO = 4`

42. **Possible outputs and max values of `BEGIN` and `END`:**  
    - (i) Correct Output:  
      ```
      BLUE
      PINK
      GREEN
      RED
      ```
    - Maximum values:  
      - `PICKER = 3`

43. **Correct ways to generate numbers from 0 to 20:**
    - (ii) **range(0,21)**
    - (iii) **range(21)**

44. **Correct dictionary declaration:**
    - **(i) `Day={1:'monday',2:'tuesday',3:'wednesday'}`**

45. **Correct declaration:**
    - **(ii) Dictionary**

46. **Valid dictionary declaration:**
    - **(iii) `d3={1:'January',2:'February',3:'March'}`**

47. **Incorrect statements about dictionaries:**
    - **(ii) Dictionary items can be accessed by their index position**
    - **(iv) Dictionary keys must be of String data type** (False, they can be numbers too)

48. **Output of the given loop:**
    ```python
    x="abAbcAba"
    for w in x:
        if w=="a":
            print("*")
        else:
            print(w)
    ```
    Output:
    ```
    *
    b
    A
    b
    c
    A
    b
    *
    ```

49. **Convert `for` loop to `while` loop:**
    ```python
    k = 10
    while k < 20:
        print(k)
        k += 5
    ```

50. **Output of given code:**
    ```python
    colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
    del colors[4]  # removes "yellow"
    colors.remove("blue")  # removes "blue"
    p = colors.pop(3)  # removes "orange"
    print(p, colors)
    ```
    Output: **"orange ['violet', 'indigo', 'green', 'red']"**

51. **Output of given `while` loop:**
    ```python
    A = 10
    B = 15
    S = 0
    while A <= B:
        S = A + B
        A = A + 10
        B = B + 10
        if A >= 40:
            A = A + 100
    print(S)
    ```
    Output: **25**

52. **Output of given conditional block:**
    ```python
    X = 17
    if X >= 17:
        X += 10
    else:
        X -= 10
    print(X)
    ```
    Output: **27**

53. **How many times loop executes?**
    ```python
    P = 5
    Q = 35
    while P <= Q:
        P += 6
    ```
    Execution steps:
    ```
    5, 11, 17, 23, 29, 35 (6 times)
    ```
    Output: **6 times**

54. **Find the output of the given code:**
    ```python
    Msg = "CompuTer"
    Msg1 = ""
    for i in range(0, len(Msg)):
        if Msg[i].isupper():
            Msg1 = Msg1 + Msg[i].lower()
        elif i % 2 == 0:
            Msg1 = Msg1 + "*"
        else:
            Msg1 = Msg1 + Msg[i].upper()
    print(Msg1)
    ```
    Output: **"\*o*M\*t\*r"**

55. **Output of identity comparison:**
    ```python
    A = 10
    B = 10
    print(A == B)  # True
    print(id(A) == id(B))  # True (Python caches small integers)
    print(A is B)  # True
    ```
    - **True**
    - **True**
    - **True**
      
