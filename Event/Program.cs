class Program
{
    static void Main()
    {
        Account account = new Account(15000);

        account.UnderBalance += PayPenalty;
        account.UnderBalance += BlockAccount;

        account.Withdraw(12000);
    }

    static void PayPenalty()
    {
        Console.WriteLine("Pay ₹500 penalty.");
    }

    static void BlockAccount()
    {
        Console.WriteLine("Your account has been blocked.");
    }
}
