# Verification Code Generator

## Introduction

A tool to help you generator a random verification code.

Do you need to judge if a request is truly sent from real person or from a script? A verification code may help you a
lot. With a verification code, you can easily recognize the normal requests and make your website return a quick
response.

## How to use

This Python file includes a function named `check_code`. It has five parameters. They are `width` and `height`: to state
the size of the verification code; `char_length`: to state the number of letters in it; `font_file` and `font_size`: to
state the settings about font of the letter in verification code. **You should notice that font file and the Python
files should be in the same directory.**

This function returns two parameters. The first is the verification code generated, the second is the answer of it.

## Dependencies

pillow=9.2.0

## Thanks

[wupeiqi](https://www.cnblogs.com/wupeiqi/articles/5812291.html)