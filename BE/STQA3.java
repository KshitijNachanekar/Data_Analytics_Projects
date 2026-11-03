// Write a Selenium WebDriver script in Java to log in to SauceDemo, add the “Sauce Labs Backpack” 
// to the shopping cart, and verify that the cart badge displays 1.
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.time.Duration;

public class AddToCart {

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

            // Enter username
            driver.findElement(By.id("user-name"))
                  .sendKeys("standard_user");

            // Enter password
            driver.findElement(By.id("password"))
                  .sendKeys("secret_sauce");

            // Click Login button
            driver.findElement(By.id("login-button"))
                  .click();

            // Wait for Products page
            wait.until(ExpectedConditions.visibilityOfElementLocated(
                By.className("title")));

            // Add Sauce Labs Backpack to cart
            driver.findElement(By.id("add-to-cart-sauce-labs-backpack"))
                  .click();

            // Wait for cart badge
            WebElement cartBadge = wait.until(
                ExpectedConditions.visibilityOfElementLocated(
                    By.className("shopping_cart_badge")));

            // Verify cart badge count
            String count = cartBadge.getText();

            if (count.equals("1")) {
                System.out.println("Product added successfully!");
                System.out.println("Cart badge displays: " + count);
                System.out.println("Test Passed!");
            } else {
                System.out.println("Test Failed!");
            }

        } finally {
            // Close browser
            driver.quit();
        }
    }
}
