using System;
using System.Threading.Tasks;//Gives access to Task, Task.Delay(), async, and await.

class Program
{
    static async Task<string> GetMessageAsync()//static Means this method belongs to the class.You can call it directly without creating an object.
    {
        await Task.Delay(2000);//await Means Wait for this task to finish, but don't block the application.
        return "Hello Sanika";
    }

    static async Task Main(string[] args)
    {
        string message = await GetMessageAsync();//This is the entry point of the program. Execution always starts here.
        Console.WriteLine(message);
    }
}