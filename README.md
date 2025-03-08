This project is designed to automate critical user flows on the Amazon platform. The test suite leverages Selenium, Pytest, and the Page Object Model (POM) design pattern to verify functionalities such as cart operations, product search, price validation, and product removal. Its purpose is to ensure the correctness and reliability of these essential workflows.

🚀Features
Product Search Tests: Verifies that specified products appear correctly in search results.

Price Validation Tests: Confirms accurate price calculation for added products on the cart page.

Product Removal Tests: Ensures products are correctly removed from the cart and validates the success message displayed afterward.

Dynamic Element Handling: Manages dynamic elements effectively using explicit waits to avoid runtime issues.

Pytest HTML Reporting: Generates comprehensive HTML reports to visualize test outcomes.

📋Test Scenarios

Product Search:

Ensures that relevant search results are displayed when a user enters a product name in the search bar.

Price Verification:

Checks if the product price updates correctly when added to the cart.

Cart Quantity Update:

Validates the functionality of increasing product quantities in the cart and the corresponding price updates.

Product Removal:

Confirms the removal of a product from the cart and checks the success message.

🛠️ Technologies Used
Language: Python

Frameworks: Selenium & Pytest

Design Pattern: Page Object Model (POM)

Reporting: Pytest HTML

Browser: Chrome (via WebDriver)
