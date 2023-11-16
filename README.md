# NTPU Fall 2023 DSP Homework #2

Source code is hosted at https://github.com/twolights/ntpu-dsp-homework2

# Pre-requisites

1. Python 3.8+ (only tested on 3.8.17 though)
2. NumPy
3. matplotlib
4. virutalenv
5. pip

# Before Running the Code

1. Setup virtualenv
 ```shell
# virtualenv `which python3` env
 ```
2. Activate virtualenv
```shell
# ./env/bin/activate
```
3. Install dependency packages
```shell
# pip install -r requirements.txt
```

# How to Run the Code

### Generate all the figures

```shell
# python3 main.py
```

or 

```shell
# python3 main.py gen
```

### Generate specific figure

#### Generate figure (a)

```shell
# python3 main.py gen a
```

#### Generate figure (d)

```shell
# python3 main.py gen d
```

### Show all the figures

```shell
# python3 main.py show
```

### Show specific figure

#### Show figure (a)

```shell
# python3 main.py show a
```

#### Show figure (c)

```shell
# python3 main.py show c
```

Note: available options are a, b, c and d
