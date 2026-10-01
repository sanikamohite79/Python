namespace Orgnization;
 public class Employee
  { 
    //Data Members  
   protected double basic_sal;
protected double hra;
protected double da;
    //Member functions

    //Constructor overloading
    public Employee(){
          this.basic_sal=5000;
          this.hra=1200;
          this.da=700;
    }

    public Employee(double bsal, double hra, double da){
        this.basic_sal=bsal;
        this.hra=hra;
        this.da=da;
    }

    public virtual double CalculateSalary ()
    {
      return basic_sal + hra+ da;
    }

    public override string ToString(){
      return base.ToString() +
      "Basic Salary ="+ this.basic_sal+
      "HRA ="+ this.hra+
      "Daily Allowance ="+ this.da;
    }
  }