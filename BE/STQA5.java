
// Write a Selenium WebDriver script in Java to launch Google Chrome,
//  open https://www.saucedemo.com/, print the page title, and close the browser.
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class LaunchBrowser {

    public static void main(String[] args) {

        // Create ChromeDriver object
        WebDriver driver = new ChromeDriver();

        // Open SauceDemo website
        driver.get("https://www.saucedemo.com/");

        // Print page title
        String title = driver.getTitle();
        System.out.println("Page Title: " + title);

        // Close the browser
        driver.quit();
    }
}
