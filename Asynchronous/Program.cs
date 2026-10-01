
using System;
using System.Threading.Tasks;
class Program{
    static async Task Main()
    {
        Console.WriteLine("Start");
        await Task.Delay(3000);
        Console.WriteLine("Finished");
    }

}