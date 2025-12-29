# Iterator 
Iterator 관련 개념을 배우기 전에 Lazy evaluation에 대해 알아보자. 
## 0. Lazy evalution
- 엄밀한 정의(Feat. Gemini): Lazy Evaluation은 연산 요청을 'Thunk(썽크)'로 감싸서 지연시키고(Deferral), 실제 값이 필요할 때(Forcing) 연산을 수행하며, 그 결과를 메모리에 캐싱(Memoization)하여 중복 연산을 방지하는 'Call-by-need' 평가 전략이다.
- 비유적인 정의: 어떤 자연수의 제곱을 계산해야 할 때, 모든 자연수의 제곱을 미리 계산한 결과를 저장해두는 방식과 대조적으로 필요할 때만 계산기를 꺼내 값을 구하는 방식

#### 파이썬에서의 Lazy evaluation
파이썬은 언어 전체가 Lazy한 언어는 아니지만, iterator를 통해 lazy evaluation 의 철학(?)을 구현할 수 있다. lazy evaluation 으로 분류되는 연산은 연산 결과를 메모리에 미리 올리는 대신, 결과를 생성할 방법과 현재 상태를 포장해둔다. generator(`yield`), iterator 객체(e.g. `map`), `range` 객체가 그 예시이다. 

## 1. Iterator
### Iterable vs Iterator 
`Iter`라는 단어에서 유추할 수 있듯이 반복적인 특징을 가졌음을 유추할 수 있다. 여러 문서를 읽고 이해한 바에 따르면, `Iterable`과 `Iterator`는 모두 반복되는 성질을 가지는 객체인데, 차이점은 `Iterable`은 반복될 수 있는 성질을 가졌지만 값을 하나씩 반환하는 능력이 없으며, `Iterator`가 될 잠재력이 있는 객체이다. 반면 `Iterator`는 실제로 값을 하나씩 반환하는 객체로, 모든 반환이 끝나면 그 값들이 소멸되는 특징이 있다. 
</br>
파이썬 공식 문서에 정의된 내용을 살펴보자. 
- **iterable**: An object capable of returning its members one at a time. Examples of iterables include all sequence types (such as `list`, `str`, and `tuple`) and some non-sequence types like `dict`, file objects, and objects of any classes you define with an `__iter__()` method or with a `__getitem__()` method that implements sequence semantics. 
Iterables can be used in a `for` loop and in many other places where a sequence is needed(e.g. `zip()`, `map()`). When an iterable object is passed as an argument to the built-in function `iter()`, it returns an iterator for the object. 
- **iterator**: An object representing a stream of data. Repeated calls to the iterator's `__next__()` method (or passing it to the built-in function `next()`) return successive items in the stream. When no more data are available a `StopIteration` exception is raised instead. At this point, the iterator object is exhausted and any further calls to its `__next__()` method just raise `StopIteration` again. Iterators are required to have an `__iter__()` method that returns the iterator object itself so every iterator is also iterable and may be sued in most places where other iterables are accepted. ... A container object(such as a `list`) produces a fresh new iterator each time you pass it to the `iter()` function or use it in a `for` loop. Attempting this with an iterator will just return the same exhausted iterator object used in the previous pass, making it appear like an empty container. 
    - Reddit에서 좀 더 직관적인 설명이 있어 첨부: 이터레이터는 상태를 가지고 있어: `next`을 할 때마다, 얻는 아이템은 이터레이터에 의해 잊혀져. 이건 아주 특정한 종류의 객체인데, 아주 특정한, 잘 정의된 동작을 해. 이터러블은 그런 제약이 없어. 어떤 종류의 객체든 될 수 있는데, 길이를 가질 수도 있고, 소모될 수도 있고, 인덱싱이 가능할 수도 있고, 아닐 수도 있고, 등등. "이터러블"하게 만드는 유일한 건 `__iter__` 메서드를 정의한다는 거야. 그래서 `iter(thing)` 을 해서 실제 이터레이터를 얻을 수 있어 (알 수 없거나 복잡한 동작을 하는 일반 객체에서, 잘 정의되고 제한된 동작을 하는 아주 특정한 이터레이터 객체로 변환하는 거지).

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

## 2. Generator
- generator: A function that returns a generator iterator. It looks like a noraml function except that it cotains `yield` expressions for producing a series of values usable in a for-loop or that can be retrieved one at a time with the `next()` function.
- generator iterator: An object created by a `generator` function. 
    - Each `yield` temporarily suspends processing, remembering the execution state (including local variables and pending tryp-statements). When the generator iterator resumes, it picks up where it left off. 
- generator exrpession: An expression that returns an iterator. It looks like a normal expression followed by a for clause defining a loop variable, range, and an optional if clause. THe combined expression generates values for an enclosing funciton: 
### 2.1. Generator comprehension
```python

```
#### map vs generator comprehension 