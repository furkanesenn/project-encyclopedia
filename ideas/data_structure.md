# Data structure
I think we could store universal, non-language dependant snippets in a dict that has multiple sub directories inside it
like this
```py
{
    "IO":{
        "Opening a file":{
            "Opening a file in byte read":{
                "py":{
                    "recommended way":{
                        "code":"""...""",
                        "libraries used":[],

                    }
                },
                "js":{

                },
                "rust":{

                }
            },
        },
        "Writing to a file"{
            "Writing a file in byte write",
        }
    },
    "Algorithms":{},
    "Loops":{}
}
```

## Languages
Each language would have its own dict, and those dicts would use keys of the main, non language-dependant dict's as keys
for example:
```py
python_data = {
    "IO":{
        "Opening a file":{
            "Opening a file in byte read":{
                code:"""...""",  # We could also put different versions that accomplish the same thing
                "perf":"", # could be used for algorithms
                "libraries used":"none",  # maybe
                "tags":["io", "file", "opening a file"]
            }
        }
    }
}
```

Idk how fast this would be or would we even have problems with optimization
we will also convert this to sql if I remember correctly

I think we should just save these in (main dict and programming-languages, then convert them to sql data using an automated tool)

Furkan also said that we should store how the code is ran (compiled, jit compiled, interpreted etc.)

