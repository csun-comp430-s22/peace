# Peace

An imperative language that adds algrebraic datatypes, 
pattern matching, and better function pointer syntax to C.

This language was developed for a language design and compilers course at
at California State University Northridge. 

## Features

### Basic Syntax

```
string printZero(x: int) {
	if (x == 0) {
    	     let zero: string = 'zero';
    	     return zero;
	} else {
    	     let notZero: string = 'not a zero';
    	     return notZero;
	}
}

void main() {
	let x: int = 3;
	let signal: bool = True;
	let someVar: string = '';
    
	while (signal == True) {
    	     if (x > 0) {
        	     x = x - 1;
    	     } else {
                 signal = False;
           }
	}

	someVar = printZero(x);
      print(someVar);
}
```

### Function Pointers

Function pointers allow variables to point to code instead of just data. They can be used to avoid code repetition, allow developers to provide custom implementations of some part of a function (such as a compare function when sorting), and provide implementations of a function for various types.

```
int add(x: int, y: int)
{
    return x + y;
}

int multiply(x: int, y: int)
{
    return x * y;
}

int performOp(x: int, y: int, op: (int, int) -> int)
{
    return op(x, y);
}

void main()
{
    let target_op: (int, int) -> int = &add;
    let result = performOp(2, 3, target_op);
}
```

### Algebraic Data Types

Some example uses of algebraic data types that we were familiar with were sum-types like linked lists. An example of this would be:

```
enum list {
    cons: string, list;
    nil: void;
}

void adtExample() {
    let groceries: list = cons('carrots', nil());
}
```

Here we can construct an enum named list, which holds two values, cons and a nil. Cons holds two values, a string and another list object. In the main block, a list named groceries is created, holding a cons which contains ‘carrots’ and a nil instance to indicate the end of the list.

### Pattern Matching

Pattern matching is an ergonomic feature that we chose to implement because we felt it would be a useful addition to C. An example of this would be:

```
void printList(a: list)
{
    match a {
   	 cons(x, y) => { 
          print(x); 
          printList(y); 
       },
   	 nil() => { print("Done shopping"); }
    }
}

void matchExample() {
    let shopping: list = cons('carrots', cons('milk', cons('bread', nil())));

    printList(shopping);
}
```

Using the list algebraic data type example above, pattern matching is used to recursively print out a list named shopping, which holds items of a grocery list and indicates when it is completed.

```
void matchExample() {
    let x: int = 10;

    match x {
   	 0 => {print('zero');}
   	 5 => {print('five');}
   	 10 => {print('ten');}
    }
}
```

Comparisons that would otherwise require many if statements can instead be replaced with a match statement.

## Known limitations

There is no working code generator. The language has no built-in way to free memory.

## How do I run the compiler?

Besides Python 3 (>3.10), the ANTLR4 runtime is the only dependency. You can install it via pip:

`pip install antlr4-python3-runtime`

To compile a program:

`python peace.py myprogram.pce`

The compiler expects a plain unicode text file. The pce extension is optional. An example program is included in “example.pce”.

## Syntax

The complete grammar can be found in `peace/antlr/Peace.g4`