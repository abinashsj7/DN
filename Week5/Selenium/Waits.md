# Selenium Waits

Implicit Wait

```python
driver.implicitly_wait(10)
```

Explicit Wait

```python
WebDriverWait(driver,10).until(...)
```

Explicit waits are preferred for dynamic pages.
