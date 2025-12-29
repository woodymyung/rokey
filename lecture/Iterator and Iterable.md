# Iterator and Iterable 
Iterator, Iterable 개념을 배우기 전에 Lazy evaluation이라는 철학 및 방법론을 알아보자. 
### Lazy evalution
필요한 시점에 연산을 실행하여 메모리를 아끼는 방식 및 문법을 아울러 뜻한다. 
#### 예시 
```python 
original_list = [1, 2, 3, 4, 5]
converted_list = []
for i in original_list: 
    i = i ** 2
    converted_list.append(i)
``` 
```python 
original_list = [1, 2, 3, 4, 5]
map_object = map(lambda x : x**2, original_list)
gen_iter = (x**2 for x in original_list)
```
리스트의 각 요소를 제곱한 결과를 반환해야하는 프로그램이 있다고 가정하자. 첫 번째 코드의 경우 `original_list`의 모든 요소에 대해 미리 연산을 수행하여 `converted_list`에 저장해둔다. 따라서 원소 데이터가 이미 10개의 자리를 차지한다. 반면 두 번째 코드의 경우 `map` 메소드를 사용하여 아직 어떤 리스트로 결과를 반환하지 않았다. 다만 어떤 계산식을 가진 설계도만 가지고 있는 상태이다. 따라서 두 번째 방식이 첫 번째 방식보다 더 적은 메모리를 차지한다. 이때 map 메소드를 사용하여 생성된 객체는 `iterator` 이다. 

### Iterable vs Iterator 
`Iter`라는 단어에서 유추할 수 있듯이 반복적인 특징을 가졌음을 유추할 수 있다. 여러 문서를 읽고 이해한 바에 따르면, `Iterable`과 `Iterator`는 모두 반복되는 성질을 가지는 객체인데, 차이점은 `Iterable`은 반복될 수 있는 성질을 가졌지만 값을 하나씩 반환하는 능력이 없으며, `Iterator`가 될 잠재력이 있는 객체이다. 반면 `Iterator`는 실제로 값을 하나씩 반환하는 객체로, 모든 반환이 끝나면 그 값들이 소멸되는 특징이 있다. 
</br>
파이썬 공식 문서에 정의된 내용을 살펴보자. 
- **iterable**: An object capable of returning its members one at a time. Examples of iterables include all sequence types (such as `list`, `str`, and `tuple`) and some non-sequence types like `dict`, file objects, and objects of any classes you define with an `__iter__()` method or with a `__getitem__()` method that implements sequence semantics. 
Iterables can be used in a `for` loop and in many other places where a sequence is needed(e.g. `zip()`, `map()`). When an iterable object is passed as an argument to the built-in function `iter()`, it returns an iterator for the object. 
- **iterator**: An object representing a stream of data. Repeated calls to the iterator's `__next__()` method (or passing it to the built-in function `next()`) return successive items in the stream. When no more data are available a `StopIteration` exception is raised instead. At this point, the iterator object is exhausted and any further calls to its `__next__()` method just raise `StopIteration` again. Iterators are required to have an `__iter__()` method that returns the iterator object itself so every iterator is also iterable and may be sued in most places where other iterables are accepted. ... A container object(such as a `list`) produces a fresh new iterator each time you pass it to the `iter()` function or use it in a `for` loop. Attempting this with an iterator will just return the same exhausted iterator object used in the previous pass, making it appear like an empty container. 

그렇다면 `for` 구문 안에서 일어나는 일을 살펴보자. 
```python 
for i in itrable: 
    print(i) 
```
1. `__iter__` 호출: `for` 문이 시작되자마자 객체의 `__iter()__` 메소드를 호출한다. 이때 객체는 내부 데이터를 처음부터 훑을 수 있는 새로운 iterator 객체를 생성하여 반환한다.
2. 순회: 임시 이터레이터의 `__next__()`를 호출하며 값을 하나씩 가져온다 
3. 소멸: 순회가 끝나면(`StopIteration` 발생), 임시 이터레이터는 메모리에서 해제된다. 
4. 결과: 원본 객체(`Iterable`)은 그대로 있기 때문에 이후 `for` 문을 돌리면 새로운 임시 이터레이터를 만들어 다시 처음부터 출력할 수 있다. 
```python
for i in iterator: 
    print(i)
```
1. `__iter__` 호출: `for` 문이 시작되자마자 객체의 `__iter()__` 메소드를 호출한다. 그러나 이때 새로운 iterator 객체가 생성되어 반환되는 게 아니라, 자기 자신(`self`)을 반환한다. 
2. 순회: 자기 자신(`self`)의 `__next__()`를 호출하며 값을 가져온다. 이때 내부의 `position`이 변경된다. 
3. 소진: `position`이 마지막에 도달하며 순회가 끝난다. 이때 이터레이터 객체는 버려지지 않은 채, 변수에 할당되어있으나 소진된 상태로 남는다.
4. 결과: 다시 `for` 문을 돌려도 `__iter__()`는 여전히 마지막 `position`에 도달한 `self`를 반환하므로, 아무 값도 나오지 않는다. 

- Iteratior has a state. Whenever it executes `next`, the item get by iterator is forgotten. Iterator, a special obejct, do the well defiend works. 
- list 는 iterable 이므로, iterator 객체를 만들 권한을 가지고 있음. 따라서, 
```python 
list = [1, 2, 3] # type(list) = list(iterable)
iterator = iter(list) # type(iterator) = iterator
```

- iterable 는 영구적으로 사용 가능
- iterator는 iterable을 이용하여 만든 객체로, 값을 하나씩 반환하며 한번 반환한 값은 그 객체에서 소모되는 성질을 가지고 있다. 


- iterable 객체는 특정 Class 로부터 생성되었는데, 이 클래스 안에는 `__iter__()`라는 메서드가 정의되어있고, 이 메서드를 호출하면 iterator 객체를 반환한다. 


- generator: A function that returns a generator iterator. It looks like a noraml function except that it cotains `yield` expressions for producing a series of values usable in a for-loop or that can be retrieved one at a time with the `next()` function.
- generator iterator: An object created by a `generator` function. 
    - Each `yield` temporarily suspends processing, remembering the execution state (including local variables and pending tryp-statements). When the generator iterator resumes, it picks up where it left off. 
- generator exrpession: An expression that returns an iterator. It looks like a normal expression followed by a for clause defining a loop variable, range, and an optional if clause. THe combined expression generates values for an enclosing funciton: 
