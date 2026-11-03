//Write a Selenium WebDriver script in Java to log in to https://www.saucedemo.com/ using username standard_user 
//and password secret_sauce. Verify that the product/inventory page is displayed after login
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.time.Duration;

public class SauceDemoLogin {

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

            // Click on Login button
            driver.findElement(By.id("login-button"))
                  .click();

            // Wait for Products page to appear
            WebElement products = wait.until(
                ExpectedConditions.visibilityOfElementLocated(
                    By.className("title")));

            // Verify Products page
            if (products.getText().equals("Products")
                && driver.getCurrentUrl().contains("inventory.html")) {

                System.out.println("Login Successful!");
                System.out.println("Products page displayed successfully.");

            } else {
                System.out.println("Login Failed!");
            }

        } finally {
            // Close browser
            driver.quit();
        }
    }
}
