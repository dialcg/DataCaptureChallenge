
# DataCapture

A piece of software that let's you process simple numbers.

## Data operations

Operations over a processed data collection are 
- How many numbers in the collection are less than a value
- How many numbers in the collection are greater than a value
- How many numbers in the collection are within a range




## Installation and usage

Make sure you have at least Python 3 installed in your system

No need to use ```pip``` or ```setuptools``` as no external libraries are used in the code

To start the processor, add you collection as arg parameter

i.e:

```bash
  python3 processor.py --collection 10 11 12 13
```

Then, you will be prompted with the requiered values:

### 1st prompt: Operation selector

```bash
Write the operation that you want to execute over your collection
```

You have the next options to write for this prompt:

- greater
- less
- between

### 2nd prompt: Computation values

```bash
Write the value you want to compute (or 2 comma separated values for 'between' operation)
```

For this prompt, just write the number that you want to compute if your operation is **greater** or **less** 

If your operation is **between**, write 2 comma separated values. *i.e:* 13,20

