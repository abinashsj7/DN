# React Component Lifecycle

In functional components, lifecycle events are handled using the useEffect hook.

## Component Mount

```javascript
useEffect(() => {
    console.log("Component Mounted");
}, []);
```

## Component Update

```javascript
useEffect(() => {
    console.log("Data Updated");
}, [count]);
```

## Component Unmount

```javascript
useEffect(() => {
    return () => {
        console.log("Component Unmounted");
    };
}, []);
```
