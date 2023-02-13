main_dict = {
    "IO":{
        "opening a file":{
            "opening a file in byte read":{
                
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
    "algorithms":{  # there is a lot

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




