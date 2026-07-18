# React Hooks

## What are Hooks?

Hooks are special functions that allow functional components to use React features such as state and lifecycle methods.

## Common Hooks

### 1. useState
Used to store and update data.

Example:

```javascript
const [count, setCount] = useState(0);
```

### 2. useEffect
Used to perform side effects like fetching data, timers, or updating the document title.

Example:

```javascript
useEffect(() => {
    console.log("Component Loaded");
}, []);
```

## Benefits

- Cleaner code
- No need for class components
- Easy state management
