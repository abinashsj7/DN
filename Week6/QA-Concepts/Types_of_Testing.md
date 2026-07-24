# Types of Software Testing

Software testing is broadly classified into Functional Testing and Non-Functional Testing.

---

# Functional Testing

Functional testing verifies whether the software works according to the specified requirements.

## 1. Unit Testing
- Tests individual components or functions.
- Performed by Developers.

Example:
Testing only the login function.

---

## 2. Integration Testing
- Tests the interaction between multiple modules.

Example:
Login module communicating with the database.

---

## 3. System Testing
- Tests the complete application as a whole.

Example:
Testing an entire banking application.

---

## 4. Acceptance Testing (UAT)
- Ensures the application meets customer requirements.
- Performed by the client or end users.

---

# Non-Functional Testing

Non-functional testing evaluates performance, security, and usability.

## 1. Performance Testing
Checks the application's speed and responsiveness.

---

## 2. Load Testing
Checks system behavior under expected user load.

Example:
1000 users accessing the website simultaneously.

---

## 3. Stress Testing
Checks how the application behaves beyond its maximum capacity.

Example:
10000 users accessing a server designed for 1000 users.

---

## 4. Security Testing
Checks the application for vulnerabilities and data protection.

---

## Frequently Asked Testing Types

### Smoke Testing
- Verifies whether the critical functionalities work.
- Performed after a new build.

Example:
Can the application launch?
Can users log in?

---

### Sanity Testing
- Verifies that a specific bug fix works correctly.
- Narrow and focused testing.

---

### Regression Testing
- Ensures new changes do not break existing features.

Example:
After adding a payment feature, verify that login, registration, and search still work.

---

# Quick Comparison

| Testing Type | Purpose |
|--------------|---------|
| Unit Testing | Test a single module |
| Integration Testing | Test interaction between modules |
| System Testing | Test the complete application |
| Acceptance Testing | Validate customer requirements |
| Smoke Testing | Verify major functionalities |
| Sanity Testing | Verify specific fixes |
| Regression Testing | Ensure old features still work |
| Load Testing | Test expected user load |
| Stress Testing | Test beyond maximum capacity |
| Security Testing | Protect against threats |
