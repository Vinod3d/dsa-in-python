# 01: Flowchart and Pseudocode – Complete Notes

---

## 1. Introduction

Before writing a program in **Python** or any other language, a programmer first plans the logic of the problem.

Two important tools used for planning are:

* **Flowchart**
* **Pseudocode**

These tools help in:

* Understanding problem logic clearly
* Avoiding mistakes before coding
* Improving problem-solving skills
* Writing clean and structured programs



## 2. What is a Flowchart?

A flowchart is a graphical representation of a process, system or algorithm. It uses symbols and arrows to show the sequence of steps needed to complete a task. Flow charts are useful in visualising how to solve a problem and make the process
easier to follow


#### 📌 Common Flowchart Symbols

| Symbol Shape  | Name           | Purpose                         |
| ------------- | -------------- | ------------------------------- |
| Oval          | Start / End    | Beginning or end of program     |
| Rectangle     | Process        | Calculation or instruction      |
| Parallelogram | Input / Output | Taking input or printing output |
| Diamond       | Decision       | Condition checking (True/False) |
| Arrow         | Flow Line      | Direction of execution          |



#### 📌Example 1 – Add Two Numbers



Take two numbers as input and print their sum.

### Flowchart Steps:

1. Start
2. Input A, B
3. Sum = A + B
4. Print Sum
5. End

Flowchart Logic Representation:

Start → Input → Process → Output → End


## 📌 Example 2 – Check Even or Odd

Check whether a number is even or odd.

### Logic:

1. Start
2. Input N
3. If N % 2 == 0

   * Print "Even"
     Else
   * Print "Odd"
4. End

This example shows **Decision (Diamond)** usage.


#### 📌 Advantages of Flowchart

* Easy to understand
* Good for beginners
* Visual clarity
* Helps in debugging
* Good for explaining logic in interviews

#### 📌 Disadvantages of Flowchart

* Takes time to draw
* Difficult for very large programs
* Modifying becomes complex

## 3. What is Pseudocode?

A Pseudocode is a simple way of describing an algorithm in plain language or a mix of code like and natural language instructions.
It doesn’t follow any specific programming language syntax, making it easier to understand, even for those without programming knowledge Pseudo code is often used as a step before writing actual code.

#### 📌 Structure of Pseudocode

Basic keywords commonly used:

* START
* END
* INPUT
* OUTPUT
* IF / ELSE
* WHILE
* FOR

#### 📌 Example 1 – Add Two Numbers (Pseudocode)

```
START
INPUT A, B
SET Sum = A + B
OUTPUT Sum
END
```

#### 📌 Example 2 – Even or Odd (Pseudocode)

```
START
INPUT N
IF N % 2 == 0 THEN
    OUTPUT "Even"
ELSE
    OUTPUT "Odd"
END IF
END
```

#### 📌 Example 3 – Find Largest of Two Numbers

```
START
INPUT A, B
IF A > B THEN
    OUTPUT "A is greater"
ELSE
    OUTPUT "B is greater"
END IF
END
```

---

## 📌 Example 4 – Print Numbers from 1 to 5

```
START
SET i = 1
WHILE i <= 5
    OUTPUT i
    SET i = i + 1
END WHILE
END
```


## Flowchart vs Pseudocode

| Feature        | Flowchart | Pseudocode  |
| -------------- | --------- | ----------- |
| Type           | Graphical | Text-based  |
| Easy to Modify | No        | Yes         |
| Best For       | Beginners | Programmers |
| Large Programs | Difficult | Easy        |
| Visual Clarity | High      | Medium      |

---

# 🔷 Important Concepts for DSA

Flowchart and Pseudocode help in:

* Understanding patterns in problems
* Writing algorithms clearly
* Preparing for coding interviews
* Improving logical thinking

In **DSA**, always follow:

1. Understand Problem
2. Write Pseudocode
3. Dry Run
4. Convert to Python Code
5. Analyze Time & Space Complexity

---

## 🔷 How to Convert Pseudocode to Python

Example:

### Pseudocode

```
INPUT N
IF N % 2 == 0
    PRINT "Even"
ELSE
    PRINT "Odd"
```

### Python Code

```python
n = int(input())
if n % 2 == 0:
    print("Even")
else:
    print("Odd")
```

