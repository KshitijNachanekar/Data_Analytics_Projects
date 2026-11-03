
// Write a Selenium WebDriver script in Java to log in to SauceDemo, add the “Sauce Labs Backpack” to the cart,
//  proceed to checkout, enter customer details, finish the order, and verify the order confirmation message.
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.time.Duration;

public class SauceDemoCheckout {

    public static void main(String[] args) {

        // Launch Chrome browser
        WebDriver driver = new ChromeDriver();

        try {
            // Open SauceDemo website
            driver.get("https://www.saucedemo.com/");

            // Maximize browser
            driver.manage().window().maximize();

            // Create explicit wait
            WebDriverWait wait = new WebDriverWait(
                    driver, Duration.ofSeconds(10));

            // 1. Login to SauceDemo
            driver.findElement(By.id("user-name"))
                    .sendKeys("standard_user");

            driver.findElement(By.id("password"))
                    .sendKeys("secret_sauce");

            driver.findElement(By.id("login-button"))
                    .click();

            // Wait for Products page
            wait.until(ExpectedConditions.visibilityOfElementLocated(
                    By.className("title")));

            // 2. Add Sauce Labs Backpack to cart
            driver.findElement(
                    By.id("add-to-cart-sauce-labs-backpack"))
                    .click();

            // 3. Open shopping cart
            driver.findElement(
                    By.className("shopping_cart_link"))
                    .click();

            // 4. Click Checkout
            driver.findElement(By.id("checkout")).click();

            // 5. Enter customer details
            wait.until(ExpectedConditions.visibilityOfElementLocated(
                    By.id("first-name")));

            driver.findElement(By.id("first-name"))
                    .sendKeys("John");

            driver.findElement(By.id("last-name"))
                    .sendKeys("Doe");

            driver.findElement(By.id("postal-code"))
                    .sendKeys("12345");

            // Click Continue
            driver.findElement(By.id("continue")).click();

            // 6. Wait for Checkout Overview page
            wait.until(ExpectedConditions.visibilityOfElementLocated(
                    By.id("finish")));

            // 7. Finish the order
            driver.findElement(By.id("finish")).click();

            // 8. Verify order confirmation
            WebElement confirmation = wait.until(
                    ExpectedConditions.visibilityOfElementLocated(
                            By.className("complete-header")));

            String message = confirmation.getText();

            if (message.equals("Thank you for your order!")) {
                System.out.println("Order placed successfully!");
                System.out.println("Confirmation: " + message);
                System.out.println("TEST PASSED");
            } else {
                System.out.println("TEST FAILED");
            }

        } finally {
            // Close browser
            driver.quit();
        }
    }
}
