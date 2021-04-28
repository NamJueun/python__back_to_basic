#!/usr/bin/env python
# coding: utf-8

# In[3]:


lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]

def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    count = len(numbers)
    average = sum(numbers) / count
    
    sorted_numbers = sorted(numbers)
    middle = count // 2
    if count % 2 == 0:
        lower = sorted_numbers[middle - 1]
        upper = sorted_numbers[middle]
        median = (lower + upper) / 2
    else:
        median = sorted_numbers[middle]
        
    return minimum, maximum, average, median, count

minimum, maximum, average, median, count = get_stats(lengths)

print(f'최소 길이: {minimum}, 최대 길이: {maximum}')
print(f'평균: {average}, 중앙값: {median}, 개수: {count}')


# In[9]:


def careful_divide(a,b):
    try:
        return True, a/b
    except ZeroDivisionError as e:
        raise ValueError('잘못된 입력')

x,y = 5,2

try:
    result = careful_divide(x,y)
except ValueError:
    print('잘못된 입력')
else:
    print('결과는 %.1f입니다' %result)


# In[8]:


def log(sequence, message, *values):
    if not values:
        print(f'{sequence}-{message}')
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{sequence} - {message}: {values_str}')
        
log(1, '좋아하는 숫자는', 7,33)
log('좋아하는 숫자는', 7,33)
log(1, '안녕')


# In[9]:


def remainder(number, divisor):
    return number% divisor

assert remainder(20,7) == 6


# In[11]:


remainder(20,7)
remainder(20, divisor=7)
remainder(number=20, divisor=7)
remainder(divisor=7, number=20)
#remainder(number=20, 7)
#cremainder(20, number=7)


# In[12]:


my_kwargs = {
    'number':20,
    'divisor':7,
}
assert remainder(**my_kwargs) == 6


# In[16]:


my_kwargs = {
    'divisor':7,
}
assert remainder(number=20, **my_kwargs) == 6


# In[17]:


my_kwargs = {
    'number' : 20,
}
other_kwargs ={
    'divisor':7,
}
assert remainder(**my_kwargs, **other_kwargs) == 6


# In[18]:


def print_parameters(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}={value}')

print_parameters(alpha=1.5, beta=9, 감마=4)


# In[ ]:




