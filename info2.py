main_dict = {
    "IO":{
        "type_name": "Input/Output",
        "type_description": "Responsible for all input and output operations",
        "type_similiars": ["Output", "Input", "File", "File Operations"],
        "opening a file":{
            "type_name": "Opening a file",
            "type_description": "Responsible for opening a file",
            "type_similiars": ["Opening a file", "Loadin File", "Open File"],
            "opening a file in byte read":{
                "func_similiars": ["Opening a file", "Load File in Bytes", "File", "File Operations"],
                "func_name": "Opening a file in byte read",
                "func_description": "Opens a file in byte read mode",
            },
            "opening a file in text read":{

            },
            "opening a json file":{

            },  # Also I think there was a mode that let you do bot things at once im not sure
        },
        "writing to a file":{
            "writing a file in byte write":{

            },
            "writing to a file in text write":{

            },
            "writing to a json file":{

            }
        }
    },
    "algorithms":{  # there is a lot

    },
    "loops":{
        "While":{},
        "for":{}  # maybe change it to 2 different for's, for range and for item 
    },
    "datatypes":{
        "mutable strings":{

        },
        "immutable strings":{

        },
        "char":{

        },
        "integers":{
            "signed":{

            },
            "unsigned":{

            },
        },
        "float":{
            "signed":{

            },
            "unsigned":{

            },
        },
        "fixed length arrays":{

        },
        "dynamic lists(linked lists)":{

        },
        "tuple":{

        },
        "Set":{

        },
        "Dict":{

        },
        "class":{

        },
        "function":{

        },
    },
    "functions":{
        "Recursive":{

        },
        "functions that return a value":{

        },
        "functions that don't return a value":{

        },
    },
    "classes":{
    },
    "operators":{
        "arithmetic":{
            "addition":{
                "int int":{},
                "int float":{},
                "float float":{},
                "list list":{},
                "list {item}":{},
            },
            "subtraction":{
                "int int":{},
                "int float":{},
                "float float":{},
                "list list":{},
                "list {item}":{},
            },
            "multiplication":{
                "int int":{},
                "int float":{},
                "float float":{},
                "list/array int":{},
            },
            "division":{
                "int int":{},
                "int float":{},
                "float float":{},
            },
            "modulus":{
                "int int":{},
                "int float":{},
                "float float":{},
            },
            "exponentiation":{
                "int int":{},
                "int float":{},
            },
            "floor division":{
                "int int":{},
                "int float":{},
                "float float":{},
            }
        },
        "assignment":{
            "=":{},
            "+=":{},
            "-=":{},
            "*=":{},
            "/=":{},
            "%=":{},
            "//=":{},
            "**=":{},
            "&=":{},
            "|=":{},
            "^=":{},
            ">>=":{},
            "<<=":{},
        },
        "comparison":{
            "==":{},
            "!=":{},
            ">":{},
            "<":{},
            ">=":{},
            "<=":{},
        },
        "logical":{
            "and":{},
            "or":{},
            "not":{},
        },
        "identity":{ # if its the same object
            "is":{},
            "is not":{},
        },
        "membership":{
            "in":{},
            "not in":{},
        },
        "bitwise":{
            "AND":{},
            "OR":{},
            "XOR":{},
            "NOT":{},
            "ZERO FILL LEFT SHIFT":{},
            "SIGNED RIGHT SHIFT":{},
        },
    },
    "exception handling":{
        "try except":{},
        "try except finally":{},
        "rust Option":{},
        "rust Result":{},
    },
    "memory management":{ # Im not sure if this should be allocating and deallocating or Heap/Stack
        "allocation":{
            "Heap":{},
            "Stack":{},
        },
        "deallocation":{
            "Heap":{},
            "Stack":{},
        },
    }
}


py_dict = {
    "IO":{
        "opening a file":{
            "opening a file in byte read":{
                "code":"""with open("file.txt", "rb") as file:
    data = file.read()""",
                "modules":[],
                # TODO: we also need to add optional arguments of functions too!
            },
            "opening a file in text read":{
                "code":"""with open("file.txt", "r") as file:
    data = file.read()""",
                "modules":[],
            },
            "opening a json file":{
                "code":"""import json
with open("file.txt", "rb") as file:
    data = json.load(file)""",
                "modules":["json"],
            },  # Also I think there was a mode that let you do bot things at once im not sure
        },
        "writing to a file":{
            "writing a file in byte write":{
                "code":"""data = bytes("hello world!", encoding="utf-8")
with open("file.txt", "wb") as file:
    file.write(data)""",
                "modules":[],
            },
            "writing to a file in text write":{
                "code":"""data = "hello world!"
with open("file.txt", "w") as file:
    file.write(data)""",
                "modules":[],
            },
            "writing to a json file":{
                "code":"""import json
                data = {"hello":"world!"}
with open("file.txt", "w") as file:
    json.dump(data, file)""",
                "modules":["json"],
            }
        }
    },
    "algorithms":{  # there is a lot of algorithms that we can add
        "sorting":{
            "bubble sort":{
                "code":"""def bubble_sort(data):
    for i in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data""",
                "modules":[],
            },
            "insertion sort":{
                "code":"""def insertion_sort(data):
    for i in range(1, len(data)):
        j = i-1
        key = data[i]
        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key
    return data""",
                "modules":[],
            },
            "selection sort":{
                "code":"""def selection_sort(data):
    for i in range(len(data)-1):
        min_index = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data""",
                "modules":[],
            },
            "merge sort":{
                "code":"""def merge_sort(data):
    if len(data) > 1:
        mid = len(data)//2
        left = data[:mid]
        right = data[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1
    return data""",
                "modules":[],
            },
            "quick sort":{
                "code":"""def quick_sort(data):
    if len(data) > 1:
        pivot = data[0]
        left = []
        right = []
        for i in range(1, len(data)):
            if data[i] < pivot:
                left.append(data[i])
            else:
                right.append(data[i])
        quick_sort(left)
        quick_sort(right)
        data[:] = left + [pivot] + right
    return data""",
                "modules":[],
            },
            "heap sort":{
                "code":"""def heapify(data, n, i):
    largest = i 
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and data[i] < data[l]:
        largest = l
    if r < n and data[largest] < data[r]:
        largest = r
    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        heapify(data, n, largest)
def heap_sort(data):
    n = len(data)   
    for i in range(n, -1, -1):
        heapify(data, n, i)
    for i in range(n-1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)
    return data""",
                "modules":[],
            },
            "counting sort":{
                "code":"""def counting_sort(data):
    max_value = max(data)
    min_value = min(data)
    range_of_values = max_value - min_value + 1
    count = [0 for _ in range(range_of_values)]
    output = [0 for _ in range(len(data))]
    for i in range(0, len(data)):
        count[data[i]-min_value] += 1
    for i in range(1, len(count)):
        count[i] += count[i-1]
    for i in range(len(data)-1, -1, -1):    
        output[count[data[i] - min_value] - 1] = data[i]
        count[data[i] - min_value] -= 1
    for i in range(0, len(data)):
        data[i] = output[i]
    return data""",
                "modules":[],
            },
            "radix sort":{
                "code":"""def counting_sort(data, exp1):
    n = len(data)
    output = [0] * (n)
    count = [0] * (10)
    for i in range(0, n):
        index = (data[i]//exp1)
        count[(index)%10] += 1
    for i in range(1,10):
        count[i] += count[i-1]
    i = n-1
    while i>=0:
        index = (data[i]//exp1)
        output[ count[ (index)%10 ] - 1] = data[i]
        count[(index)%10] -= 1
        i -= 1
    i = 0
    for i in range(0,len(data)):
        data[i] = output[i]
def radix_sort(data):
    max1 = max(data)
    exp = 1
    while max1/exp > 0:
        counting_sort(data,exp)
        exp *= 10
    return data""",
                "modules":[],
            },
            "bucket sort":{
                "code":"""def bucket_sort(data):
    bucket = []
    for i in range(len(data)):
        bucket.append([])
    for j in data:
        index_b = int(10 * j)
        bucket[index_b].append(j)
    for i in range(len(data)):
        bucket[i] = sorted(bucket[i])
    k = 0
    for i in range(len(data)):
        for j in range(len(bucket[i])):
            data[k] = bucket[i][j]
            k += 1
    return data""", 
                "modules":[],
            },
            "shell sort":{
                "code":"""def shell_sort(data):
    gap = len(data) // 2
    while gap > 0:
        for i in range(gap, len(data)):
            temp = data[i]
            j = i
            while j >= gap and data[j - gap] > temp:
                data[j] = data[j - gap]
                j -= gap
            data[j] = temp
        gap //= 2
    return data""",
                "modules":[],
            },
            "comb sort":{
                "code":"""def comb_sort(data):
    gap = len(data)
    shrink = 1.3
    sorted = False
    while not sorted:
        gap = int(gap/shrink)
        if gap > 1:
            sorted = False
        else:
            gap = 1
            sorted = True
        i = 0
        while i + gap < len(data):
            if data[i] > data[i + gap]:
                data[i], data[i + gap] = data[i + gap], data[i]
                sorted = False
            i += 1
    return data""",
                "modules":[],
            },
            "cycle sort":{
                "code":"""def cycle_sort(data):
    writes = 0  
    for cycleStart in range(0, len(data) - 1):  
        item = data[cycleStart]
        pos = cycleStart
        for i in range(cycleStart + 1, len(data)):
            if data[i] < item:
                pos += 1
        if pos == cycleStart:
            continue
        while item == data[pos]:
            pos += 1
        data[pos], item = item, data[pos]
        writes += 1
        while pos != cycleStart:
            pos = cycleStart
            for i in range(cycleStart + 1, len(data)):
                if data[i] < item:
                    pos += 1
            while item == data[pos]:
                pos += 1
            data[pos], item = item, data[pos]
            writes += 1
    return data""",
                "modules":[],
            },
        },
    },
    "loops":{
        "While":{
            "condition":{
                "code":"""a = 10
b = 10
while a == b:
    print("Printing because a is equal to b")"""
            },
            "simple":{  # Idk what to name this
                "code":"""while True:
    print("I will print this unless you break out of this loop")
    """
            }
        },
        "for":{
            "index from length":{
                "code":"""data = [10, 20, 30, 40]
for index in range(len(data)-1):
    print(f"index:{index} data:{data[index]}")
    # f"" allows us to format our string"""
            },
            "key from dict":{
                "code":"""dict = {"alex":24, "john":42, "mustafa":33}  # ages of people
for key in dict.keys():
    print(key)
                """
            },
            "value from dict":{
                "code":"""dict = {"alex":24, "john":42, "mustafa":33}  # ages of people
for value in dict.values():
    print(value)
                """
            },
            "key and value from dict":{
                "code":"""dict = {"alex":24, "john":42, "mustafa":33}  # ages of people
for key, value in dict.items():
    print(key, value)
                """
            },
            "item from list":{
                "code":"""list = ["apple", "orange", "banana"]
for item in list:
    print(item)
                """
            },
            
        }  # maybe change it to 2 different for's, for range and for item 
    },
    "datatypes":{
        "mutable strings":{
            "str":{  # Idk what to put here other than this
                "code":"""name="Mary"
                print(name)
                """
            }
        },
        "immutable strings":{  # Idk what to put here, this is python
        },
        "char":{
            "chr":{
                "code":"""character = chr(65)
print(character)
# A"""
            }
        },
        "integers":{
            "signed":{

            },
            "unsigned":{

            },
        },
        "float":{
            "signed":{

            },
            "unsigned":{

            },
        },
        "fixed length arrays":{

        },
        "dynamic lists(linked lists)":{

        },
        "tuple":{

        },
        "Set":{

        },
        "Dict":{

        },
        "class":{

        },
        "function":{

        },
    },
    "functions":{
        "Recursive":{

        },
        "functions that return a value":{

        },
        "functions that don't return a value":{

        },
    },
    "classes":{
    },
    "operators":{
        "arithmetic":{
            "addition":{
                "int int":{},
                "int float":{},
                "float float":{},
                "list list":{},
                "list {item}":{},
            },
            "subtraction":{
                "int int":{},
                "int float":{},
                "float float":{},
                "list list":{},
                "list {item}":{},
            },
            "multiplication":{
                "int int":{},
                "int float":{},
                "float float":{},
                "list/array int":{},
            },
            "division":{
                "int int":{},
                "int float":{},
                "float float":{},
            },
            "modulus":{
                "int int":{},
                "int float":{},
                "float float":{},
            },
            "exponentiation":{
                "int int":{},
                "int float":{},
            },
            "floor division":{
                "int int":{},
                "int float":{},
                "float float":{},
            }
        },
        "assignment":{
            "=":{},
            "+=":{},
            "-=":{},
            "*=":{},
            "/=":{},
            "%=":{},
            "//=":{},
            "**=":{},
            "&=":{},
            "|=":{},
            "^=":{},
            ">>=":{},
            "<<=":{},
        },
        "comparison":{
            "==":{},
            "!=":{},
            ">":{},
            "<":{},
            ">=":{},
            "<=":{},
        },
        "logical":{
            "and":{},
            "or":{},
            "not":{},
        },
        "identity":{ # if its the same object
            "is":{},
            "is not":{},
        },
        "membership":{
            "in":{},
            "not in":{},
        },
        "bitwise":{
            "AND":{},
            "OR":{},
            "XOR":{},
            "NOT":{},
            "ZERO FILL LEFT SHIFT":{},
            "SIGNED RIGHT SHIFT":{},
        },
    },
    "exception handling":{
        "try except":{},
        "try except finally":{},
        "rust Option":{},
        "rust Result":{},
    },
    "memory management":{ # Im not sure if this should be allocating and deallocating or Heap/Stack
        "allocation":{
            "Heap":{},
            "Stack":{},
        },
        "deallocation":{
            "Heap":{},
            "Stack":{},
        },
    }
}

js_dict = {

}

rust_dict = {

}




