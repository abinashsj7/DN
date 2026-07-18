# React Routing

React Router enables navigation between pages without reloading the browser.

## Install

```bash
npm install react-router-dom
```

## Example

```javascript
import { BrowserRouter, Routes, Route } from "react-router-dom";

<BrowserRouter>
    <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
    </Routes>
</BrowserRouter>
```

## Advantages

- Single Page Application
- Faster navigation
- Better user experience
