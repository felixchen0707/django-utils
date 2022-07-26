# Pagination Widget

## Introduction

This Python file can help you quickly add paging function into your **django** web project.

## How to use

**First**, import the `Pagination` class in this Python file and create an object. 
```python
pagination = Pagination(request, query_set)
```
|parameter|infomation|
|:-:|:-:|
|`request`|request from user|
|`query_set`|the data list you want to display|
|`page_param`|the parameter's name in the URL|
|`page_size`|the number of data in a single page|
|`width`|width of the nav-bar at the bottom|

**Then**, use `pagination.page_query_set` to get the data list which is going to show at a certain page.
```python
data_list = pagination.page_query_set
```

**Finally**, to introduce the nav-bar, you should use the following to inject the html content.
```python
html = pagination.html()
```
```html
<ul class="pagination">
    {{ html }}
</ul>
```

Now you've got it.

## Requirements

You should include **BootStrap**.