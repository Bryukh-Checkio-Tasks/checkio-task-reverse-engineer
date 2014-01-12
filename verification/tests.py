"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "01":
        {
            "expression": "x+y",
            "answer": "x+y"
        },
    "02":
        {
            "expression": "x-y",
            "answer": "x-y"
        },
    "03":
        {
            "expression": "x*y",
            "answer": "x*y"
        },
    "04":
        {
            "expression": "x//y",
            "answer": "x/y"
        },
    "05":
        {
            "expression": "x-x+y",
            "answer": "x-x+y"
        },
    "06":
        {
            "expression": "(x+x)*y",
            "answer": "(x+x)*y"
        },
    "07":
        {
            "expression": "(x+y)//x",
            "answer": "(x+y)/x"
        },
    "08":
        {
            "expression": "(x-y)*(x+y)",
            "answer": "(x-y)*(x+y)"
        },


}
