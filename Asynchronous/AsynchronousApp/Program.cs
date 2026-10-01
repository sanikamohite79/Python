using System;
using System.Threading.Tasks;

class Program
{
    // Simulate fetching data from a database or API
    static async Task<string> FetchDataAsync()
    {
        // Wait for 2 seconds
        await Task.Delay(2000);

        return "Data fetched successfully!";
    }

    // Process the fetched data
    static async Task ProcessDataAsync()
    {
        try
        {
            // Call FetchDataAsync() and wait for the result
            string data = await FetchDataAsync();

            // Display the fetched data
            Console.WriteLine(data);

            // Process the data
            Console.WriteLine("Processing data...");
        }
        catch (Exception ex)
        {
            Console.WriteLine("Oops! Something went wrong: " + ex.Message);
        }
    }

    // Program starts here
    static async Task Main(string[] args)
    {
        Console.WriteLine("Processing started...");

        await ProcessDataAsync();

        Console.WriteLine("Processing completed.");
    }
}