
namespace System;
public delegate void AccountOperation();
public class Account
{
   public int balance;

   public event AccountOperation Underbalance;

   public Account(int amount)
   {
    balance = amount;

   }

   public void Withdraw(int amount)
   {
    balance = balance - amount;
    Console.WriteLine("current balance : " + balance);

    if (balance <500)
{
    Underbalance();
}   
}
}