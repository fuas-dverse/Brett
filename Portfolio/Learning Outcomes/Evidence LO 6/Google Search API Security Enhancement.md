# [[Google Search API Security Enhancement]]

## Context
This project focuses on enhancing the security of an API that integrates Google Search functionalities. I implement and validate numerous security measures using a comprehensive testing strategy. This document details my approach to testing the security features of the API.

## Security Features
### Implemented Security Headers
To protect against common web vulnerabilities, the application incorporates several crucial HTTP security headers:
1. **Content-Security-Policy (CSP)**: `default-src 'self'`
    - Restricts resources (scripts, images, etc.) to the domain of the website, preventing XSS attacks and data injections.
2. **X-Content-Type-Options**: `nosniff`
    - Prevents the browser from MIME-sniffing the content type, blocking the execution of non-executable MIME types as executable.
3. **X-Frame-Options**: `DENY`
    - Stops the application from being displayed in a frame or iframe, protecting against clickjacking.
4. **X-XSS-Protection**: `1; mode=block`
    - Enables the browser's built-in filter to prevent detected XSS attacks by blocking the entire page.
5. **Referrer-Policy**: `no-referrer`
    - Directs the browser to omit HTTP Referrer headers to increase privacy and security.
6. **Strict-Transport-Security (HSTS)**: `max-age=63072000; includeSubDomains`
    - Forces the browser to connect to the API over HTTPS, reducing the risk of man-in-the-middle attacks.

### Authentication
The API uses a key-based authentication mechanism where each request must include a valid API key in the `Authorization` header, ensuring that access is granted only to authenticated users.

## Testing with pytest
### Testing Configuration
I use `pytest` to implement automated tests that ensure the API's security features are functioning as intended.

- **Test Execution Command:**
```bash
pytest --cov=app --cov-report=term --cov-fail-under=90
```
This setup mandates that the code coverage for the `app` module remains above 90%. If the coverage dips below this threshold, the test suite will fail, indicating insufficient test coverage and potentially untested code paths.

### Key Test Scenarios
My tests focus primarily on security aspects:
- **Security Headers Validation**: Tests verify that all security headers are correctly set in the responses from the API. Each header's presence and configuration are checked to ensure they comply with the security policies defined.
- **Authentication Checks**: I perform tests to confirm that requests without a valid API key are denied access. Additional tests verify that providing a valid API key permits access, ensuring the authentication system functions as expected.
- **Input Validation**: Tests ensure that the API correctly handles various inputs, rejecting malformed or dangerous requests that could lead to security vulnerabilities.

## CI/CD Pipeline Focused on Testing
The CI/CD pipeline integrates my testing strategy:

### CI/CD Configuration in GitHub Actions
- **Workflow Name**: "Security Tests for Google Search API"
- **Environment**: Runs on `ubuntu-latest`

### Steps
1. **Check Out Code**:
    - The latest code is checked out using the GitHub Actions `checkout@v2`.
2. **Set Up Python**:
    - Python is set up with the specified version to ensure compatibility and consistency across testing environments.
3. **Install Dependencies**:
    - Dependencies are installed as per `requirements.txt`, setting up the necessary environment for testing.
4. **Run Tests and Check Coverage**:
    - The `pytest` command runs the security tests, enforcing the coverage threshold to ensure high code quality and security.

### Trigger
- The pipeline is triggered only on changes in the directory `./GoogleSearchAgent`, the tests are being trigged on each branch. The build and deployment is being triggered only on the `main` branch.

## Conclusion
Through rigorous security testing using `pytest` and a disciplined CI approach, this project ensures that the Google Search API integration maintains robust security defenses against potential threats. This dedicated focus on security helps safeguard sensitive data and functionalities against exploitation.