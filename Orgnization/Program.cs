using Orgnization;
public class Program
{
public static void Main (string [] args)
  {
      Manager mgr =new Manager();


      double Inc=mgr.CalculateIncentives ();

      Console.WriteLine();

      double sal=mgr.CalculateSalary ();

         Console.WriteLine();

       Console.WriteLine(mgr);
  }
}