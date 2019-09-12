using System;
using OpenQA.Selenium.Firefox;
using OpenQA.Selenium;


namespace SeleniumTest
{
    class Program
    {
        static void Main(string[] args)
        {
            System.Environment.SetEnvironmentVariable("geckodriver.exe", "..");
            IWebDriver driver = new FirefoxDriver();
            driver.Navigate().GoToUrl("http://www.google.com.ar");
            /*driver.Manage().Window.Maximize();
            IWebElement buscador = driver.FindElement(By.Name("q"));
            buscador.SendKeys("C# y Selenium");
            Console.WriteLine("20 vueltas para esto");
            driver.Close();*/
        }
    }
}
