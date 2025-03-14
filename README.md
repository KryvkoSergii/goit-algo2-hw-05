# Big data algorithms

## Task 1. Checking the uniqueness of passwords using a Bloom filter

Create a function to check the uniqueness of passwords using a Bloom filter. This function should determine whether a password has been used before, without having to store the passwords themselves.

### Specifications

1. Implement a BloomFilter class that provides the ability to add elements to a filter and check whether an element is in the filter.

2. Implement a check_password_uniqueness function that uses an instance of BloomFilter and checks the list of new passwords for uniqueness. It should return the result of the check for each password.

3. Ensure that all data types are handled correctly. Passwords should be treated simply as strings, without hashing. Empty or invalid values ​​should also be considered and handled appropriately.

4. The function and class should work with large data sets, using minimal memory.

### Prerequisites 
```bash
poetry install
poetry shell
```

### Execure task
```bash
poetry run .\app\task1.py
```
### Result
```
Password 'password123' - Password already exists.
Password 'newpassword' - Password is unique.
Password 'admin123' - Password already exists.
Password 'guest' - Password is unique.
```

## Task 2. Compare the performance of HyperLogLog with the exact unique element count

Create a script to compare the exact unique element count and the count using HyperLogLog.

### Specifications

1. Load a dataset from a real log file [lms-stage-access.log](https://drive.google.com/file/d/13NUCSG7l_z2B7gYuQubYIpIjJTnwOAOb/view) containing information about IP addresses.

2. Implement a method for the exact unique IP address count using the set structure.

3. Implement a method for the approximate unique IP address count using HyperLogLog.

4. Compare the methods in terms of execution time.

### Prerequisites 
```bash
poetry install
poetry shell
```

### Execure task
```bash
poetry run .\app\task2.py
```
### Result
```bash
 Comparison Results                         
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃                       ┃     Exact Count     ┃    HyperLogLog     ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ Unique Elements       │         28          │ 28.825169450822077 │
│ Execution Time (sec.) │ 0.42615675926208496 │ 0.4436922073364258 │
└───────────────────────┴─────────────────────┴────────────────────┘
```