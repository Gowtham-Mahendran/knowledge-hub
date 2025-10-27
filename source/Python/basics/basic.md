## Print statement reduction


```python
print("\nPhase-A Components:")
print("E0 =", Eao)
print("E1 =", Ea1)
print("E2 =", Ea2)
```
It can be written in the `f-string` format

```python
print(f"Phase-A components: Ea0 = {Eao}, Ea1 = {Ea1}, Ea2 = {Ea2}")
```

The result will be like

```text
Phase-A components: Ea0 = (28+15j), Ea1 = (72.289692+11.553760000000002j), Ea2 = (-40.28934-26.5531j)
```

It is also possible to round off using `f-string`
```python
print(f"Phase-A components: Ea0 = {Eao:.2f}, Ea1 = {Ea1:.2f}, Ea2 = {Ea2:.2f}")
```

```text
Phase-A components: Ea0 = 28.00+15.00j, Ea1 = 72.29+11.55j, Ea2 = -40.29-26.55j
```



(.venv)  gowtham@debian  ~/Documents/power-system/seq-tool  python
Python 3.12.11 (main, Sep 18 2025, 19:47:19) [Clang 20.1.4 ] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import matplotlib.pyplot as plt
>>> fig, ax = plt.subplots()
>>> help(ax)

>>> for x in dir(ax):
...     if not x.startswith("_"):
...         print(x)
... 
