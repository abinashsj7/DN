# Props vs State

| Props | State |
|--------|-------|
| Passed from parent | Managed inside component |
| Read-only | Can be modified |
| Used for communication | Used for storing data |

## Props Example

```javascript
<Student name="Abinash" />
```

## State Example

```javascript
const [name, setName] = useState("");
```

## Difference

Props are inputs to a component.

State stores data that changes during execution.
