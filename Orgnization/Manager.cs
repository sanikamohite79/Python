
namespace Orgnization;

//Derived Class
  public class Manager: Employee
  { 
    private double incentive;

    public Manager():base(){
      this.incentive=0;
    }

    public Manager(double bsal, double hra, double da, double incentive):
                  base(bsal, hra, da)  //Member Initialized List
    {
      this.incentive=incentive;
    }

    public double CalculateIncentives ()
    {
      //code to calculate incentives
      return incentive*2;
    }
    
    //Method overriding
    public override double CalculateSalary ()
    {
      return basic_sal + hra+ da + CalculateIncentives();
    }

    public override string ToString(){
      return base.ToString() + "Incentive ="+ this.incentive;
    }
  }
