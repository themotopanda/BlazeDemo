// import org.openqa.selenium.By;
// import org.openqa.selenium.WebDriver;
// import org.openqa.selenium.WebElement;
// import org.openqa.selenium.chrome.ChromeDriver;
// import org.testng.Assert;
// import org.testng.annotations.Test;

// import java.util.concurrent.TimeUnit;
// import java.util.Date;
// import java.io.File;
// import org.openqa.selenium.support.ui.Select;
// import org.openqa.selenium.interactions.Actions;
// import org.openqa.selenium.chrome.ChromeDriver;
// import org.openqa.selenium.*;
// import static org.openqa.selenium.OutputType.*;



// public class blazedemo_NG {
// 	public WebDriver driver = new ChromeDriver();
// 	String demoURL = "http://www.blazedemo.com";

// @Test	
// public void launchingChrome() {		
// 	driver.get(demoURL);
// 	}
// }
import org.testng.*;
// import org.openqa.selenium;
// import org.openqa.selenium.WebDriver;
// import org.openqa.selenium.chrome.ChromeDriver;
// import org.testng.annotations.*;
// import org.openqa.selenium.*;

public class blazedemo_NG {
    ChromeDriver wd;

    @Before
    public void setUp() throws Exception {
        wd = new ChromeDriver();
        wd.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
    }

    @Test
    public void BlazeDemo() {
        wd.get("http://www.blazedemo.com");
        wd.findElement(by.cssSelector("input.btn.btn-primary")).click();
    }

    @After
    public void tearDown() {
        wd.quit();
    }
}