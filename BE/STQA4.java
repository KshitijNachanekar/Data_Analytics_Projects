
// Write a Selenium WebDriver script in Java to log in to SauceDemo, add the “Sauce Labs Backpack” to the cart, 
// proceed to checkout, enter customer details, finish the order, and verify the order confirmation message.
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.time.Duration;

public class STQA4 {

    public static void main(String[] args) {

        // Launch Chrome browser
        WebDriver driver = new ChromeDriver();

        try {
            // Open SauceDemo website
            driver.get("https://www.saucedemo.com/");

            // Maximize browser window
            driver.manage().window().maximize();

            // Create explicit wait
            WebDriverWait wait = new WebDriverWait(
                    driver, Duration.ofSeconds(10));

            // Step 1: Enter login credentials
            driver.findElement(By.id("user-name"))
                    .sendKeys("standard_user");

            driver.findElement(By.id("password"))
                    .sendKeys("secret_sauce");

            // Click Login button
            driver.findElement(By.id("login-button"))
                    .click();

            // Wait for Products page
            wait.until(ExpectedConditions.visibilityOfElementLocated(
                    By.className("title")));

            // Step 2: Add Sauce Labs Backpack to cart
            driver.findElement(
                    By.id("add-to-cart-sauce-labs-backpack"))
                    .click();

            // Step 3: Click shopping cart
            driver.findElement(
                    By.className("shopping_cart_link"))
                    .click();

            // Wait for cart page
            wait.until(ExpectedConditions.visibilityOfElementLocated(
                    By.id("checkout")));

            // Step 4: Click Checkout button
            driver.findElement(By.id("checkout")).click();

            // Step 5: Enter customer details
            wait.until(ExpectedConditions.visibilityOfElementLocated(
                    By.id("first-name")));

            driver.findElement(By.id("first-name"))
                    .sendKeys("John");

            driver.findElement(By.id("last-name"))
                    .sendKeys("Doe");

            driver.findElement(By.id("postal-code"))
                    .sendKeys("12345");

            // Click Continue button
            driver.findElement(By.id("continue")).click();

            // Step 6: Wait for Checkout Overview page
            wait.until(ExpectedConditions.visibilityOfElementLocated(
                    By.id("finish")));

            // Step 7: Click Finish button
            driver.findElement(By.id("finish")).click();

            // Step 8: Verify order confirmation message
            WebElement confirmation = wait.until(
                    ExpectedConditions.visibilityOfElementLocated(
                            By.className("complete-header")));

            String message = confirmation.getText();

            if (message.equals("Thank you for your order!")) {
                System.out.println("Order placed successfully!");
                System.out.println("Confirmation Message: " + message);
                System.out.println("TEST PASSED");
            } else {
                System.out.println("Order confirmation failed!");
                System.out.println("TEST FAILED");
            }

        } finally {
            // Close browser
            driver.quit();
        }
    }
}
